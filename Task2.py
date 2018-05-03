def isPrime(szam):
    if szam <= 1:
        return 'Not Prime'
    for i in range(2, szam):
        if szam%i==0:
            return 'Not Prime'
    return 'Prime'


def largest_prime_factor(n):
    list1=[]
    list2=[]
    for i in range(2, n):
        if n % i == 0:
            list1.append(i)

    for i in list1:
        if isPrime(i) == 'Prime':
            list2.append(i)

    max = 0
    for j in list2:
        if j > max:
            max = j
    return max

print(largest_prime_factor(13195))