n = int(input("Input value:"))

def timestable(n):
    for x in range (1, n+1):
        trueList = []
        for y in range (1, n+1):
            trueList.append(x*y) #end ="\t"
            return trueList
        #return("\n")

print (timestable(n))