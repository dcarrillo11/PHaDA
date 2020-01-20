#PHaDa v1.0 | 20/01/2020
#Daniel Carrillo Martin

#Modules
import argparse
import csv 
import os
import shutil
import sys

from subprocess import call,PIPE, Popen
from datetime import datetime
from time import sleep

from Bio import SeqIO

import blaster
import features
import muscler
import prositer

features.header() #UserInterface
features.setup() #UserInterface

#Argparse: check arguments position and type
parser = argparse.ArgumentParser()
parser.add_argument("query",help="Protein fasta file for the query",type=argparse.FileType('r'))
parser.add_argument("subject",help="Protein fasta file for the subject",type=argparse.FileType('r'))
args = parser.parse_args()
if not args.query or not args.query: print(args)

filequery = sys.argv[1]
filesubject = sys.argv[2]

#Blast and Muscle install check
if not features.installcheck('blastp'):
    print("\n~ Blastp is not installed or unable to locate ~\n")
    if not features.installcheck('muscle'):
        print("~ Muscle is not installed or unable to locate ~\n")
    exit()
else:
    if not features.installcheck('muscle'):
        print("\n~ Muscle is not installed or unable to locate ~\n")
        exit()

#Fasta format file check
testQ,querydict = features.isfasta(filequery)
testS,subjectdict = features.isfasta(filesubject)

if not testQ:
    print("\n ~ Query file is not a fasta ~\n")
    if not testS:
        print(" ~ Subject file is not a fasta ~\n")
    exit()
else:
    if not testS:
        print("\n~ Subject file is not a fasta ~\n")
        exit()

features.header() #UserInterface

#Creates the needed directories
features.directorer(filequery,filesubject)

features.header() #UI

#BLASTp
blast_hits = blaster.blastprocess("./Data/"+os.path.basename(filequery),
                                  "./Data/"+os.path.basename(filesubject))

#Fasta blast result for each query
blaster.fastawriter(querydict,subjectdict,blast_hits)

#For each query and its hits
for key in blast_hits:
    features.header()
    print("■ %s homology analysis:\n" % key)
    sleep(0.2)

    #Sequences alignment
    inputfile = "./Results/%s/%s_blastresult.fasta" % (key,key)
    alignment = muscler.aligner(inputfile)

    #align_output = open("./Results/",key,"/",key,"_alignment.fasta","w")
    align_output = open("./Results/%s/%s_alignment.fasta" % (key,key),"w")
    align_output.write(alignment)
    align_output.close()
    print("▪ %s and homologous sequences aligned!\n" % key)
    sleep(0.2)

    #Phylogenetic tree
    alignfile = "./Results/%s/%s_alignment.fasta" % (key,key)
    tree = muscler.NJtree(alignfile)

    tree_output = open("./Results/%s/%s_tree.phy" % (key,key),"w")
    tree_output.write(tree)
    tree_output.close

    print("▪ NJ phylogenetc tree has been created!\n")

    #Domain search
    keydomains = prositer.domainsearch(inputfile)
    infodomains = prositer.domaininfo(keydomains)

    for i in range(0,len(infodomains)):
        with open ("./Results/%s/%s_domains.txt" %(key,infodomains[i][0][0]),"w",newline='') as domain_output:
            for j in range(0,len(infodomains[i])):
                list = infodomains[i][j]
                for item in list:
                    domain_output.write("%s\n" % item)
    
    print("▪ Domains for %s and its homologous have been found!\n" % key)

    wd = os.getcwd()
    wd = os.path.basename(wd)
    print("The alignment, tree.phy and domains can be found at: %s\n" % wd)
    sleep(0.5)


    


