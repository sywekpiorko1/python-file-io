f = open('files/data.txt', 'r+')

f.seek(0)
f.write("Newe A\n")

f.seek(14)
f.write("Newe C\n")

f.close()

f = open('files/data.txt', 'a')
f.write("Newe E\n")
f.close()