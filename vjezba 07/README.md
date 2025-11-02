Vježba 7: Validacija i provjera jakosti lozinke

Napišite program koji traži od korisnika da unese lozinku. Lozinka mora zadovoljavati sljedeće uvjete:

    ako duljina lozinke nije između 8 i 15 znakova, ispišite poruku "Lozinka mora sadržavati između 8 i 15 znakova".
    ako lozinka ne sadrži barem jedno veliko slovo i jedan broj, ispišite "Lozinka mora sadržavati barem jedno veliko slovo i jedan broj"
    ako lozinka sadrži riječ "password" ili "lozinka" (bez obzira na velika i mala slova), ispišite: "Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'"
    ako lozinka zadovoljava sve uvjete, ispišite "Lozinka je jaka!"

Metode za normalizaciju stringova: lower(), upper(), islower(), isupper().

Provjera je li znakovni niz broj: isdigit()

Kod za provjeru dodajte u funkciju provjera_lozinke(lozinka).