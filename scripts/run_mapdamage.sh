#!/bin/bash
# 来源：mapDamage 输出目录中的 Runtime_log.txt 记录的原始命令（2023-12-21），已去掉主机路径和样本名
mapDamage -i <SAMPLE>.mapped.maponly.sorted.qF.sorted.bam -r <REF_DIR>/VS1.final.fa
