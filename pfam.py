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
