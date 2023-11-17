#This program is used for calculating the number of GFP individuals sequenced by SMRT in each replicate population and in each generation
import os
import csv
import sys
import re


PATH='~'
csvpath='~.csv'

#ref indicates GFP (ancestor) cDNA sequence

ref="ATGATGAGCAAGGGCGAGGAGCTGTTCACCGGGGTGGTGCCCATCCTGGTCGAGCTGGACGGCGACGTAAACGGCCACAAGTTCAGCGTGTCCGGCGAGGGCGAGGGCGATGCCACCTACGGCAAGCTGACCCTGAAGTTCATCTGCACCACCGGCAAGCTGCCCGTGCCCTGGCCCACCCTCGTGACCACCTTCAGCTACGGCCTGCAATGCTGCGCCCGCTACCCCGACCACATGAAGCTGCACGACTTCTTCAAGTCCGCCATGCCCGAAGGCTACGTCCAGGAGCGCACCATCTTCTTCAAGGACGACGGCAACTACAAGACCCGCGCCGAGGTGAAGTTCGAGGGCGACACCCTGGTGAACCGCATCGAGCTGAAGGGCATCGACTTCAAGGAGGACGGCAACATCCTGGGGCACAAGCTGGAGTACAACTACAACAGCCACAACGTCTATATCATGGCCGACAAGCAGAAGAACGGCATCAAGGTGAACTTCAAGATCCGCCACAACATCGAGGACGGCAGCGTGCAGCTCGCCGACCACTACCAGCAGAACACCCCCATCGGCGACGGCCCCGTGCTGCTGCCCGACAACCACTACCTGAGCTGCCAGTCCGCCCTGAGCAAAGACCCCAACGAGAAGCGCGATCACATGGTCCTGCTGGAGTTCGTGACCGCCGCCGGGATCACTCTCGGCATGGACGAGCTGTACAAGTGA"

#the following codes are used for grouping sequences from each replicate population in every generation 
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



def Numseq_each(filepath):
	FileName = os.path.split(filepath)[1] 
	Name=FileName.split('_')[1:4]
	Seqlist_each=Seq_List(filepath)
	Numseq_each=Name+[len(Seqlist_each)]
	return Numseq_each

#the following codes are used for reading all input files (in the folder "~/fasta") which contain cDNA sequences of each evolving population sequenced by SMRT sequencing
def eachFile(filepath):
	os.chdir(filepath)
	pathDir = os.listdir(filepath)      
	for s in pathDir:
		newDir=os.path.join(filepath,s)     
		if os.path.isfile(newDir) :         
			if os.path.splitext(newDir)[1]==".fasta":  
				Num_each=Numseq_each(newDir) 
				Num_all.append(Num_each)                    

Num_all=[]
eachFile(PATH)

#print (Num_all)
#the following codes are used for writing the result into a csv file
with open(csvpath, 'w') as csvfile:
	Wri = csv.writer(csvfile)
	Wri.writerow(['Generation','Population','Replicate','Number of Sequences'])
	for each in Num_all:
			Wri.writerow(each)
