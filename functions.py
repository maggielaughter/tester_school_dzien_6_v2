def square(x):
    return x **2

y = square(3)
print(y)
print()

def power(exponent, base):
    return base ** exponent

print(power(2,3))
print(power(exponent=2, base=3))
print(power(base=3, exponent=2))
print(power(2, base=3))
# błąd składni!!!! print(power(base=3, 2))