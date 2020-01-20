#PHaDA: Muscler v1.0
#Daniel Carrillo Martin

from subprocess import PIPE, Popen

def aligner(queryfasta):
    """queryfasta: multifasta file.

    This function align the sequences in a multifasta file using
    the Muscle package"""

    process = Popen(['muscle','-in',queryfasta], 
                    stdout=PIPE, stderr=PIPE)
    alignment = process.stdout.read()
    alignment = alignment.decode("utf-8")

    process.stdout.close()

    return alignment
    
def NJtree(align_fasta):
    """queryfasta: aligned multifasta file by Muscle.

    This function creates a NeighborJoining phylogenetic tree
    using the Muscle package."""

    process = Popen(['muscle','-maketree','-in',align_fasta,'-cluster',
                    'neighborjoining'], stdout=PIPE, stderr=PIPE)
    treenewick = process.stdout.read()
    treenewick = treenewick.decode("utf-8")

    process.stdout.close()

    return treenewick



