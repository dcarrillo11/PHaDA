![logo](/picturename.jpg)

# PHaDA: Protein Homology and Domain Analysis

Release 1.0 | Created by: Daniel Carrillo Martín

## What's PHaDA?

PHaDA is a bash bioinformatic tool for protein homology and domain analysis. What does this mean? Homology analysis includes the performing of a **blastp**, a multiple alignment of each query and its blastp hits sequences with **Muscle** and a neighbor-joining phylogenetic tree from the previous alignment (Also with **Muscle**). The domain analysis part carries out a PROSITE's domains pattern search in the sequences of each query and its blastp hits. It shows the recognised domains and some information about them in each protein. 

## Requirements

- Python 3.x

- [BioPython](https://biopython.org/)

- [Blastp](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download)

- [Muscle](https://www.drive5.com/muscle/)

## Usage 

PHaDA is structured in packages. There are multiple packages for each part of the analysis like `blaster.py`,`muscler.py`,etc. For running PHaDA, it is necessary that all packages are in the same folder or directory. The PROSITE files: `Prosite.dat` and `Prosite.doc` also need to be in that folder (You can download them [here](ftp://ftp.expasy.org/databases/prosite)). The code for running PHaDA is:

`python3 main.py query.fasta subject.fasta`

`main.py` takes two arguments: the query fasta file and the subject fasta file. Both arguments are mandatory.

PHaDA creates its own directory for each run at the actual working directory. 

## Output

PHaDA creates a `Results/` directory for each run. This directory contains another directory for each query from the query.fasta that got at least one hit in **blastp**. These query-named directories, in turn, contain the following files:

- Blastresult_QUERY.fasta : fasta file for the query and blast hits sequences.
- QUERY_alignment.fasta : query and blast hits sequences alignment in fasta format.
- QUERY_tree.phy : NeighborJoining tree of the query and blast hits in Newick format.
- QUERY_domains.csv : Domains recognised in the query protein.
- SUBJECTX_domains.csv : Domains recognised in the subject protein X.
