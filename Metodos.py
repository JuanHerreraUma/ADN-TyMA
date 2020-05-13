# Juan Antonio Herrera Conde para TyMA. DNA Sequence.

Nucleotidos = ["A", "C", "G", "T"]
Compl = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
ADN_Codones = {"GCA": "A", "GCC": "A", "GCG": "A", "UGC": "C", "UGU": "C", "GAC": "D", "GAA": "E", "GAG": "E",
               "UUC": "F",
               "GGA": "G", "GGC": "G", "GGG": "G", "CAC": "H", "CAU": "H", "AUA": "I", "AUU": "I", "AAA": "K",
               "AAG": "K",
               "UUG": "L", "CUA": "L", "CUC": "L", "CUU": "L", "AUG": "M", "AAC": "N", "CCA": "P", "CCC": "P",
               "CCG": "P",
               "CAA": "Q", "CAG": "Q", "AGA": "R", "CGA": "R", "CGC": "R", "CGU": "R", "AGC": "S", "AGU": "S",
               "UCA": "S",
               "UCG": "S", "UCU": "S", "ACA": "T", "ACG": "T", "ACU": "T", "GUA": "V", "GUG": "V", "GUU": "V",
               "UGG": "W",
               "UAU": "Y", "UAG": "_", "UAA": "_", "GCU": "A", "GAU": "D", "UUU": "F", "GGU": "G", "AUC": "I",
               "UUA": "L",
               "CUG": "L", "AAU": "N", "CCU": "P", "AGG": "R", "CGG": "R", "UCC": "S", "ACC": "T", "GUC": "V",
               "UAC": "Y",
               "UGA": "_"}


# Validamos la secuencia
def validarSecuencia(dna_sec):
    tmpseq = dna_sec.upper()  # Necesitamos las letras en mayúsculas
    for nucleotidos in tmpseq:
        if nucleotidos not in nucleotidos:
            return False
    return tmpseq


# Contar la frecuencia de los nucleótidos

def contarFrecuenciaNuc(dna_sec):
    tmpFreq = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nucleotidos in dna_sec:
        tmpFreq[nucleotidos] += 1

    print("A=",(tmpFreq["A"] / len(dna_sec)) * 100,"%",
          "C=",(tmpFreq["C"] / len(dna_sec)) * 100,"%",
          "G=",(tmpFreq["G"] / len(dna_sec)) * 100,"%",
          "T=",(tmpFreq["T"] / len(dna_sec)) * 100,"%",)

def transcripcion(dna_seq):
    # Proceso en el que el adn se transforma en arn antes de ser traducido a proteinas
    return dna_seq.replace("T", "U")


def Complementaria(seq):
    return ''.join([Compl[nucleotidos] for nucleotidos in seq])


def reversaComplementaria(seq):
    return ''.join([Compl[nucleotidos] for nucleotidos in seq])[::-1]


def traduccion(seq, init_pos=0):
    return [ADN_Codones[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)]


def marcosLectura(seq):
    # Genera seis marcos de lectura
    marcos = []
    marcos.append(traduccion(seq, 0))
    marcos.append(traduccion(seq, 1))
    marcos.append(traduccion(seq, 2))
    marcos.append(traduccion(seq, 3))
    marcos.append(traduccion(seq, 4))
    marcos.append(traduccion(seq, 5))

    return marcos


def codones(seq):
    numeroNucleotidos = len(seq)
    start_position = 0
    for b in range(numeroNucleotidos):
        if (seq[b:b + 3] == "AUG"):
            start_position = b
            print("Codon de inicio detectado. Ahora leemos las bases de tres en tres...")
            break
    for t in range(start_position, numeroNucleotidos, 3):
        codon = seq[t:t + 3]
        print(codon)
        if (codon == "UAA"):
            print("Un codon de parada!")
        elif (codon == "UAG"):
            print("Un codon de parada!")
        elif (codon == "UGA"):
            print("Un codon de parada!")
