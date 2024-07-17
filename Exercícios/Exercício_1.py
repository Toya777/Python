res = int

print("\n-----Calculadora-----\n")

num01 = int(input("\nDigite o primeiro numero da soma:"))
sinal = str(input("\nDigite o sinal:"))
num02 = int(input("\nDigite o segundo numero:"))

if(sinal == "-"):   
    res = num01 - num02
    print("o resultado é: ", res)
elif (sinal == "+"):
    res = num01 + num02
    print("o resultado é: ", res)
elif(sinal == "/" ):
    res = num01 / num02
    print("O resultado é: ", res)
elif(sinal == "*"):
    res = num01 * num02
    print("O resultado é: ", res)
else:
    print("sinal invalido")