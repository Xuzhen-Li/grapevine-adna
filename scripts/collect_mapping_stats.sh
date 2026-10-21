#!/usr/bin/env bash

samples=(
SAMPLE_01 SAMPLE_02  # ...
)

output="stats.all.tsv"
echo -e "SampleID\tRawReads\tMappedReads\tQ30Reads\tDupReads\tDedupBases" > "$output"

debug_log="stats_debug.log"
echo "==== 开始运行统计脚本 ====" > "$debug_log"

extract_value() {
    local filename=$1
    local grep_str=$2

    echo "尝试读取文件: $filename" >> "$debug_log"
    [[ -f "$filename" ]] || { echo "[WARNING] 文件不存在: $filename" >> "$debug_log"; echo "NA"; return 1; }

    echo "文件内容前10行:" >> "$debug_log"
    head -n 10 "$filename" >> "$debug_log"

    local value=$(grep -m1 "$grep_str" "$filename" | awk '{gsub(/[^0-9]/, "", $1); print $1}')
    [[ -n "$value" ]] || { echo "[WARNING] 未找到匹配模式 '$grep_str' 的数值" >> "$debug_log"; echo "NA"; return 1; }

    echo "提取到的值: $value" >> "$debug_log"
    echo "$value"
}

for sample in "${samples[@]}"; do
    echo -e "\n==== 处理样本: $sample ====" >> "$debug_log"

    # 直接拼文件名
    rawreads=$(extract_value "${sample}.mapped.stats" 'in total')
    mappedreads=$(extract_value "${sample}.mapped.stats" 'primary mapped')
    q30reads=$(extract_value "${sample}.mapped.maponly.sorted.qF.bam.qF.stats" 'in total')
    dupreads=$(extract_value "${sample}.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.stats" 'primary mapped')

    dedupbase="NA"
    genome_file="${sample}.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD_stats/genome_results.txt"
    if [[ -f "$genome_file" ]]; then
        echo "=== genome_results.txt 内容片段 ===" >> "$debug_log"
        grep -A 2 "number of mapped bases" "$genome_file" >> "$debug_log"

        dedupbase=$(grep "number of mapped bases" "$genome_file" | \
                    awk -F '= ' '{print $2}' | \
                    awk '{gsub(/,| bp/, "", $1); print $1}')
        echo "提取到的DedupBases: $dedupbase" >> "$debug_log"
    else
        echo "[WARNING] 文件不存在: $genome_file" >> "$debug_log"
    fi

    printf "%s\t%s\t%s\t%s\t%s\t%s\n" \
        "$sample" \
        "${rawreads:-NA}" \
        "${mappedreads:-NA}" \
        "${q30reads:-NA}" \
        "${dupreads:-NA}" \
        "${dedupbase:-NA}" >> "$output"
done

echo -e "\n==== 脚本运行完成 ====" >> "$debug_log"
echo "统计完成！结果文件: $output"
echo "调试日志: $debug_log"
