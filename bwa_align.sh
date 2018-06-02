#!/bin/sh

echo Creating index.....
bwa index -a bwtsw chr17.fa

echo
echo Alingment....
bwa aln chr17.fa reads_mutation.fastq > aln_sa.sai

echo
echo Generating sam file......
bwa samse chr17.fa aln_sa.sai reads_mutation.fastq > aln_se.sam

echo Generating sam.txt file......
samtools stats aln_se.sam  > aln_se.sam.txt

