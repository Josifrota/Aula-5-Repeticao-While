
# Exercicio 10

numero = int(input("Digite um número: "))

contador = 0

while contador <= numero:
    print(f"Número = {contador}")
    contador += 1

print("\n")
print("--------------------")

# Exercicio 11

contador = int(input("Digite um número: "))

while contador >= 0:
  print(f"Número =  {contador}")
  contador -= 1

print("\n")
print("--------------------")

# Exercicio 12

numero = int(input("Digite um número para saber a tabuada: "))

i = 0
while i <= 10:
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")
  i += 1

print("\n")
print("--------------------")

tabuada = int(input("Digite a tabuada que deseja executar: "))
contador=0
while tabuada <= 10:
  resultado=tabuada * contador
  print("Tabuada de ", tabuada * contador)
  tabuada += 1
  print(tabuada) 

print("\n")
print("--------------------")

# Exercicio 13

while True:
  numero = int(input("Digite um número para saber a tabuada: "))
  if numero >=1 and numero <= 10:
    break
  else:
    (print("Número fora do intervalo permitido"))

i = 0
while i <= 10:
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")
  i += 1

