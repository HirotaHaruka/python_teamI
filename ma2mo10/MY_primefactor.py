import sys

args = sys.argv

def prime_factor(n):
    prime_list = []
    for i in range(2, int((n**0.5//1))+1):
        if n%i == 0:
            while n%i == 0:
                n = n // i
                prime_list.append(i)
    
    if prime_list == []:
        prime_list.append(n)
    elif n > i:
        for j in range(i, n+1):
            if n%j == 0:
                prime_list.append(j)

    return prime_list


print(prime_factor(int(args[1])),end="")