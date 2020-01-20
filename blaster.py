#PHaDA: Blaster v1.0
#Daniel Carrillo Martin

import os
import re

from datetime import datetime
from subprocess import PIPE, Popen
from time import sleep

from Bio import SeqIO

def blastprocess(queryfasta,subjectfasta):
    """queryfasta: fasta file containing the query sequences for the blast.
       subjectfasta: fasta file containing the subject sequences for the blast.
       
       This function perform a blastp analysis and returns a dictionary containing
       the query ID as key and the subject IDs of its hits as values."""

    print("■ Blastp\n")
    for x in range(0,4):
        print("  ▪ Running blastp","."*x, end="\r")
        sleep(1)

    process = Popen(['blastp','-query',queryfasta,'-subject',subjectfasta,'-evalue',
                    '0.000001','-outfmt','6 qseqid sseqid'], 
                    stdout=PIPE, stderr=PIPE)              
    #error_encontrado = process.stderr.read()
    result = process.stdout.read()
    result = result.decode("utf-8")
    resultlisted = list(re.split("\t|\n",result))
    resultlisted = resultlisted[:-1]

    process.stderr.close()
    process.stdout.close()

    resultdict = {}
    for i in range(0,len(resultlisted),2):
        if resultlisted[i] in resultdict.keys():
            resultdict[resultlisted[i]].append(resultlisted[i + 1])
        else:
            resultdict[resultlisted[i]] = [resultlisted[i + 1]]

    return resultdict


def fastawriter(querydict,subjectdict,resultdict):
    """querydict: the query fasta file in a dictionary format,
                  keys are the sequences IDs.
       subjectdict: the subject fasta file in a dictionary format,
                    keys are the sequence IDs.
       resultdict: a query and its blast hits in a dictionary format.

       This function combines these dictionares to create a fasta file for each
       query beside its hits."""

    print("\n")
    for x in range(0,4):
        print("  ▪ Writing blastp hits to fasta","."*x, end="\r")
        sleep(0.5)

    for key in resultdict:
        outputfile = "%s_blastresult.fasta" % key
        os.mkdir("./Results/%s/" % key)
        output = open("./Results/%s/%s" % (key,outputfile),"w")
        output.write(querydict[key].format("fasta"))

        for i in resultdict[key]:
            output.write(subjectdict[i].format("fasta"))

        output.close()




            




    

 
    


    




