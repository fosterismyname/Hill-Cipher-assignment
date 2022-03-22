import numpy as np

key = [[4,3],[5,4]] #key-matrix
invertedKey = [[4,-3],[-5,4]]

def wordToNumbers(word):
    '''
    Converts the word into an array of numbers
    :param word: initial word
    :return: array of numbers which correspond to their characters
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
    for i in range(0, len(decryptedArr), 1):
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


def matrixMultiplication(curMatrix, multiplicator):
    '''
    Matrix multiplication
    :param cur_matrix: matrix of 2 symbols of original text (1x2)
    :prarm key: standart key (or reversed key)
    :return: matrix of encoded symbols (1x2)
    '''
    resultMatrix = []
    multMatrix = np.matmul(curMatrix, multiplicator)
    for i in range(2):
        #29 is the alphabet's length
        resultMatrix.append(multMatrix[i]%29)
    return resultMatrix


def toOutput(array):
    '''
    Writes array values to a string for better-looking output
    :param array: crypted or decrypted array
    '''
    toOutput = ''
    for i in range(len(array)):
        toOutput += array[i]
    print(toOutput)


# Algorythm
option = int(input('1:cipher\n2:decipher\n'))


if option == 1:
    word = input('word to cipher: ')
    if (len(word)%2) != 0:
        #Adding a single character to make the matrix multiplication possible
        word += 'Z'
    numberedWord = wordToNumbers(word)
    cryptedArr = []
    for i in range(0, len(numberedWord), 2):
        #Temporary variable to hold 2 numbers for multiplication
        mat = [numberedWord[i], numberedWord[i+1]]
        #Writing values to the ending array as numbers
        cryptedArr.append(matrixMultiplication(mat, key)[0])
        cryptedArr.append(matrixMultiplication(mat, key)[1])
    #Converting numbers to characters
    cryptedWord = numbersToWord(cryptedArr)
    #Printing the final output
    toOutput(cryptedWord)


elif option == 2:
    word = input('Enter the values: ')
    length = len(word)%2
    if (length) != 0:
        word += 'Z'
    numberedWord = wordToNumbers(word)
    decryptedArr = []
    for i in range(0, len(numberedWord), 2):
        mat = [numberedWord[i], numberedWord[i+1]]
        decryptedArr.append(matrixMultiplication(mat,invertedKey)[0])
        decryptedArr.append(matrixMultiplication(mat,invertedKey)[1])
    decryptedWord = numbersToWord(decryptedArr)
    toOutput(decryptedWord)
