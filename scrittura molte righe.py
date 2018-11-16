#LETTURA
def readFile(fileName): 
  out = []
  file = open(fileName)
  r = file.readlines()
  file.close()

  for e in r:
    out.append(int(e.replace("\n", "")))

  return out

#SALVATAGGIO
def saveFile(fileName, list):
  file = open(fileName, "w")
  for r in list:
    file.write(str(r) + "\n")
  file.close()

#PROGRAMMA
numeri = readFile("./input4.txt")
out = [ numeri[0] ]

for i in range(1, len(numeri)):
  out.append(numeri[i] * numeri[i-1])

saveFile('./output4.txt', out)