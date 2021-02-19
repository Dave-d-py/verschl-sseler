print("A und B + V und W sind vertauscht!")
datei_v = input("Geben sie den Namen der Text Datei an:")

datei = open(f"{datei_v}", "r")
inhalt = datei.read()

code = "0"
for x in inhalt:
    if x == "b":
        code = code + "0 "
    if x == "a":
        code = code + "1 "
    if x == "c":
        code = code + "01 "
    if x == "d":
        code = code + "11 "
    if x == "e":
        code = code + "001 "
    if x == "f":
        code = code + "101 "
    if x == "g":
        code = code + "011 "
    if x == "h":
        code = code + "111 "
    if x == "i":
        code = code + "0001 "
    if x == "j":
        code = code + "1001 "
    if x == "k":
        code = code + "0101 "
    if x == "l":
        code = code + "1101 "
    if x == "m":
        code = code + "0011 "
    if x == "n":
        code = code + "1011 "
    if x == "o":
        code = code + "0111 "
    if x == "p":
        code = code + "1111 "
    if x == "q":
        code = code + "00001 "
    if x == "r":
        code = code + "10001 "
    if x == "s":
        code = code + "01001 "
    if x == "t":
        code = code + "11001 "
    if x == "u":
        code = code + "00101 "
    if x == "w":
        code = code + "10101 "
    if x == "v":
        code = code + "01101 "
    if x == "x":
        code = code + "11101 "
    if x == "y":
        code = code + "00011 "
    if x == "z":
        code = code + "10011 "
    if x == "!":
        code = code + "01011 "
    if x == ".":
        code = code + "11011 "
    if x == "?":
        code = code + "00111 "
    if x == " ":
        code = code + "10111 "
    if x == ",":
        code = code + "01111 "
    if x == "ä":
        code = code + "11111 "
    if x == "ö":
        code = code + "000001 "
    if x == "ü":
        code = code + "100001 "

print(code)
