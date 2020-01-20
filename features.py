#PHaDA: features v1.0
#Daniel Carrillo Martin

import os
import shutil

from datetime import datetime
from subprocess import Popen,PIPE,call
from time import sleep

from Bio import SeqIO

def directorer(filequery,filesubject):
    """filequery: query fasta file
       filesubject: subject fasta file

       This functions creates the main directories used for the
       script and make a copy of the fasta files into the 
       Data subdirectory."""

    dt = datetime.now()
    maindir = "PHaDA_"+dt.strftime("%Y-%m-%d_%H-%M-%S")

    os.mkdir(maindir)
    os.mkdir("%s/Data/" % maindir)
    os.mkdir("%s/Results/" % maindir)

    shutil.copy2(filequery, "./%s/Data/" % maindir)
    shutil.copy2(filesubject, "./%s/Data/" % maindir)

    os.chdir(maindir)

    print("Directory %s has been created!" % maindir)
    print("Results will be saved there.")
    sleep(3)


def isfasta(filename):
    """"filename: a file for creating a dictionary and testing.
    
    This function check if the file introduced is a fasta file 
    while creating a dictionary of the fasta file. Returns the dictionary,
    bul also True if filename is a fasta file. False if it is not."""

    with open(filename, "r") as handle:
        fastadict = SeqIO.to_dict(SeqIO.parse(handle, "fasta"))
        if fastadict:
            test = True
        else:
            test = False

    return test,fastadict

def installcheck(command):
    """command = a bash command to check.
    
    This function checks whether a bash package is installed or not.
    Returns True if it is installed. False, if it is not."""

    try:
        Popen([command,"-h"], stderr=PIPE, stdout=PIPE)        
        return True
    except:
        return False

def setup():
    
    for x in range(0,4):
        print("> Checking everything is okay","."*x, end="\r")
        sleep(0.5)


def header():

    call("clear",shell=True)
    print("\n   -------------------")
    print("\tPHaDA v1.0")
    print("   -------------------")
    print("> Daniel Carrillo, 2020 <\n")
