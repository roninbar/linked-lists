from LinkedList import LinkedList

small_primes = LinkedList(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
k = 1
for n in range(2, 1000):
    qs = [p for p in small_primes if p * p <= n]
    for q in qs:
        if n % q == 0:
            break
    else:
        print(f'[{k}] {n}')
        k += 1
