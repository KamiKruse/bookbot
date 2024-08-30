def main():
    bookContent = getBook()
    numWords = wordCount(bookContent)
    # print(charCount(bookContent))
    listOfObjects = toList(charCount(bookContent))
    listOfObjects.sort(reverse=True, key=sort_on)
    report(listOfObjects, numWords)

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
    return [{"letter":key, "count":value} for key, value in dict.items()]

def sort_on(dict):
    return dict["count"]

def report(listOfObjs, numOfWords):
    print(f"--- Begin report of books/frankenstein.txt ---\n")
    print(f"{numOfWords} words was found in the document\n")
    for obj in listOfObjs:
        if obj["letter"].isalpha():
            print(f"The {obj['letter']} character was found {obj['count']} times")
    print("\n")
    print(f"--- End report ---")
                
main()
