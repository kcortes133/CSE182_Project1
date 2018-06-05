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

'''create a dictionary of accession numbers and go terms queried from prosite/pfam/uniprot'''
accgoid = {}

'''create a dictionary of go id and go term names'''
goid = {}

'''temp file name is querygo.txt'''
with open("querygo.txt") as f:
    for line in f:
        (key, val) = line.split()
        accgoid[key] = val
        '''for each go id search the GO db'''
        for val in go.values():
            goid[val] = go_term.name
            
print(accgoid)
print(goid)
