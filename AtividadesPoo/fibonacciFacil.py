n = int(input())

fibonacci = []

if n >= 1:
    fibonacci.append(0)
if n >=2:
    fibonacci.append(1)

for i in range(2, n):
    proximo = fibonacci [i - 1] + fibonacci[i - 2]
    fibonacci.append(proximo)
    
print(" ".join(map(str,fibonacci)))