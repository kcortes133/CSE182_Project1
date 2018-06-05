'''
install goatools
easy_install goatools
'''

'''
fasta file with sequences
UP000006737.fasta
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

go_obo_url = 'http://www.geneontology.org/ontology/subsets/goslim_metagenomics.obo'
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
    raise Exception('Data path (' + data_folder + ') exists as a file. '
                   'Please rename, remove or change the desired location of the data path.')

'''Check if the file exists already'''
if(not os.path.isfile(data_folder+'/go-basic.obo')):
    go_obo = wget.download(go_obo_url, data_folder+'/go-basic.obo')
else:
    go_obo = data_folder+'/go-basic.obo'

print(go_obo)

'''create a dictionary of the GO terms - using the obo_parser from GOATools'''
go = obo_parser.GODag(go_obo)
