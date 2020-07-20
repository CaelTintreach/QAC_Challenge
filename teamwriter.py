file = open ("Teams.txt", "w")

file.write("M.Un" + "\n")
file.write("L.Pool" + "\n")
file.write("C.Sea" + "\n")
file.write("S.Field" + "\n")
file.write("N.Iron" + "\n")

file.close

file = open ("Teams.txt", "r")

print(file.readline())
file.readline()
file.readline()
print(file.readline())

file.close