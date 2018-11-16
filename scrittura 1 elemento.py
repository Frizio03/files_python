#LETTURA
def readFile(fileName): 
  out = []
  file = open(fileName)
  r = file.readlines()
  file.close()

  for e in r:
    out.append(int(e.replace("\n", "")))

  return out

lista = readFile('./input1.txt')

#PROGRAMMA
somma = 0
for numero in lista:
  somma += numero

#SALAVATGGIO
file = open('./output1.txt', 'w')
file.write(str(somma))
file.close()