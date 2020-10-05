# Zackery Beane
# 9.28.2020

import numpy as np
import matplotlib.pyplot as plt

ecoli =  "Ecoli-bacteria-complete-genome-low-GC.fasta"
thermo = "thermophile-thermo-microbium-complete-genome-has-high-CGs.fasta"


def Genome(genome):
    count = 0
    numA = 0
    numC = 0
    numG = 0
    numT = 0
    with open(genome) as fp:
        for line in fp:
            if line.count('>') == 0:
                if 'A' in line:
                    numA += line.count('A')
                if 'C' in line:
                    numC += line.count('C')
                if 'G' in line:
                    numG += line.count('G')
                if 'T' in line:
                    numT += line.count('T')
            count += 1
            print("Line{}: {}".format(count, line.strip()))

    perA = (numA) / (numA + numC + numG + numT) * 100
    perC = (numC) / (numA + numC + numG + numT) * 100
    perG = (numG) / (numA + numC + numG + numT) * 100
    perT = (numT) / (numA + numC + numG + numT) * 100
    print("A# = " + str(numA) + "A% = " + str(perA))
    print("C# = " + str(numC) + "C% = " + str(perC))
    print("G# = " + str(numG) + "G% = " + str(perG))
    print("T# = " + str(numT) + "T% = " + str(perT))
    # creating the dataset
    data = {'A': perA, 'C': perC, 'G': perG,
            'T': perT}
    genes = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(genes, values, color='maroon',
            width=0.4)

    plt.xlabel("letters")
    plt.ylabel("percentage of letter")
    plt.title("percentage of each letter in " + genome)
    plt.show()


Genome(ecoli)
Genome(thermo)

