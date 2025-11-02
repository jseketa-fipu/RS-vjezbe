Vježba 5: Analiziraj sljedeće for petlje

Pojasnite zašto sljedeća petlja nema (previše) smisla:

#  samo jedna iteracija
for i in range(1, 2):
  print(i)

Što će ispisati sljedeća petlja?
range prima sljedece argumente:
class range(
    __start: SupportsIndex,
    __stop: SupportsIndex,
    __step: SupportsIndex = ...,
    /
Start index je manji od stop indexa, petlja se nece izvrsiti
for i in range(10, 1, 2):
  print(i)

Što će ispisati sljedeća petlja?
Petlja broji unatrag, start = 10, stop = 1, step = -1 (umanjuje start index dok
 ne dostigne stop index)
for i in range(10, 1, -1):
  print(i)

10
9
8
7
6
5
4
3
2