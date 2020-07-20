file = open ("Teams.txt", "r")
datakept = ""

for line in range (0,6):
    if line != "M.Un":
        datakept += file.readline()
    else:
        file.readline

file.close()

file = open ("Teams.txt", "w")
file.write("This is a new line." + "\n")
file.write(datakept)

file.close()

file = open ("Teams.txt", "r")
file = open("filename.txt", "r")
lines = file.readlines()
print(lines)
file.close()