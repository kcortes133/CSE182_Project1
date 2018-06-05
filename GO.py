'''
install goatools = easy_install goatools
fasta file with sequences = UP000006737.fasta
http://nbviewer.jupyter.org/urls/dessimozlab.github.io/go-handbook/GO%20Tutorial%20in%20Python%20-%20Solutions.ipynb
'''

'''
Import the OBO parser from GOATools
'''
from goatools import obo_parser

'''
To download the GO OBO file, we need the wget and os libraries.
'''
import wget
import os

def transitive_closure(go_term, go):
    go_term_set = set()
    find_parents(go_term, go, go_term_set)
    find_children(go_term, go, go_term_set)
    return go_term_set
    
def find_parents(term1, go, go_term_set={}, ret=False):
    for term2 in term1.parents:
        go_term_set.update({term2})
        
        # Recurse on term to find all parents
        find_parents(term2, go, go_term_set)          
    if(ret):
        return go_term_set

def find_children(term1, go, go_term_set={}, ret=False):
    for term2 in term1.children:
        go_term_set.update({term2})
        
        # Recurse on term to find all children
        find_children(term2, go, go_term_set)
    if(ret):
        return go_term_set

go_obo_url = 'http://purl.obolibrary.org/obo/go.obo'
data_folder = os.getcwd() + '/data'

'''Check if we have the ./data directory already'''
if(not os.path.isfile(data_folder)):
    '''Emulate mkdir -p (no error if folder exists)'''
    try:
        os.mkdir(data_folder)
    except OSError as e:
        if(e.errno != 17):
            raise e
else:
    raise Exception('Data path (' + data_folder + ') exists as a file. ')

'''Check if the file exists already'''
if(not os.path.isfile(data_folder+'/go.obo')):
    go_obo = wget.download(go_obo_url, data_folder+'/go.obo')
else:
    go_obo = data_folder+'/go.obo'

'''create a dictionary of the GO terms - using the obo_parser from GOATools'''
go = obo_parser.GODag(go_obo)

growth_count = 0
for go_term in go.values():
    if 'pterin' in go_term.name:
        growth_count += 1

print('Number of GO terms with "growth" in their name: {}'.format(growth_count))
