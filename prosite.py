# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 00:32:43 2018

@author: Jonathan
"""

from Bio.ExPASy import ScanProsite
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

sequences = []

with open("100seq.fasta", "r") as infile:
    sequence = ""
    for line in infile.readlines():
        line = line.strip()
        if line.startswith(">"):
            sequences.append(sequence)
            sequence = ""
            continue
        sequence = sequence + line
    sequences.append(sequence)
    del sequences[0]
    
    
    
        
    


with open("biop.output", "w") as outfile:
    
    for sequence in sequences:
        
        print "starting PROSITE"

        handle = ScanProsite.scan(seq=sequence)

        result = ScanProsite.read(handle)
        signature_ac = "NA"
        sequence_ac = "NA"
        if len(result) > 0:
            tophit = result[0]
            signature_ac = tophit["signature_ac"]
            sequence_ac = tophit["sequence_ac"]
        
        print "starting BLAST"
        
        result_handle = NCBIWWW.qblast("blastp","nr", sequence)
        
        blast_record = NCBIXML.read(result_handle)
        gi = "NA"
        ref = "NA"
        anno = "NA"
        if len(blast_record.alignments) > 0:
            title = str(blast_record.alignments[0].title)
            gititle, gi, reftitle, ref, anno = title.split(">")[0].split("|")
        
            
        outfile.write(signature_ac + "\t" + sequence_ac + "\t" + gi + "\t" + ref + "\t" + anno + "\n")
        outfile.flush()


