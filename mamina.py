# prime numbers until n
n = int(input("Enter a number: "))

prime = []
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)
print(len(prime))