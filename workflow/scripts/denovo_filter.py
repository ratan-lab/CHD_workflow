import sys

if __name__ == "__main__":
    input_vcf = sys.argv[1]
    input_ped = sys.argv[2]
    output_vcf = sys.argv[3]


proband = None
mother = None
father = None


with open(input_ped, 'r') as f:
    for line in f:
        tokens = line.strip().split('\t')
        if tokens[5] == '2':
            proband = tokens[1]
        else:
            if tokens[4] == '1':
                father = tokens[1]
            elif tokens[4] == '2':
                mother = tokens[1]

assert proband is not None
assert mother is not None
assert father is not None

probandi = None
motheri = None
fatheri = None

with open(input_vcf, 'r') as f:
    for line in f:
        if line.startswith("#CHROM"):
            tokens = line.strip().split("\t")
            probandi = tokens.index(proband)
            motheri = tokens.index(mother)
            fatheri = tokens.index(father)
            break

assert probandi is not None
assert motheri is not None
assert fatheri is not None

with open(input_vcf, 'r') as f, open(output_vcf, 'w') as g:
    for line in f:
        if line.startswith("#"):
            print(line.strip(), file=g)
        else:
            tokens = line.strip().split("\t")
            assert tokens[8].split(":")[0] == "GT"
            proband_gt = tokens[probandi].split(":")[0]
            mother_gt = tokens[motheri].split(":")[0]
            father_gt = tokens[fatheri].split(":")[0]
            hom_ref = [f"{tokens[3]}/{tokens[3]}", f"{tokens[3]}"]
            het = [f"{tokens[3]}/{tokens[4]}", f"{tokens[4]}"]
            if tokens[6] == "PASS" and \
                father_gt in hom_ref and \
                mother_gt in hom_ref and \
                proband_gt in het:
                print(line.strip(), file=g)
