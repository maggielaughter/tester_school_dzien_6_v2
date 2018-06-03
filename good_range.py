def good_range(number1, number2):
    while number 1 > number2:
        try:
            number1=int(input("Podaj liczbę :"))
            number2=int(input("Podaj liczbę :"))
        except ValueError:
            print('Liczba nr 2 jest za mała w stosunku do liczby nr 1!')
    return number1, number2

print(good_range(5,1))