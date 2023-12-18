def pollard_rho(n):
    if n % 2 == 0:
        return 2
    x = 1
    y = 1
    c = 1
    d = 1
    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = gcd(abs(x - y), n)
    return d

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def factors(file):
    with open(file, 'r') as f:
        for line in f:
            n = int(line.strip())
            d = pollard_rho(n)
            while d != n:
                print(f"{n}={d}*{n//d}")
                n = d
                d = pollard_rho(n)

if __name__ == "__main__":
    import sys
    factors(sys.argv[1])
