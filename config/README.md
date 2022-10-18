# General settings

To configure this workflow, modify `config/config.yaml` according to your needs, following the explanations provided in the file

## Sample sheet
* Add samples to `config/samples.tsv`. For each sample, the column `sample` has to be defined. 
* Add the full path of the CRAM file that we received for the sample in `cram_location`.

## Sample pedigree
* Add samples to `config/samples.ped`. For each sample, add the columns in the PED format as specified here: https://gatk.broadinstitute.org/hc/en-us/articles/360035531972-PED-Pedigree-format

## HPO terms
* Add the HPO terms for the proband, one on each line to `config/hpo.txt`.

