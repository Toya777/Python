resultado = int
print("\n---------CALCULADORA---------")

num01 = int(input("\nDigite o primeiro numero: "))
sinal = str(input("\nDigite o sinal: "))
num02 = int(input("\nDigite o segundo numero: "))

if(sinal == "-"):
    resultado = num01 - num02
    print("\nO resultado é: ", resultado)
    
elif(sinal == "+"):
    resultado = num01 + num02
    print("\nO resultado é: ", resultado)
    
else:
    print("\nSinal invalido")