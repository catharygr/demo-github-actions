def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

if __name__ == "__main__":
    print(sumar(1, 2))
    print(restar(1, 2))
    print(multiplicar(1, 2))
    try:
       print(dividir(5, 2))
       print(dividir(1, 0))
    except ValueError as e:
        print(e)



