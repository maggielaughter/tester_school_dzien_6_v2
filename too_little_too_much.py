import random

"""print(random.random()) # liczba od [0,1)
print(random.randint(0,10)) #liczba całkowita od 0 do 10 włącznie
print(random.choice(['a','b','c'])) #wybierze nam losową wartość z listy

print()
print()"""


def int_input(prompt):
    number = None
    while number is None:
        try:
            number = int(input(prompt))
        except ValueError:
            print('To nie była liczba...')
    return number

first=0
second = -1
while first > second:
    first=int_input('Podaj dół zakresu :')
    last=int_input('Podaj górę zakresu :')
    if first > second:
        print('Początek zakresu nie może być większy niż koniec...')

ran_number=random.randint(first,last)
count=0
answer = None

while answer != ran_number:
    count += 1
    answer = int_input('Podaj liczbę :')
    if answer > ran_number:
        print("Za dużo!")
    elif answer < ran_number:
        print("Za mało!")
print('Zgadłeś! Ilość ruchów :', count)
