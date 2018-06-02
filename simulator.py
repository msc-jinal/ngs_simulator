import Bio.SeqIO as SeqIO
from random import random,randint,choice
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq



readsize=50
totalreads=100000
errfreq = 0.00
tot_err_base=int(totalreads * errfreq)         
gseq=[]

#simulating random reads

def simulate_reads():
    genebankFile = SeqIO.read("chr17.fa","fasta")
    refseqlen = (len(genebankFile.seq))    
    for i in range(0,totalreads):
        start = randint(0,refseqlen-readsize)
        end = start+readsize
        subSeq = genebankFile.seq[start:end]
        seqRead = SeqRecord(subSeq,'Sequence_%i' % (i+1),description='')
        seqRead.letter_annotations["phred_quality"]=[5]*len(subSeq) # Adding dummy quality score as &
        gseq.append(seqRead)
    
   


#adding mutation/errors in original reads
def add_mutation():        
    for i in range(tot_err_base):
        i_seq = randint(0,totalreads-1) ## Finding random sequence object from list
        seqRecord = gseq[i_seq];
        strSeq=replaceBase(str(seqRecord.seq))
        seqRecord.seq=Seq(strSeq)
  
  
#this function will replace random single base  
def replaceBase(seq):
    seq = list(seq) # string to list
    while 1==1:
        ch = choice("ACGT")
        position=randint(0,49)
        if seq[position].upper()!=ch:
            seq[position]=ch
            break
    
    seq=''.join(seq) # list to string       
    return seq
        


def main():
    simulate_reads();
    #writing original reads in fastq file    
    SeqIO.write(gseq, "reads.fastq", "fastq")
    
    add_mutation();
    #writing mutated reads in fastq file    
    SeqIO.write(gseq, "reads_mutation.fastq", "fastq")


    
main()
    
    

