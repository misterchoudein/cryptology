import argparse
import os
import sys
import json
import matplotlib.pyplot as plt

def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = []
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            result.append(char)
    return ''.join(result)

def load_dictionary(dictionary_file):
    try:
        with open(dictionary_file, 'r') as file:
            return set(json.load(file))
    except IOError:
        print(f"Error: Cannot read dictionary file '{dictionary_file}'.")
        sys.exit(1)

def calculate_match_percentage(text, dictionary):
    words = text.split()
    if not words:
        return 0
    match_count = sum(1 for word in words if word.lower() in dictionary)
    return (match_count / len(words)) * 100

def brute_force_caesar(text, dictionary):
    results = []
    for key in range(1, 26):
        decrypted = caesar_cipher(text, key, decrypt=True)
        match_percentage = calculate_match_percentage(decrypted, dictionary)
        results.append((key, decrypted, match_percentage))
    return results

def plot_results(results):
    keys = [result[0] for result in results]
    percentages = [result[2] for result in results]

    plt.figure(figsize=(10, 5))
    plt.plot(keys, percentages, marker='o')
    plt.title('Brute Force Caesar Cipher Match Percentages')
    plt.xlabel('Key')
    plt.ylabel('Match Percentage')
    plt.xticks(keys)
    plt.grid(True)
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Tool")
    parser.add_argument('-i', '--input', required=True, help="Input file")
    parser.add_argument('-o', '--output', help="Output file")
    parser.add_argument('-K', '--key', type=int, help="Shift key (1-26)")
    parser.add_argument('-e', '--encrypt', action='store_true', help="Encrypt the file")
    parser.add_argument('-d', '--decrypt', action='store_true', help="Decrypt the file")
    parser.add_argument('-b', '--bruteforce', action='store_true', help="Brute force decrypt the file")
    parser.add_argument('-w', '--dictionary', help="Dictionary file for brute force")

    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print(f"Error: Input file '{args.input}' does not exist.")
        sys.exit(1)

    try:
        with open(args.input, 'r') as infile:
            text = infile.read()
    except IOError:
        print(f"Error: Cannot read input file '{args.input}'.")
        sys.exit(1)

    if args.bruteforce:
        if not args.dictionary:
            print("Error: Dictionary file is required for brute force.")
            sys.exit(1)
        dictionary = load_dictionary(args.dictionary)
        results = brute_force_caesar(text, dictionary)
        for key, decrypted, match_percentage in results:
            print(f"Key: {key}, Match Percentage: {match_percentage:.2f}%, Decrypted: {decrypted}")
        plot_results(results)
        sys.exit(0)

    if args.encrypt and args.decrypt:
        print("Error: Cannot specify both --encrypt and --decrypt.")
        sys.exit(1)

    if not args.encrypt and not args.decrypt:
        print("Error: Must specify either --encrypt or --decrypt.")
        sys.exit(1)

    if not (1 <= args.key <= 25):
        print("Error: Shift key must be between 1 and 25.")
        sys.exit(1)

    result = caesar_cipher(text, args.key, decrypt=args.decrypt)

    if args.output:
        try:
            with open(args.output, 'w') as outfile:
                outfile.write(result)
        except IOError:
            print(f"Error: Cannot write to output file '{args.output}'.")
            sys.exit(1)
    else:
        print(result)

if __name__ == "__main__":
    main()