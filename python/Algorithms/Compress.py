def compressIt():
    text = input("Please enter the text you need to be compress: ")
    text = list(text)
    compressed = []
    def printError(charError):
        print("You entered \"" + charError + "\". Please enter alphabetical characters and spaces only.")  
    for i in text:
        if i == " ":
            text.remove(i)
        elif i.isalpha() == False:
            printError(i)
            return compressIt()
            
    j = 0
    while j < len(text):
        num = 1
        c = text[j]

        while j != len(text) - 1 and text[j + 1] == text[j]:
            num = num + 1
            j = j + 1
        if num != 1:
            compressed.append(str(num))
        compressed.append(c)
        j = j + 1
        
    compressed = ''.join(compressed)
    print("Compressed text: ", compressed)
    return compressIt()

compressIt()
