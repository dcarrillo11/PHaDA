![logo](/picturename.jpg)

# PHaDA: Protein Homology and Domain Analisys

Release 1.0 | Created by: Daniel Carrillo Martín

## What's PHaDA?

PHaDA is a bash bioinformatic tool for protein homology
and domain analisys. What does this mean? Homology analisys
include 


## Requirements

- Python 3.x

- [BioPython](https://biopython.org/)

- [Blastp](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download)

- [Muscle](https://www.drive5.com/muscle/)

## Usage 

PHaDA is 

`python main.py query.fasta subject.fasta`

## Output

PHaDA creates a **Results/** directory for each execution.
RESULTS CONTIENE OTRO DIRECTORIO QUE AUNA TODOS LOS RESULTADOS PARA CADA *QUERY* 
QUE HA OBTENIDO AL MENOS UN *HIT* EN EL BLASTP. CADA UNO DE ESTOS DIRECTORIOSM ASU VEZ
CONTIENE:
- Blastresult_QUERY.fasta : 
- QUERY_alignment.fasta :
- QUERY_tree.phy :
- QUERY_domains.tsv :
- SUBJECT_domains.tsv :
