word = input("Input the word to crypt: ")
numberedWord = []
# Switch to convert the word into an array of numbers
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
        case "v":
            num = 22
        case "w":
            num = 23
        case "x":
            num = 24
        case "y":
            num = 25
        case "z":
            num = 26
        case " ":
            num = 27
        case ".":
            num = 28
        case ",":
            num = 29

    numberedWord.append(num)
print(numberedWord)
