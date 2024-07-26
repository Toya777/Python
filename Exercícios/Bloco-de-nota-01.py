resultado = float
print("\n---------CALCULADORA---------")

for i in range(1000000):
    num01 = float(input("\nDigite o primeiro numero: "))
    sinal = str(input("\nDigite o sinal: "))
    num02 = float(input("\nDigite o segundo numero: ")) 
    if(sinal == "-"):
        resultado = num01 - num02
        print("\nO resultado é: ", resultado)    
    elif(sinal == "+"):
        resultado = num01 + num02
        print("\nO resultado é: ", resultado)
    elif(sinal == "*"):
        resultado = num01 * num02
        print("\nO resultado é: ", resultado)
    elif(sinal == "/"):
        resultado = num01 / num02
        print("\nO resultado é: ", resultado)
    elif(sinal == "%"):
        resultado = num01 % num02
        print("\nO resultado é: ", resultado)
    else:
        print("\nSinal invalido")

    avancar = input("Digite nao caso nao queira continuar: ")
    if(avancar == "nao"):
        break