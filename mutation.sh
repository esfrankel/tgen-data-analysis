#!/usr/bin/env bash

function run_mut() {
    # Checking if mutant file exists; if not, create it
    if [ ! -f "./mutant_file.txt" ]; then
        touch ./mutant_file.txt;
    fi

    # Clearing mutant_file, then writing the mutation change from input to it
    > mutant_file.txt;
    echo $1 >> mutant_file.txt;

    # Checking if results file exists; if not, create it
    if [ ! -f "./results.txt" ]; then
        touch ./results.txt;
        #TODO: add in the part that adds the header to the results file
    fi

    # Checking if repaired_pdb exists IN CONTEXT OF DNM1; if not, throw error
    if [ ! -f "./

    # Execute foldx script portion
    ~/Desktop/foldx/foldx --command=BuildModel --pdb=3snh_Repair.pdb --mutant-file=mutant_file.txt --ionStrength=0.05 --pH=7 --water=CRYSTAL --vdwDesign=2 --pdbHydrogens=false --numberOfRuns=10
}