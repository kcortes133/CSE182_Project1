import os, subprocess, xmltodict, json, csv, time, ast

#return result['jobs']['job']['result_url']


def get_results(url):
    command = "curl -LH 'Expect:' 'https://pfam.xfam.org" + url +"'"
    print("command : ", command)
    output = os.popen(command).read()
    result = json.dumps(xmltodict.parse(output))
    info = {}
    temp_result = result['pfam']['results']['matches']['protein']['database']['match']
    info['accession'] = temp_result['@accession']
    info['type'] = temp_result['@type']
    info['class'] = temp_result['@class']
    return temp_result

def search(seq):
    with open("out.txt", 'w') as outf:
        outf.write(seq)
    command = "curl -LH 'Expect:' -F seq='<out.txt' -F output=xml 'http://pfam.xfam.org/search/sequence'"
    output = os.popen(command).read()
    result = json.dumps(xmltodict.parse(output))
    result_dict = ast.literal_eval(result)
    return result_dict['jobs']['job']['result_url']
   

with open('UP000006737.fasta', 'r') as inf:
    lines = inf.readlines()

cont = False
temp = ""
j = 0
with open("pfam_info", 'w') as outfile:
    for l in lines:
        if '>' in l:
            j+=1
            if j>1:
                r_url = search(temp)
                time.sleep(200)
                try:
                    info = get_results(r_url)
                    protien = {str(j) : info}
                    outfile.write(json.dumps(info))
                    print(info)
                except:
                    protien = {str(j): 'None'}
                temp = ""
        else:
            temp = temp + l
        if j > 120:
            break


    
