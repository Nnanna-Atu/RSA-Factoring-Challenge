import math

def factorize_number(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return n, 1

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]

    factorizations = [f"{n}={'*'.join(map(str, factorize_number(n)))}" for n in numbers]

    return factorizations

if __name__ == "__main__":
    file_path = "tests/test00"
    result = factorize_file(file_path)

    for line in result:
        print(line)

