LETRAS = "AEIOU"
texto = input("Informe um texto: ")

#sem for else
for letra in texto:
    if letra.upper() in LETRAS:
        print(letra, end=" ")
        print(letra.upper(), end="\n")

print()#linha em branco

texto += texto

#com for else
for letra in texto:
    if letra.upper() in LETRAS:
        print(letra, end=" ")
        print(letra.upper(), end="\n")
else:
    print()

for numero in range(0,11):
    print(numero, end= " ")

for numero in range(0, 51, 5):
    print(numero, end= "\n")