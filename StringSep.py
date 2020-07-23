def stringsplitsort():
    words = "This is a test string."
    words = words.split()
    #wordslist = ("This", "is", "a","test","string")
    words.sort(key=lambda ele: str(ele[1]))
    #sorted(wordslist, reverse=True)
    print("The sorted words are:")
    for word in words:
        print(word)
    #print(wordslist)

stringsplitsort()