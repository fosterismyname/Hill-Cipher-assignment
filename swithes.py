def wordToNumbers(word):
    '''
    Converts the word into an array of numbers
    :param word: initial word
    :return: an array of numbers which correspond to a character
    '''
    numberedWord = []
    for i in range(len(word)):
        letter = word[i]
        match letter:
            case "a":
                num = 0
            case "b":
                num = 1
            case "c":
                num = 2
            case "d":
                num = 3
            case "e":
                num = 4
            case "f":
                num = 5
            case "g":
                num = 6
            case "h":
                num = 7
            case "i":
                num = 8
            case "j":
                num = 9
            case "k":
                num = 10
            case "l":
                num = 11
            case "m":
                num = 12
            case "n":
                num = 13
            case "o":
                num = 14
            case "p":
                num = 15
            case "q":
                num = 16
            case "r":
                num = 17
            case "s":
                num = 18
            case "t":
                num = 19
            case "u":
                num = 20
            case "v":
                num = 21
            case "w":
                num = 22
            case "x":
                num = 23
            case "y":
                num = 24
            case "z":
                num = 25
            case " ":
                num = 26
            case ".":
                num = 27
            case ",":
                num = 28

        numberedWord.append(num)
    return(numberedWord)


def numbersToWord(decryptedArr):
    '''
    Converts an array of into the word (symbols)
    :param decryptArr: the result of multiplication of the key^-1 matrix and the encrypted word array
    :return: the decrypted word
    '''
    decryptedWord = []
    for i in range(len(decryptedArr)):
        symbol = decryptedArr[i]
        match symbol:
            case 0:
                symb = 'a'
            case 1:
                symb = 'b'
            case 2:
                symb = 'c'
            case 3:
                symb = 'd'
            case 4:
                symb = 'e'
            case 5:
                symb = 'f'
            case 6:
                symb = 'g'
            case 7:
                symb = 'h'
            case 8:
                symb = 'i'
            case 9:
                symb = 'j'
            case 10:
                symb = 'k'
            case 11:
                symb = 'l'
            case 12:
                symb = 'm'
            case 13:
                symb = 'n'
            case 14:
                symb = 'o'
            case 15:
                symb = 'p'
            case 16:
                symb = 'q'
            case 17:
                symb = 'r'
            case 18:
                symb = 's'
            case 19:
                symb = 't'
            case 20:
                symb = 'u'
            case 21:
                symb = 'v'
            case 22:
                symb = 'w'
            case 23:
                symb = 'x'
            case 24:
                symb = 'y'
            case 25:
                symb = 'z'
            case 26:
                symb = ' '
            case 27:
                symb = '.'
            case 28:
                symb = ','
        decryptedWord.append(symb)
    return decryptedWord


