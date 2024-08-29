def main():
    bookContent = getBook()
    numWords = wordCount(bookContent)
    # print(charCount(bookContent))
    listOfObjects = toList(charCount(bookContent))
    print(test(listOfObjects))

def getBook():
    bookpath = "books/frankenstein.txt"
    return readBook(bookpath)

def readBook(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def wordCount(text):
    words = text.split()
    return len(words)

#The file contents from read are passed in as individual words. Hence the below code works
def charCount(wordArr):
    charC = {}
    for char in wordArr:
        lowChar = char.lower()
        if lowChar in charC:
            charC[lowChar] += 1
        else:
            charC[lowChar] = 1
    return charC

def toList(dict):
    return [{key:value} for key, value in dict.items()]

def test(arr):
    narr = []
    for i in arr:
        for key, value in i.items():
            if key.isalpha():
                narr.append(value)
    return narr

                
main()
