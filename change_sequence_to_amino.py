genetic_code = {
    "TTT": "F", "TTC": "F",  # Phenylalanine
    "TTA": "L", "TTG": "L",  # Leucine
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",  # Leucine
    "ATT": "I", "ATC": "I", "ATA": "I",  # Isoleucine
    "ATG": "M",  # Methionine (Start)
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",  # Valine
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",  # Serine
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",  # Proline
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",  # Threonine
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",  # Alanine
    "TAT": "Y", "TAC": "Y",  # Tyrosine
    "TAA": "*", "TAG": "*", "TGA": "*",  # Stop codons
    "CAT": "H", "CAC": "H",  # Histidine
    "CAA": "Q", "CAG": "Q",  # Glutamine
    "AAT": "N", "AAC": "N",  # Asparagine
    "AAA": "K", "AAG": "K",  # Lysine
    "GAT": "D", "GAC": "D",  # Aspartic acid
    "GAA": "E", "GAG": "E",  # Glutamic acid
    "TGT": "C", "TGC": "C",  # Cysteine
    "TGG": "W",  # Tryptophan
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",  # Arginine
    "AGT": "S", "AGC": "S",  # Serine
    "AGA": "R", "AGG": "R",  # Arginine
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"   # Glycine
}

def read_fasta(path_to_fasta:str) -> str:
    with open(path_to_fasta, 'r') as f:
        FASTA = f.readlines()
        FASTA.pop(0)
        fasta = ''.join(FASTA)
    return fasta

fasta = read_fasta('sequence.txt')
print(fasta)