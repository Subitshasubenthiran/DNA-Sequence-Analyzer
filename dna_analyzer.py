def clean_sequence(seq):
    return seq.upper().replace(" ", "").replace("\n", "")


def read_fasta_file(filename):
    sequence = ""

    with open(filename, "r") as file:
        for line in file:
            if not line.startswith(">"):
                sequence += line.strip()

    return clean_sequence(sequence)


def validate_dna(seq):
    return all(base in ["A", "T", "G", "C"] for base in seq)


def count_bases(seq):
    return {
        "A": seq.count("A"),
        "T": seq.count("T"),
        "G": seq.count("G"),
        "C": seq.count("C")
    }


def gc_content(seq):
    return ((seq.count("G") + seq.count("C")) / len(seq)) * 100


def reverse_complement(seq):
    complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return "".join(complement[base] for base in seq[::-1])


def dna_to_rna(seq):
    return seq.replace("T", "U")


def analyze_sequence(dna):
    if len(dna) == 0:
        print("DNA sequence cannot be empty.")
        return

    if not validate_dna(dna):
        print("Invalid DNA sequence. Use only A, T, G, C.")
        return

    print("\nDNA Sequence Analysis")
    print("----------------------")
    print("DNA Sequence:", dna)
    print("Length:", len(dna))
    print("Base Count:", count_bases(dna))
    print("GC Content:", round(gc_content(dna), 2), "%")
    print("Reverse Complement:", reverse_complement(dna))
    print("RNA Sequence:", dna_to_rna(dna))


print("DNA Sequence Analyzer")
print("1. Enter DNA manually")
print("2. Read DNA from FASTA file")

choice = input("Choose option 1 or 2: ")

if choice == "1":
    dna = input("Enter DNA sequence: ")
    dna = clean_sequence(dna)
    analyze_sequence(dna)

elif choice == "2":
    filename = input("Enter FASTA filename: ")
    dna = read_fasta_file(filename)
    analyze_sequence(dna)

else:
    print("Invalid choice.")