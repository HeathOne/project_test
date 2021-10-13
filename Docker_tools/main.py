one = int(input('Введите one: '))
two = int(input('Введите two: '))

for k in range(one, two+1):
    if k == 1:
        continue
    prime = True

    for i in range(2, k):
        if k % i == 0:
            prime = False
            break

    if prime:
        print(k)
