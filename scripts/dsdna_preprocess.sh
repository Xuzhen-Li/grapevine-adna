#!/bin/bash
#SBATCH --job-name=pre
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=40
#SBATCH -p <PARTITION>
#SBATCH -o pre.out
#SBATCH -e pre.err
FLIES=`ls *_R1.fastq.gz | sed 's/_R1.fastq.gz//g'`
for F in $FLIES;
do
AdapterRemoval --file1 ${F}_R1.fastq.gz --file2 ${F}_R2.fastq.gz --qualitybase 33 --qualitybase-output 33 --trimqualities --minquality 2 --trimns --minlength 30 --basename ${F} --collapse --gzip --threads 35
bwa aln -l 1000 -n 0.01 -f ${F}.collapsed.sai -t 35 <REF_DIR>/VS1.final.fa ${F}.collapsed.gz
bwa samse -r @RG\\tID:${F}\\tSM:${F} -f ${F}.collapsed.sam <REF_DIR>/VS1.final.fa ${F}.collapsed.sai ${F}.collapsed.gz
samtools view -@ 35 -Sb -o ${F}.mapped.bam ${F}.collapsed.sam
samtools flagstat -@ 35 ${F}.mapped.bam > ${F}.mapped.stats
samtools view -@ 35 -F4 -b ${F}.mapped.bam -o ${F}.mapped.maponly.bam
samtools sort -@ 35 -m 2G -o ${F}.mapped.maponly.sorted.bam ${F}.mapped.maponly.bam
samtools index ${F}.mapped.maponly.sorted.bam
samtools view -@ 35 -q 30 -b ${F}.mapped.maponly.sorted.bam -o ${F}.mapped.maponly.sorted.qF.bam
samtools flagstat ${F}.mapped.maponly.sorted.qF.bam  > ${F}.mapped.maponly.sorted.qF.bam.qF.stats
samtools sort -@ 35 -m 2G -o ${F}.mapped.maponly.sorted.qF.sorted.bam ${F}.mapped.maponly.sorted.qF.bam
picard CleanSam INPUT=${F}.mapped.maponly.sorted.qF.sorted.bam OUTPUT=${F}.mapped.maponly.sorted.qF.sorted.cleaned.bam
picard MarkDuplicates INPUT=${F}.mapped.maponly.sorted.qF.sorted.cleaned.bam OUTPUT=${F}.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam REMOVE_DUPLICATES=TRUE AS=TRUE METRICS_FILE=${F}.mapped.maponly.sorted.qF.sorted.cleaned.markdup.metrics VALIDATION_STRINGENCY=SILENT 
samtools index ${F}.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam
samtools flagstat ${F}.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam  > ${F}.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.stats
qualimap bamqc -bam ${F}.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam -nt 35 -outformat HTML
mapDamage -i ${F}.mapped.maponly.sorted.qF.sorted.cleaned.rmdup.MarkD.bam -r <REF_DIR>/VS1.final.fa -d ${F}_damage
done
