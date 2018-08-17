# Author: Eric Frankel

import pandas as pd
import subprocess


def run_rnn(training_path):
    mutations = pd.read_csv(training_path)
    missenses = mutations['Protein Consequence']

    for mutation in missenses:
        mut = mutation[2:]
        new_mut = parse_aa(mut[0:3]) + mut[3:-3] + parse_aa(mut[-3:])
        subprocess.call("./mutation.sh && run_mut() " + new_mut, shell=True) # TODO: add function call from the mutation script


def parse_aa(mutation):
    return {
        'Gly': 'G',
        'Ala': 'A',
        'Leu': 'L',
        'Val': 'V',
        'Ile': 'I',
        'Pro': 'P',
        'Arg': 'R',
        'Thr': 'T',
        'Ser': 'S',
        'Cys': 'C',
        'Met': 'M',
        'Lys': 'K',
        'Glu': 'E',
        'Gln': 'Q',
        'Asp': 'D',
        'Asn': 'N',
        'Trp': 'W',
        'Tyr': 'Y',
        'Phe': 'F',
        'His': 'H'
    }[mutation]