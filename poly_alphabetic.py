import sys
import getopt
import random
import string
import matplotlib.pyplot as plt
from collections import Counter

# Generates K random substitution tables
def generate_substitution_tables(K):
    tables = []
    alphabet = list(string.ascii_lowercase)
    for _ in range(K):
        shuffled = alphabet[:]
        random.shuffle(shuffled)
        tables.append(str.maketrans(string.ascii_lowercase, ''.join(shuffled)))
    return tables

# Encryption using K cyclic substitution tables
def encrypt_poly(input_file, output_file, K):
    with open(input_file, 'r') as f:
        text = f.read().lower()

    tables = generate_substitution_tables(K)
    encrypted = []

    for i, char in enumerate(text):
        if char in string.ascii_lowercase:
            table = tables[i % K]
            encrypted.append(char.translate(table))
        else:
            encrypted.append(char)

    with open(output_file, 'w') as f:
        f.write(''.join(encrypted))
    print(f"Encrypted using {K} substitution tables.")

# Frequency analysis for each step (step) from 2 to 10
def crack_poly_cipher(file_path):
    with open(file_path, 'r') as f:
        text = f.read().lower()

    steps = range(2, 11)
    most_frequent_percentages = []

    for step in steps:
        segments = ['' for _ in range(step)]
        for i, char in enumerate(text):
            if char in string.ascii_lowercase:
                segments[i % step] += char

        avg_freqs = []
        for segment in segments:
            if segment:
                freq = Counter(segment)
                most_common_letter, count = freq.most_common(1)[0]
                percentage = (count / len(segment)) * 100
                avg_freqs.append(percentage)

        avg = sum(avg_freqs) / len(avg_freqs)
        most_frequent_percentages.append(avg)

    # Graphical display
    plt.plot(list(steps), most_frequent_percentages, marker='o')
    plt.title("Most Frequent Letter % by Step (Key Length Guess)")
    plt.xlabel("Step Value (Guessed Key Length)")
    plt.ylabel("Avg. % of Most Frequent Letter")
    plt.grid(True)
    plt.show()

# Command-line interface
def main():
    input_file = output_file = None
    K = None
    encrypt_mode = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:K:e")
    except getopt.GetoptError as err:
        print(err)
        sys.exit(1)

    for o, a in opts:
        if o == "-i":
            input_file = a
        elif o == "-o":
            output_file = a
        elif o == "-K":
            K = int(a)
        elif o == "-e":
            encrypt_mode = True

    if encrypt_mode:
        if not input_file or not output_file or not K:
            print("Usage: -i <input> -o <output> -K <number_of_tables> -e")
            sys.exit(1)
        encrypt_poly(input_file, output_file, K)
    else:
        if not input_file:
            print("Usage for crack mode: -i <ciphertext_file>")
            sys.exit(1)
        crack_poly_cipher(input_file)

if __name__ == "__main__":
    main()