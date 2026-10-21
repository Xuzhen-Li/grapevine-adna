#!/bin/bash

# 显式定义所有样本名称
samples=(
SAMPLE_01
SAMPLE_02
# ...
)

# 为每个样本生成处理脚本
for sample in "${samples[@]}"; do
    # 创建样本专属目录
    mkdir -p "./${sample}"
    
    # 生成脚本路径
    script_path="./${sample}/${sample}.sh"
    
    # 写入完整配置和命令
    cat > "${script_path}" << EOF
#!/bin/bash
#SBATCH --job-name=${sample}
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=20
#SBATCH --partition=<PARTITION>
#SBATCH -o ./${sample}/${sample}.out
#SBATCH -e ./${sample}/${sample}.err

# 进入工作目录
cd "./${sample}" || { echo "无法进入目录 ${sample}"; exit 1; }

# 原始数据处理
AdapterRemoval \\
  --file1 ../${sample}_1.fq.gz \\
  --file2 ../${sample}_2.fq.gz \\
  --qualitybase 33 \\
  --qualitybase-output 33 \\
  --trimqualities \\
  --minquality 2 \\
  --trimns \\
  --minlength 25 \\
  --basename ${sample} \\
  --collapse \\
  --gzip \\
  --threads 20

# 比对处理
bwa aln \\
  -l 1024 \\
  -n 0.01 \\
  -f ${sample} \\
  -t 20 \\
  <REF_DIR>/VS1.final.fa \\
  ${sample}.collapsed.gz

bwa samse \\
  -r "@RG\\tID:${sample}\\tSM:${sample}" \\
  -f ${sample}.collapsed.sam \\
  <REF_DIR>/VS1.final.fa \\
  ${sample} \\
  ${sample}.collapsed.gz

# SAM转BAM
samtools view -@ 20 -Sb -o ${sample}.mapped.bam ${sample}.collapsed.sam || exit 1
samtools flagstat -@ 20 ${sample}.mapped.bam > ${sample}.collapsed.stats

# 初级过滤
samtools view -@ 20 -F4 -b ${sample}.mapped.bam -o ${sample}.mapped.maponly.bam
samtools sort -@ 20 -m 4G -o ${sample}.mapped.maponly.sorted.bam ${sample}.mapped.maponly.bam
samtools index ${sample}.mapped.maponly.sorted.bam

# 质量过滤
samtools view -@ 20 -q 30 -b ${sample}.mapped.maponly.sorted.bam -o ${sample}.mapped.maponly.sorted.qF.bam
samtools flagstat ${sample}.mapped.maponly.sorted.qF.bam > ${sample}.mapped.maponly.sorted.qF.bam.qF.stats

# 最终排序
samtools sort -@ 20 -m 4G ${sample}.mapped.maponly.sorted.qF.bam -o ${sample}.mapped.maponly.sorted.qF.sorted.bam
samtools index ${sample}.mapped.maponly.sorted.qF.sorted.bam

# 去重处理
picard CleanSam \\
  INPUT=${sample}.mapped.maponly.sorted.qF.sorted.bam \\
  OUTPUT=${sample}.mapped.maponly.sorted.qF.sorted.cleaned.bam

picard MarkDuplicates \\
  INPUT=${sample}.mapped.maponly.sorted.qF.sorted.cleaned.bam \\
  OUTPUT=${sample}.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam \\
  REMOVE_DUPLICATES=TRUE \\
  AS=TRUE \\
  METRICS_FILE=${sample}.mapped.maponly.sorted.qF.sorted.cleaned.markdup.metrics \\
  VALIDATION_STRINGENCY=SILENT

samtools index ${sample}.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam
samtools flagstat ${sample}.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam > ${sample}.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.stats

# 质量评估
qualimap bamqc \\
  -bam ${sample}.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam \\
  -nt 20 \\
  -outformat HTML

# 损伤分析
mapDamage \\
  -i ${sample}.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam \\
  -r <REF_DIR>/VS1.final.fa \\
  -d ${sample}_damage

echo "[$(date)] 处理完成: ${sample}"
EOF

    # 添加执行权限
    chmod +x "${script_path}"
    echo "已生成脚本: ${script_path}"
done
