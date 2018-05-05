def isPrime(szam):
    if szam <= 1:
        return False
    for i in range(2, szam):
        if szam%i==0:
            return False
    return True

def nthPrime(n):
    primes=[]
    j=2
    while len(primes)<n:
        if (isPrime(j)) == True:
            primes.append(j)
        j+=1
    print("A keresett szám:",str(primes[n-1]))

nthPrime(10001)


