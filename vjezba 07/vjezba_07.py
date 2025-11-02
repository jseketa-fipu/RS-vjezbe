# Vježba 7: Validacija i provjera jakosti lozinke

# Napišite program koji traži od korisnika da unese lozinku. Lozinka mora zadovoljavati sljedeće uvjete:

#     ako duljina lozinke nije između 8 i 15 znakova, ispišite poruku "Lozinka mora sadržavati između 8 i 15 znakova".
#     ako lozinka ne sadrži barem jedno veliko slovo i jedan broj, ispišite "Lozinka mora sadržavati barem jedno veliko slovo i jedan broj"
#     ako lozinka sadrži riječ "password" ili "lozinka" (bez obzira na velika i mala slova), ispišite: "Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'"
#     ako lozinka zadovoljava sve uvjete, ispišite "Lozinka je jaka!"

# Metode za normalizaciju stringova: lower(), upper(), islower(), isupper().

# Provjera je li znakovni niz broj: isdigit()

# Kod za provjeru dodajte u funkciju provjera_lozinke(lozinka).

forbidden_words_list: list[str] = ["password", "lozinka"]


def check_forbidden_words(lozinka: str) -> bool:
    lower_case = lozinka.lower()
    return not any(word.lower() in lower_case for word in forbidden_words_list)


def provjera_lozinke(lozinka: str) -> None:
    # checks:
    # between 8 and 15 characters
    between_8_and_15_characters: bool = len(lozinka) >= 8 and len(lozinka) <= 15
    # at least one uppercase letter
    at_least_one_uppercase: bool = any(ch.isupper() for ch in lozinka)
    # at least one number
    at_least_one_number: bool = any(ch.isdigit() for ch in lozinka)
    # forbidden words
    forbidden_words: bool = check_forbidden_words(lozinka)

    if not between_8_and_15_characters:
        print("Lozinka mora sadržavati između 8 i 15 znakova")
    elif not at_least_one_uppercase or not at_least_one_number:
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
    elif not forbidden_words:
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
    else:
        print("Lozinka je jaka!")


if __name__ == "__main__":
    pw = input("Unesi lozinku: ").strip()
    provjera_lozinke(pw)
