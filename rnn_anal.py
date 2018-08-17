# Author: Eric Frankel

import pandas as pd


def run_rnn(training_path):
   mutations = pd.read_csv(training_path)
   missenses = mutations['Protein Consequence']
   new_muts = []

   for mutation in missenses:
       mut = mutation[2:]
       new_mut = parse_aa(mut[0:3]) + mut[3:-3] + parse_aa(mut[-3:])
       new_muts.append(new_mut)

   mutations['Formatted Mutations'] = new_muts


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