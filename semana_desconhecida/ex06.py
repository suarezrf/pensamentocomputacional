fibonacci = [0, 1]

for i in range(13):
    soma = fibonacci[i] + fibonacci[i + 1]
    fibonacci.append(soma)

print(fibonacci)
