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

    # Checking if repaired_pdb exists IN CONTEXT OF DNM1; if not, terminate
    if [ ! -f "./3snh_Repair.pdb" ]; then
        echo "No repaired PDB file found; terminating";
        return;
    fi

    # Execute foldx script portion
    ~/Desktop/foldx/foldx --command=BuildModel --pdb=3snh_Repair.pdb --mutant-file=mutant_file.txt --ionStrength=0.05 --pH=7 --water=CRYSTAL --vdwDesign=2 --pdbHydrogens=false --numberOfRuns=10;

    # Handle all files that get generated, removing the useless ones
    rm WT*;
    rm 3snh_Repair_*;
    rm PdbList*;
    rm Dif_3snh*;
    mv Average_3snh_Repair.fxout Average_3snh_Repair.txt

    # Defining constants for future operations
    TAB=$'\t'
    NLINE=$'\n'

    # Adds temporary text file; parses through the text file to add additional column
    # TODO: This process feels clunky af but I don't want to mess with it. Play around and check if it can be more efficient. Like could we just do it in a dataframe and leave as is?
    cp Average_3snh_Repair.txt temp.txt
    sed -i".bak" '1,9d' temp.txt
	sed -e '$s/$/'"${TAB}"''"$1"'/' temp.txt >> temp.txt
	sed -i".bak" '1d' temp.txt
	for line in temp.txt
	do
		echo -e '\n'
		cat $line
	done >> results.txt
	> temp.txt
	rm Average_3snh_Repair.txt
}