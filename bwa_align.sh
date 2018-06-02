#!/bin/sh

echo Creating index BWA.....
bwa index chr17.fa

echo
echo Alingment....
bwa aln chr17.fa reads_mutation.fastq > aln_sa.sai

echo
echo Generating sam file......
bwa samse chr17.fa aln_sa.sai reads_mutation.fastq > aln_se.sam

echo Generating sam.txt file......
samtools stats aln_se.sam  > aln_se.stats

echo Creating index SAMtools.....
samtools faidx chr17.fa

echo converting SAM to BAM 
samtools import chr17.fa.fai aln_se.sam aln_se.bam

echo Sorting BAM file 
samtools sort aln_se.bam > aln_se.sorted

echo Indexing BAM file 
samtools index aln_se.sorted > aln_se.sorted.bam

