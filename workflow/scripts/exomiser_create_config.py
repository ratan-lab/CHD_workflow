import yaml
import sys

if __name__ == "__main__":
    ref_file = sys.argv[1]
    vcf_file = sys.argv[2]
    input_vcfi = sys.argv[3]
    ped_file = sys.argv[4]
    hpo_file = sys.argv[5]

    prioritiser = sys.argv[6]
    prioritiser_params = sys.argv[7]
    priority = sys.argv[8]

    output = sys.argv[9]


with open(hpo_file) as f: hpo = f.read().splitlines()

if ref_file.endswith("human_g1k_v37_decoy.fasta"):
    ref = "hg19"
elif ref_file.endswith("hs38DH.fa"):
    ref = "hg38"
else:
    print("unknown reference input to exomiser", file=sys.stderr)
    exit(1)

proband = None
with open(ped_file, 'r') as f:
    for line in f:
        tokens = line.strip().split('\t')
        if tokens[5] == '2':
            proband = tokens[1]
            break
assert proband is not None



initial_string = f"analysis:\n    genomeAssembly: {ref}\n    vcf: {vcf_file}\n    ped: {ped_file}\n    proband: {proband}\n    hpoIds: {hpo}\n"

constant_string1 = "    inheritanceModes: {\n            AUTOSOMAL_DOMINANT: 0.1,\n            AUTOSOMAL_RECESSIVE_HOM_ALT: 0.1,\n            AUTOSOMAL_RECESSIVE_COMP_HET: 2.0,\n            X_DOMINANT: 0.1,\n            X_RECESSIVE_HOM_ALT: 0.1,\n            X_RECESSIVE_COMP_HET: 2.0,\n            MITOCHONDRIAL: 0.2\n    }\n    analysisMode: PASS_ONLY\n    frequencySources: [\n        THOUSAND_GENOMES,\n        TOPMED,\n        UK10K,\n        ESP_AFRICAN_AMERICAN, ESP_EUROPEAN_AMERICAN, ESP_ALL,\n        EXAC_AFRICAN_INC_AFRICAN_AMERICAN, EXAC_AMERICAN,\n        EXAC_SOUTH_ASIAN, EXAC_EAST_ASIAN,\n        EXAC_FINNISH, EXAC_NON_FINNISH_EUROPEAN,\n        EXAC_OTHER,\n        GNOMAD_E_AFR,\n        GNOMAD_E_AMR,\n        GNOMAD_E_ASJ,\n        GNOMAD_E_EAS,\n        GNOMAD_E_FIN,\n        GNOMAD_E_NFE,\n        GNOMAD_E_OTH,\n        GNOMAD_E_SAS,\n        GNOMAD_G_AFR,\n        GNOMAD_G_AMR,\n        GNOMAD_G_ASJ,\n        GNOMAD_G_EAS,\n        GNOMAD_G_FIN,\n        GNOMAD_G_NFE,\n        GNOMAD_G_OTH,\n        GNOMAD_G_SAS\n        ]\n    pathogenicitySources: [REVEL, MVP, CADD]\n    steps: [\n        failedVariantFilter: {},\n        variantEffectFilter: {\n            remove: [\n                FIVE_PRIME_UTR_EXON_VARIANT,\n                FIVE_PRIME_UTR_INTRON_VARIANT,\n                THREE_PRIME_UTR_EXON_VARIANT,\n                THREE_PRIME_UTR_INTRON_VARIANT,\n                NON_CODING_TRANSCRIPT_EXON_VARIANT,\n                UPSTREAM_GENE_VARIANT,\n                INTERGENIC_VARIANT,\n                REGULATORY_REGION_VARIANT,\n                CODING_TRANSCRIPT_INTRON_VARIANT,\n                NON_CODING_TRANSCRIPT_INTRON_VARIANT,\n                DOWNSTREAM_GENE_VARIANT\n            ]\n        },\n        frequencyFilter: {maxFrequency: 2.0},\n        pathogenicityFilter: {keepNonPathogenic: true},\n        inheritanceFilter: {},\n        omimPrioritiser: {},\n"

priority_string1 = f"        {prioritiser}: { {prioritiser_params} },\n"
constant_string2 = "        priorityScoreFilter: {priorityType: "
priority_string2 = f"{priority}"
constant_string3 = ", minPriorityScore: 0.501}\n        ]\noutputOptions:\n    outputContributingVariantsOnly: true\n    numGenes: 10\n    outputPrefix:"
priority_string3 = f" exomiser/{prioritiser}"
constant_string4 = "\n    outputFormats: [HTML, JSON, TSV_GENE, TSV_VARIANT, VCF]"

with open(output[0], 'w') as f:
    print(initial_string + constant_string1 + priority_string1.replace('\'', '') + constant_string2 + priority_string2 + constant_string3 + priority_string3 + constant_string4, file=f)
