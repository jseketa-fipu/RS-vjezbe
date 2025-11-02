# Vježba 15: Pobroji samoglasnike i suglasnike

# Napišite funkciju count_vowels_consonants() koja prima string i vraća rječnik s brojem samoglasnika i brojem suglasnika u tekstu.

# vowels = "aeiouAEIOU"
# consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

# Primjer:

# tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

# print(count_vowels_consonants(tekst))

# # {'vowels': 30, 'consonants': 48}


def count_vowels_consonants(text: str) -> dict[str, int]:
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    counts = {"vowels": 0, "consonants": 0}

    for character in text:
        if character in vowels:
            counts["vowels"] += 1
        elif character in consonants:
            counts["consonants"] += 1

    return counts


text = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

print(count_vowels_consonants(text))
