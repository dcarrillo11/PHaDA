#PHaDA: Prositer v1.0
#Daniel Carrillo Martin

import re

from Bio.ExPASy import Prosite,Prodoc
from Bio import SeqIO


def domainsearch (filename):
    """filename: fasta file containing the protein sequences.

    This function extracts the domain patterns from PROSITE and 
    use them to search for this patterns in the protein sequences 
    of a fasta file. Returns a list with all the matches."""

    with open(filename, "r") as handle:
        fasta = list(SeqIO.parse(handle, "fasta"))
    
    repatterns = []
    propatterns = []
    initialre = [".","x","X","-","{","}","<",">","(",")"]
    finalre = ["",".",".","","[^","]","^","$","{","}"]
    handle = open("../prosite.dat","r")
    records = Prosite.parse(handle)
    for record in records:
        if record.pattern:
            pattern = record.pattern
            for i in range(0,len(initialre)):
                pattern = pattern.replace(initialre[i],finalre[i])
            repatterns.append(pattern)
            propatterns.append(record.pattern)
        else:
            continue
    
    results = []
    for j in range(0,len(fasta)):
        protresults = []
        for k in range(0,len(repatterns)):
            matches = re.finditer(r"" + repatterns[k],str(fasta[j].seq))
            for m in matches:
                pattresults = []
                pattresults.append(fasta[j].id)
                pattresults.append(m.group())
                pattresults.append(m.start())
                pattresults.append(m.end())
                pattresults.append(propatterns[k])
                if pattresults:
                    protresults.append(pattresults)
    
        results.append(protresults)

    return results

def domaininfo(keydomains):
    """keydomains: a list of the PROSITE domain matches.

    This function takes the matches domains founded and extend
    the information about them."""

    handle = open("../prosite.dat","r")
    recordsdat = Prosite.parse(handle)

    for record in recordsdat:
        for i in range(0,len(keydomains)):
            for j in range(0,len(keydomains[i])):
                if record.pattern == keydomains[i][j][-1]:
                    keydomains[i][j].append(record.accession)
                    keydomains[i][j].append(record.name)
                    keydomains[i][j].append(record.description)
                    handle = open("../prosite.doc")
                    recordsdoc = Prodoc.parse(handle)
                    for info in recordsdoc:
                        if str(keydomains[i][j][5]) in str(info.prosite_refs):
                            keydomains[i][j].append(info.text)
    
    return keydomains

        

