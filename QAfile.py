a = range(6)
for x in a:
    print(x)

b = "Памагітє"
print(b)

def check_even(c, d="Всьо очєнь плоха"):
    if c % 2 == 0:
        return float(c)
    else:
        return d

result = check_even(10)
result1 = check_even(11)
result2 = check_even(12)
print(result, result1, result2)
print("Памагітє")
