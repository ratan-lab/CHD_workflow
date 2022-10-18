This workflow takes as input exome CRAM files from a trio, realigns the reads to a new reference using `bwa mem`, marks duplicates using `SAMblaster`. It then calls variants using `FreeBayes` and annotates the variants using `VEP`. In combination with pedigree information and HPO terms, it then runs `Exomiser` to rank the variants based on their probability to cause the disease. 

This workflow is not ready for public consumption.
