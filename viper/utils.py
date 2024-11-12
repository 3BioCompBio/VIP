def reverse_complement(input_seq: str) -> str:
    NUCLEOTIDE_MAPPER = {"A": "T", "C": "G", "T": "A", "G": "C"}
    return "".join(NUCLEOTIDE_MAPPER[n] for n in input_seq[::-1])
