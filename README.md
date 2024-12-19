# egfr-competition

This repository contains the files required for fine-tuning Raygun and running LocalColabFold for the EGFR binder competition. No scripts are used for ProTrek filtering--sequences are manually inputted into http://search-protrek.com/.

## `raygun-files`
This directory can be placed into the `example-configs` directory within the original Raygun repository (https://github.com/rohitsinghlab/raygun)

After installing the necessary requirements, Raygun can then be fine-tuned on the EGFR endogenous ligands as templates using 
```
raygun-sample --config 'example-configs/egf/generate-sample-egf-v2.yaml'
```
## `af2-files`
We provide an example of an input fasta file. The input sequence is formatted as {binder seq}:{egfr seq}

Installation of LocalColabFold (https://github.com/YoshitakaMo/localcolabfold) is required.

To run LocalColabFold, use 
```
colabfold_batch input.fasta output_dir --num-recycle 3 --num-seeds 3 --num-models 5 --templates
```
## `scripts`
This directory contains three scripts for calculating the edit distance from wildtype EGF, calculating ESM2 650M pseudo log-likelihood (PLL), and calculating iPTM and iPAE from AF2 output files. Scripts for PLL and AF2 metric calculations are from https://github.com/adaptyvbio/competition_metrics
