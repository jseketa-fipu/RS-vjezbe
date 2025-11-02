# Vježba 6: Krenimo "petljati"

#     Napišite program koji ispisuje sumu svih parnih brojeva od 1 do 100 (uključivo).

#     Napišite program koji ispisuje prvih 10 neparnih brojeva u obrnutom redoslijedu.

#     Napišite program koji ispisuje Fibonaccijev niz do 1000. Fibonaccijev niz počinje s brojevima 0 i 1, a svaki sljedeći broj je zbroj prethodna dva broja.

# Svaki zadatak riješite for i while petljom.

# Napišite program koji ispisuje sumu svih parnih brojeva od 1 do 100 (uključivo).
# for petlja
list_even_numbers_for_loop: list = []
for i in range(1, 101, 1):
    if i % 2 == 0:
        list_even_numbers_for_loop.append(i)

print(
    f"Suma svih parnih brojeva izmedu 1 i 100 (for petlja): {sum(list_even_numbers_for_loop)}"
)

# while petlja
list_even_numbers_while_loop: list = []
i = 0
while True:
    if i > 100:
        break
    if i % 2 == 0:
        list_even_numbers_while_loop.append(i)
    i = i + 1

print(
    f"Suma svih parnih brojeva izmedu 1 i 100 (while petlja): {sum(list_even_numbers_while_loop)}"
)

# Napišite program koji ispisuje prvih 10 neparnih brojeva u obrnutom redoslijedu.
# for petlja
list_odd_numbers_for_loop: list = []
for i in range(100, 1, -1):
    if i % 2 != 0:
        list_odd_numbers_for_loop.append(i)
    if len(list_odd_numbers_for_loop) == 10:
        break

# enumerate is useful for obtaining an indexed list:
# list of integers is a non-iterable object
# index is to be started at 1, so it can be used in a formatted string
for i, number in enumerate(list_odd_numbers_for_loop, start=1):
    print(f"{i}. neparni broj je: {number}")

# Napišite program koji ispisuje prvih 10 neparnih brojeva u obrnutom redoslijedu.
# while petlja
list_odd_numbers_while_loop: list = []
number_needed = 10
total_needed = number_needed
start = 100
while number_needed:
    if start % 2 != 0:
        index = total_needed - number_needed + 1
        print(f"{index}. neparni broj je: {start}")
        number_needed = number_needed - 1
    start = start - 1


# Napišite program koji ispisuje Fibonaccijev niz do 1000.
# Fibonaccijev niz počinje s brojevima 0 i 1,
# a svaki sljedeći broj je zbroj prethodna dva broja.
# for petlja
# for petlja
a, b = 0, 1
sequence_for_loop: list[int] = []

# Any large upper bound works; we break when a > 1000
for _ in range(1000):
    if a > 1000:
        break
    sequence_for_loop.append(a)
    a, b = b, a + b

print(f"Fibonacci niz do 1000 je: {', '.join(map(str, sequence_for_loop))}")


# while petlja
# start condition a = 0, b = 1
a, b = 0, 1
sequence_while_loop: list = []
while a <= 1000:
    sequence_while_loop.append(a)
    a, b = b, a + b

# unpack operator * is not allowed in the formatted string
# wrong output, empty first element
# Fibonacci niz do 1000 je: , 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987
# That leading comma comes from sep=", " being inserted between the header string and the first number:
print(f"Fibonacci niz do 1000 je: {', '.join(map(str, sequence_while_loop))}")
