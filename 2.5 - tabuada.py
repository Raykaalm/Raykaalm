numero = int(input("Insira a tabuada que deseja: "))
inicio = int(input("Iniciar a tabuada por qual número? "))
fim = int(input("Finalizar a tabuada por qual número? "))

for i in range (inicio, fim+1):
  print(f" {i} x {numero} = {i*numero} ")
  