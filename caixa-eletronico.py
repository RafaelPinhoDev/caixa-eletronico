print("-------------------------------")
print("CAIXA ELETRÔNICO")
print("-------------------------------")
print("Notas Disponíveis: R$ 1, R $2, R$ 5, R$ 10,R$ 20, R$ 50, R$ 100")
print("                                                                ")
saldo = int(input("Digite o valor que deseja sacar: R$"))
print("                                                                ")
n100 = n50 = n20 = n10 = n5 = n2 = n1 = 0

if saldo >= 100:
    n100 = saldo//100
    saldo = saldo - n100*100
if saldo >= 50:
    n50 = saldo//50
    saldo = saldo - n50*50
if saldo >= 20:
    n20 = saldo//20
    saldo = saldo - n20*20
if saldo >= 10:
    n10 = saldo//10
    saldo = saldo - n10*10
if saldo >= 5:
    n5 = saldo//5
    saldo = saldo - n5*5
if saldo >= 2:
    n2 = saldo//2
    saldo = saldo - n2*2
if saldo >= 1:
    n1 = saldo

print("Notas de R$ 100: ", n100)
print("Notas de R$ 50: ", n50)
print("Notas de R$ 20: ", n20)
print("Notas de R$ 10: ", n10)
print("Notas de R$ 5: ", n5)
print("Notas de R$ 2: ", n2)
print("Notas de R$ 1: ", n1)
