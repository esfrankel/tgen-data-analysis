# Author: Eric Frankel

import pandas as pd
import subprocess


def create_results_file(missense_path):
    mutations = pd.read_csv(missense_path)
    missenses = mutations['Protein Consequence']

    for mutation in missenses:
        mut = mutation[2:]
        new_mut = parse_aa(mut[0:3]) + mut[3:-3] + parse_aa(mut[-3:])
        subprocess.call("./mutation.sh && run_mut() " + new_mut, shell=True) # TODO: add function call from the mutation script
    return "Finished creating results file"


def combine_mut_dataframes(missense_path, results_path="./results.txt"):
    mutations = pd.read_csv(missense_path)
    results = pd.read_csv(results_path)
    mutations


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
