
def modulo(a, b):
    """
    Retourne le reste de la division de a par b
    Arguments :
        a: dividende
        b: diviseur
    Retour:
        le reste de la division de a par b

    Examples:
    >>> modulo(10, 3)
    1
    >>> modulo(8, 2)
    0
    >>> modulo(7, 5)
    2
    >>> modulo(9, 4)
    1
    >>> modulo(5, 8)
    5
    >>> modulo(0, 1)
    0
    >>> modulo(1, 1)
    0
    """
    return a % b

if __name__ == '__main__':
    #les tests
    import doctest
    doctest.testmod()
    print("Modulo de 10 par 3 est :", end=' ')
    print(modulo(10, 3))
    print("Modulo de 8 par 2 est :", end=' ')
    print(modulo(8, 2))
    print("Modulo de 7 par 5 est :", end=' ')
    print(modulo(7, 5))
    print("Modulo de 9 par 4 est :", end=' ')
    print(modulo(9, 4))
    print("Modulo de 5 par 8 est :", end=' ')
    print(modulo(5, 8))
    print("Modulo de 0 par 1 est :", end=' ')
    print(modulo(0, 1))
    print("Modulo de 1 par 1 est :", end=' ')
    print(modulo(1, 1))