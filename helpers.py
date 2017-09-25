def alphabet_position(letter):
    letters = {
        "A" : 0,
        "B" : 1,
        "C" : 2,
        "D" : 3,
        "E" : 4,
        "F" : 5,
        "G" : 6,
        "H" : 7,
        "I" : 8,
        "J" : 9,
        "K" : 10,
        "L" : 11,
        "M" : 12,
        "N" : 13,
        "O" : 14,
        "P" : 15,
        "Q" : 16,
        "R" : 17,
        "S" : 18,
        "T" : 19,
        "U" : 20,
        "V" : 21,
        "W" : 22,
        "X" : 23,
        "Y" : 24,
        "Z" : 25,
    }
    return letters[letter.upper()]

def rotate_character(letter, amt):
    letters = {
        "A" : 0,
        "B" : 1,
        "C" : 2,
        "D" : 3,
        "E" : 4,
        "F" : 5,
        "G" : 6,
        "H" : 7,
        "I" : 8,
        "J" : 9,
        "K" : 10,
        "L" : 11,
        "M" : 12,
        "N" : 13,
        "O" : 14,
        "P" : 15,
        "Q" : 16,
        "R" : 17,
        "S" : 18,
        "T" : 19,
        "U" : 20,
        "V" : 21,
        "W" : 22,
        "X" : 23,
        "Y" : 24,
        "Z" : 25,
    }
    if not letter.isalpha():
        return letter

    elif letter.islower():
        lett = (alphabet_position(letter))
        letts = lett + amt
        letts = letts % 26
        return (list(letters.keys())[list(letters.values()).index(letts)]).lower()
    else:
        lett = (alphabet_position(letter))
        letts = lett + amt
        letts = letts % 26
        return (list(letters.keys())[list(letters.values()).index(letts)]).upper()
 
