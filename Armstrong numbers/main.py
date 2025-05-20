number = int(input(""))

def armstrong(n):
    num = str(n)
    sum_of_digit = 0

    for digit in num:
        sum_of_digit += (int(digit))**(len(num))

    return sum_of_digit

armstrong_number = []
i = 1
while len(armstrong_number) < number:
    if i == armstrong(i):
        armstrong_number.append(i)
    i += 1

print(armstrong_number)