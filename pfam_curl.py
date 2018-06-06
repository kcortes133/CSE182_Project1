import os, subprocess, xmltodict, json, csv, time, ast

#return result['jobs']['job']['result_url']


def get_results(url):
    command = "curl -LH 'Expect:' 'https://pfam.xfam.org" + url 
    print("command : ", command)
    output = os.popen(command).read()
    result = json.dumps(xmltodict.parse(output))
    print(result)
    info = []
    temp_result = result['pfam']['results']['matches']['protein']['database']['match']
    info.append(temp_result['accession'])
    info.append(temp_result['type'])
    info.append(temp_result['class'])
    return info


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
with open("pfam_info", 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    for l in lines:
        if '>' in l:
            j+=1
            if j>1:
                r_url = search(temp)
                time.sleep(180)
                info = get_results(r_url)
                writer.writerow(info)
                print(info)
                temp = ""
        else:
            temp = temp + l


    
