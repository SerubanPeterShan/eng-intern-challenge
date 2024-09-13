# I had to change the python3 to python as my powershell was not recognizing python3
# Separate dictionaries for letters, numbers, and symbols
# Each dictionary maps a character to its corresponding braille representation
# I needed to do this as python does not know which is number and which is letter so i seperated them into defferent dictionaries
braille_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OO.OO', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

braille_symbols = {
    '.': '.O.OOO', ',': '.O....', ';': '.OO...', ':': '.O.O..', '?': '.O..O.',
    '!': '.OO.O.', '(': '.OOO.O', ')': '.OOO.O', '-': '..O.O.', '/': '..OO..',
    ' ': '......'
}

capital_follows = '.....O'
number_follows = '.O.OOO'
decimal_point = '.O...O'

# This function will convert the text to braille if it's numbe or letter or symbol it will check the respective dictionary and convert it to braille by checking each character
def text_to_braille(text):
    braille = []
    number_mode = False
    for chr in text:
        if chr.isupper():
            braille.append(capital_follows)
            chr = chr.lower()
        if chr.isdigit():
            if not number_mode:
                braille.append(number_follows)
                number_mode = True
            braille.append(braille_numbers.get(chr, '......'))
        elif chr == '.':
            if not number_mode:
                braille.append(number_follows)
                number_mode = True
            braille.append(decimal_point)
        else:
            number_mode = False
            braille.append(braille_letters.get(chr, braille_symbols.get(chr, '......')))
    return ''.join(braille)

# This function will convert the braille to text if it's numbe or letter or symbol it will check the respective dictionary and convert it to text by checking each 6 characters
def braille_to_text(braille):
    text = []
    i = 0
    number_mode = False
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == capital_follows:
            i += 6
            symbol = braille[i:i+6]
            char = next((k for k, v in braille_letters.items() if v == symbol), ' ')
            text.append(char.upper())
        elif symbol == number_follows:
            number_mode = True
            i += 6
            continue
        elif symbol == decimal_point:
            text.append('.')
            i += 6
            continue
        else:
            if number_mode:
                chr = next((k for k, v in braille_numbers.items() if v == symbol), ' ')
                if chr.isdigit():
                    text.append(chr)
                else:
                    number_mode = False
                    chr = next((k for k, v in braille_letters.items() if v == symbol), ' ')
                    text.append(chr)
            else:
                chr = next((k for k, v in braille_letters.items() if v == symbol), ' ')
                if chr == ' ':
                    chr = next((k for k, v in braille_symbols.items() if v == symbol), ' ')
                text.append(chr)
        i += 6
    return ''.join(text)

# I use this function checks if the input text is in braille or text
def is_braille(input_text):
    return all(chr in 'O.' for chr in input_text) and len(input_text) % 6 == 0

# This function is the main function this will seprarate the input text and call the respective function and later use is_braille function to check if the input text is in braille or text
def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        return
    
    input_text = ' '.join(sys.argv[1:])
    
    if is_braille(input_text):
        print(braille_to_text(input_text))
    else:
        print(text_to_braille(input_text))

if __name__ == "__main__":
    main()