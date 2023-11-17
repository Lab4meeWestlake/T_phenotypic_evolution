#This program is used for calculating the mean number of SNPs per GFP molecule sequenced by SMRT in each replicate population and in each generation
import os
import csv
import sys
import re


PATH='~'
csvpath='~.csv'

#ref indicates GFP (ancestor) cDNA sequence

ref="ATGATGAGCAAGGGCGAGGAGCTGTTCACCGGGGTGGTGCCCATCCTGGTCGAGCTGGACGGCGACGTAAACGGCCACAAGTTCAGCGTGTCCGGCGAGGGCGAGGGCGATGCCACCTACGGCAAGCTGACCCTGAAGTTCATCTGCACCACCGGCAAGCTGCCCGTGCCCTGGCCCACCCTCGTGACCACCTTCAGCTACGGCCTGCAATGCTGCGCCCGCTACCCCGACCACATGAAGCTGCACGACTTCTTCAAGTCCGCCATGCCCGAAGGCTACGTCCAGGAGCGCACCATCTTCTTCAAGGACGACGGCAACTACAAGACCCGCGCCGAGGTGAAGTTCGAGGGCGACACCCTGGTGAACCGCATCGAGCTGAAGGGCATCGACTTCAAGGAGGACGGCAACATCCTGGGGCACAAGCTGGAGTACAACTACAACAGCCACAACGTCTATATCATGGCCGACAAGCAGAAGAACGGCATCAAGGTGAACTTCAAGATCCGCCACAACATCGAGGACGGCAGCGTGCAGCTCGCCGACCACTACCAGCAGAACACCCCCATCGGCGACGGCCCCGTGCTGCTGCCCGACAACCACTACCTGAGCTGCCAGTCCGCCCTGAGCAAAGACCCCAACGAGAAGCGCGATCACATGGTCCTGCTGGAGTTCGTGACCGCCGCCGGGATCACTCTCGGCATGGACGAGCTGTACAAGTGA"



#the following codes are used for grouping sequences from replicate population in a generation 
def Seq_List(filepath):
	f1 = open(filepath, "r")
	SNPlines = f1.readlines()
	Seqlist=[]
	for line in SNPlines:
		if not line.strip(): continue
		if re.search(">",line):
			seqName=line
		else:
			Seqlist.append(line.strip())
	return Seqlist

#the following codes are used for getting the mean number of SNPs per GFP molecule in each replicate population and in each generation 
def SNP(seqlist):
	numSeq=len(seqlist)
	if numSeq>0:
		diff=0
		for seq in seqlist:
			for i in range (len(ref)):
				if seq[i]!=ref[i]:
					diff+=1
		snpNum='%.4f'%(float(diff)/numSeq)
	else:  
		snpNum=''

	return snpNum


def SNPEach(filepath):
	FileName = os.path.split(filepath)[1] 
	Name=FileName.split('_')[1:4]
	Seqlist_each=Seq_List(filepath)
	SNP_each=Name+[SNP(Seqlist_each)]
	return SNP_each


#the following codes are used for reading all input files (in the folder "~/fasta") which contain cDNA sequences of each evolving population sequenced by SMRT sequencing
def eachFile(filepath):
	os.chdir(filepath)
	pathDir = os.listdir(filepath)      
	for s in pathDir:
		newDir=os.path.join(filepath,s)     
		if os.path.isfile(newDir) :         
			if os.path.splitext(newDir)[1]==".fasta":  
				SNP_each=SNPEach(newDir)                     
				SNP_all.append(SNP_each) 
SNP_all=[]
eachFile(PATH)
#print SNP_all

#the following codes are used for writing the result into a csv file
with open(csvpath, 'w') as csvfile:
	Wri = csv.writer(csvfile)
	Wri.writerow(['Generation','Population','Replicate','SNP'])
	for each in SNP_all:
			Wri.writerow(each)
