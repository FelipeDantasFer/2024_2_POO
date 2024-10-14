valor = int(input())
a = valor // 100
b = (valor%100) // 50
c = ((valor%100)%50)//20
d = (((valor%100)%50)%20)//10
e = ((((valor%100)%50)%20)%10)//5
f = (((((valor%100)%50)%20)%10)%5)//2
g = ((((((valor%100)%50)%20)%10)%5)%2)//1
 
print(valor)
print(f"{a} nota(s) de R$ 100,00",)
print(f"{b} nota(s) de R$ 50,00",)
print(f"{c} nota(s) de R$ 20,00",)
print(f"{d} nota(s) de R$ 10,00",)
print(f"{e} nota(s) de R$ 5,00",)
print(f"{f} nota(s) de R$ 2,00",)
print(f"{g} nota(s) de R$ 1,00",)