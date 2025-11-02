# Vježba 8: Filtriranje parnih iz liste

# Napišite funkciju koja prima listu cijelih brojeva i vraća novu lista koja sadrži samo parne brojeve iz originalne liste.

# Primjer:

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(filtriraj_parne(lista)) # [2, 4, 6, 8, 10]


def filtriraj_parne(original_list: list[int]) -> list[int]:
    filtered_list = [n for n in original_list if n % 2 == 0]

    return filtered_list


lista: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(filtriraj_parne(lista))
