qwerty_grafite_keymap = {
    'b': 'q',
    'l': 'w',
    'd': 'e',
    'w': 'r',
    'z': 't',
    "'": 'y',
    'f': 'u',
    'o': 'i',
    'u': 'o',
    'j': 'p',
    'n': 'a',
    'r': 's',
    't': 'd',
    's': 'f',
    'g': 'g',
    'y': 'h',
    'h': 'j',
    'a': 'k',
    'e': 'l',
    'l': ';',
    'q': 'z',
    'x': 'x',
    'm': 'c',
    'c': 'v',
    'v': 'b',
    'k': 'n',
    'p': 'm',
    '.': ',',
    '-': '.',
    'B': 'Q',
    'L': 'W',
    'D': 'E',
    'W': 'R',
    'Z': 'T',
    "'": 'Y',
    'F': 'U',
    'O': 'I',
    'U': 'O',
    'J': 'P',
    'N': 'A',
    'R': 'S',
    'T': 'D',
    'S': 'F',
    'G': 'G',
    'Y': 'H',
    'H': 'J',
    'A': 'K',
    'E': 'L',
    'L': ':',
    'Q': 'Z',
    'X': 'X',
    'M': 'C',
    'C': 'V',
    'V': 'B',
    'K': 'N',
    'P': 'M',
}

input = input('Enter text: ')

output = ''

for char in input:
    if char in qwerty_grafite_keymap:
        output += qwerty_grafite_keymap[char]
    else:
        output += char

print(output)
