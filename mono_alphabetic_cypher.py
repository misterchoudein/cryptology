import sys
import getopt
import string
import matplotlib.pyplot as plt
from collections import Counter

def cypher(input_file, output_file, key, mode):
    with open(input_file, 'r') as f:
        text = f.read()
    if key.isdigit():
        key = generate_key(int(key))
    if mode == 'e':
        alphabet = string.ascii_lowercase
        table = str.maketrans(alphabet, key)
    elif mode == 'd':
        alphabet = key
        table = str.maketrans(key, alphabet)
    else:
        raise ValueError('Invalid mode')
    text = text.translate(table)
    with open(output_file, 'w') as f:
        f.write(text)

def generate_key(shift):
    alphabet = string.ascii_lowercase
    return alphabet[shift:] + alphabet[:shift]

def letter_frequency(text):
    return Counter(text)

def plot_frequency(frequencies, title):
    letters = list(frequencies.keys())
    counts = list(frequencies.values())
    plt.bar(letters, counts)
    plt.title(title)
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.show()

def identify_e_letter(frequencies):
    most_common = frequencies.most_common(1)
    return most_common[0][0] if most_common else None

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'i:o:k:ed')
    except getopt.GetoptError as err:
        print(err)
        sys.exit(1)
    input_file = None
    output_file = None
    key = None
    mode = None
    for o, a in opts:
        if o == '-i':
            input_file = a
        elif o == '-o':
            output_file = a
        elif o == '-k':
            key = a
        elif o == '-e':
            mode = 'e'
        elif o == '-d':
            mode = 'd'
    if not input_file or not output_file or not key or not mode:
        print('Usage: {} -i input_file -o output_file -k key -e|-d'.format(sys.argv[0]))
        sys.exit(1)
    cypher(input_file, output_file, key, mode)

    with open(output_file, 'r') as f:
        text = f.read()
    frequencies = letter_frequency(text)
    
    # Print the occurrences of each letter
    print("Letter occurrences:")
    for letter, count in frequencies.items():
        print(f"{letter}: {count}")
    
    plot_frequency(frequencies, 'Letter Frequency in Ciphered Text')
    e_letter = identify_e_letter(frequencies)
    print(f'The letter that encrypts "e" is likely: {e_letter}')

if __name__ == '__main__':
    main()