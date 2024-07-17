resultado = float
print("\n---------CALCULADORA---------")

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
    
if(num02 == 0):
    print("\nErro: Divisão por zero não é permitida.")
elif(sinal == "%"):
    resultado = num01 % num02
    print("\nO resultado é: ", resultado)
else:
    print("\nO resultado é: ", resultado)