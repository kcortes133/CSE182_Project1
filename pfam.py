import requests
from xml.etree import ElementTree

"""
Test:
*  You can retrieve a sub-set of the data in a Pfam-A family page as an XML document using any of the following styles of URL:
* /family?output=xml&acc=PF02171
"""

acc_num = "PF02171"
basic = "https://pfam.xfam.org"
url = basic +'/protein?output=xml&acc=P00789'

response = requests.get(url, stream=True)
response.raw.decode_content = True

events = ElementTree.iterparse(response.raw)
for event, elem in events:
    print(elem.tag, elem.attrib)
    print(elem.text)


print("--------------------------------------------BLAST UNIPROT-------------------------------------")
# BLAST UNIPROT
"""
1 request/2 seconds
QUERY = Accession
PROGRAM = ?
DATABASE = ?
https://www.uniprot.org/help/api_retrieve_entries

uniprot
entry
keyword
.text



uniprot
entry
go_terms
category
term
go_id ="" 


1. Get id by searching embl-cds 
 - 
2. Run BLAST against UNIPROT on that id
 - https://www.uniprot.org/blast/uniprot/B2018060583C3DD8CE55183C76102DC5D3A26728B1D87CDE.xml


EBIApplicationResult
SequenceSimilaritySearchResult
hit
hit
descrtion

"""

# Getting the identifier
"""
import urllib,urllib2

url = 'http://www.uniprot.org/uploadlists/'

params = {
'from':'ACC',
'to':'P_REFSEQ_AC',
'format':'tab',
'query':'P13368 P20806 Q9UM73 P97793 Q17192'
}

data = urllib.urlencode(params)
request = urllib2.Request(url, data)
contact = "" # Please set a contact email address here to help us debug in case of problems (see https://www.uniprot.org/help/privacy).
request.add_header('User-Agent', 'Python %s' % contact)
response = urllib2.urlopen(request)
page = response.read(200000)
"""

basic_url = "https://www.uniprot.org/uniprot/"
uid = "P12345"
url = basic_url + uid + ".xml"


response = requests.get(url, stream=True)
response.raw.decode_content = True

events = ElementTree.iterparse(response.raw)
for event, elem in events:
    print(elem.tag, elem.attrib)
    print(elem.text)
