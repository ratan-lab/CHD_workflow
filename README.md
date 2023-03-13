This workflow takes as input exome CRAM files from a trio, realigns the reads to a new reference using `bwa mem`, marks duplicates using `SAMblaster`. It then calls variants using `FreeBayes` and annotates the variants using `VEP`. In combination with pedigree information and HPO terms, it then runs `Exomiser` to rank the variants based on their probability to cause the disease. 

## Running the workflow

In order to use this workflow, first clone this repository. Then 'cd CHD_workflow'. Fill in the details in the 'config/config.yaml' file. Then run

'''
snakemake --cores 1 --configfile config/config.yaml -d . --use-conda
'''

if you are running locally using a single core.

### Points to remember

1. The first rule converts the sequences in the CRAM to a fastq file. You need to set REF_PATH and REF_CACHE for the sequences that are used in the input CRAMs. Follow the steps outline [here](https://www.htslib.org/workflow/cram.html) to ensure that these are set correctly.

2. The second rule aligns the sequences to a new reference using BWA mem. Please ensure that all files needed by BWA are available. The files are assumed to be present with the reference fasta file that is included in the config.yaml file.

3. The mdust file should be tabix indexed.

4. The reference file you want to use for alignment should have a .dict file. Please see http://gatkforums.broadinstitute.org/discussion/1601/how-can-i-prepare-a-fasta-file-to-use-as-reference for help creating it.


This workflow is not ready for public consumption.
