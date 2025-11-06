# Combined READMEs

## ninotelefonino

# Raspodijeljeni sustavi: Zadatak za vježbu - 31. 10. 2025.

## Zadatak: Nino Telefonino

<img src="https://raw.githubusercontent.com/lukablaskovic/FIPU-PJS/main/0.%20Template/FIPU_UNIPU.png" style="width:20%; box-shadow: none !important; float:left;"></img>

### Tekst zadatka

Ima jedan Nino kemu rabi novi telefonino. E ben, zato: Definiraj Python funkciju `validiraj_broj_telefona(broj: str)` koja očekuje broj telefona kao ulazni parametar te vraća rječnik sa sljedećim ključevima:

```python
{
"pozivni_broj": pogledati tablicu (str),
"broj_ostatak": ostatak broja (str),
"vrsta": "fiksna mreža" ili "mobilna mreža" ili "posebne usluge" (str),
"mjesto" : pogledati tablicu (str),
"operater": pogledati tablicu (str),
"validan": True ili False (bool)
}
```

**Validacijska pravila:**

- Funkcija mora ispraviti `broj` tako da ukloni sve nepotrebne znakove (razmake, crtice, zagrade, random whitespace itd.) i provjeriti je li broj ispravan prema pravilima u nastavku.
- Pozivni broj mora biti jedan od onih navedenih u tablici ispod.
- Nakon pozivnog broja, `broj_ostatak` mora imati točno 6 ili 7 znamenki za fiksne mreže, 6 ili 7 znamenki za mobilne mreže te točno 6 znamenki za posebne usluge. `broj_ostatak` predstavlja pretplatnički dio broja (bez pozivnog broja).
- `broj` može počinjati s opcionalnim znakom `+`, `385` ili `00385`, ili pak varijante sa zagradama `(385)917217633` za međunarodne pozive; validacija to mora uzeti u obzir.
- Funkcija mora preslikati/mapirati `broj` na odgovarajuću `vrstu`, `mjesto` ili `operater` na temelju pozivnog broja.
- Ako je broj mobilan, `mjesto` postavite na `None`. Ako je broj posebne usluge, postavite `mjesto` i `operater` na `None`. Ako je broj fiksan, `operater` postavite na `None`.

Ako je broj valjan, postavite ključ `validan` na True i ispunite ostale ključeve prema tablici. Ako broj nije valjan, postavite `validan` na False te postavite samo one ključeve koje je moguće odrediti (npr. `pozivni_broj` i `broj_ostatak`).

**Još napomena:**

- Poželjno je definirati pomoćne funkcije za čišćenje i validaciju broja.

- Korisne metode: `str.replace()`, `str.startsWith()`, `str.isdigit()`, `len()`, `str.join()` (Google it).

- Zadatak probajte riješiti bez regularnih izraza (RegEx).

### Tablica pozivnih brojeva RH:

| Pozivni broj | Mjesto / Operater                                             | Vrsta          |
| ------------ | ------------------------------------------------------------- | -------------- |
| 01           | Grad Zagreb i Zagrebačka županija                             | Fiksna mreža   |
| 020          | Dubrovačko-neretvanska županija                               | Fiksna mreža   |
| 021          | Splitsko-dalmatinska županija                                 | Fiksna mreža   |
| 022          | Šibensko-kninska županija                                     | Fiksna mreža   |
| 023          | Zadarska županija                                             | Fiksna mreža   |
| 031          | Osječko-baranjska županija                                    | Fiksna mreža   |
| 032          | Vukovarsko-srijemska županija                                 | Fiksna mreža   |
| 033          | Virovitičko-podravska županija                                | Fiksna mreža   |
| 034          | Požeško-slavonska županija                                    | Fiksna mreža   |
| 035          | Brodsko-posavska županija                                     | Fiksna mreža   |
| 040          | Međimurska županija                                           | Fiksna mreža   |
| 042          | Varaždinska županija                                          | Fiksna mreža   |
| 043          | Bjelovarsko-bilogorska županija                               | Fiksna mreža   |
| 044          | Sisačko-moslavačka županija                                   | Fiksna mreža   |
| 047          | Karlovačka županija                                           | Fiksna mreža   |
| 048          | Koprivničko-križevačka županija                               | Fiksna mreža   |
| 049          | Krapinsko-zagorska županija                                   | Fiksna mreža   |
| 051          | Primorsko-goranska županija                                   | Fiksna mreža   |
| 052          | Istarska županija                                             | Fiksna mreža   |
| 053          | Ličko-senjska županija                                        | Fiksna mreža   |
| 091          | A1 Hrvatska                                                   | Mobilna mreža  |
| 092          | Tomato                                                        | Mobilna mreža  |
| 095          | Telemach                                                      | Mobilna mreža  |
| 097          | bonbon                                                        | Mobilna mreža  |
| 098, 099     | Hrvatski Telekom                                              | Mobilna mreža  |
| 0800         | Besplatni pozivi                                              | Posebne usluge |
| 060          | Komercijalni pozivi                                           | Posebne usluge |
| 061          | Glasovanje telefonom                                          | Posebne usluge |
| 064          | Usluge s neprimjerenim sadržajem                              | Posebne usluge |
| 065          | Nagradne igre                                                 | Posebne usluge |
| 069          | Usluge namijenjene djeci                                      | Posebne usluge |
| 072          | jedinstveni pristupni broj za cijelu državu za posebne usluge | Posebne usluge |

## vjezba 01

Vježba 1: Jednostavni kalkulator

Napišite program koji traži od korisnika unos dva broja (float) te jedan od operatora (+, -, *, /). Program treba ispisati rezultat operacije nad unesenim brojevima u formatu:

Rezultat operacije 5.0 + 3.0 je 8.0

Ako korisnik pokuša dijeljenje s nulom, program treba ispisati poruku:

Dijeljenje s nulom nije dozvoljeno!

Ako korisnik unese nepodržani operator, program treba ispisati poruku:

Nepodržani operator!

## vjezba 02

Vježba 2: Prijestupna godina

Napišite program koji traži unos godine i provjerava je li godina prijestupna. Godina je prijestupna ako:

    je djeljiva s 4, ali ne sa 100 ili
    godina je djeljiva sa 400

Ako godina zadovoljava ove uvjete, program treba ispisati poruku:

Godina ____. je prijestupna.

Ako godina nije prijestupna, program treba ispisati poruku:

Godina ____. nije prijestupna.

## vjezba 03

Vježba 3: Pogađanje broja sve dok nije pogođen

Implementirajte igru pogađanja broja u rasponu od 1 do 100. Korisnik unosi svoj pokušaj, a program nakon svakog unosa ispisuje poruku koja označava je li uneseni broj veći, manji ili jednak traženom broju. Igra traje dok korisnik ne pogodi točan broj.

    Za izlazak iz igre koristite pomoćnu bool varijablu broj_je_pogoden.

    Na kraju ispišite korisniku poruku: "Bravo, pogodio si u __ pokušaja".

## vjezba 04

Vježba 4: Zbrajanje unesenih brojeva
Napišite program koji traži od korisnika unos cijelih brojeva sve dok korisnik ne unese broj 0. Nakon unosa 0, program treba ispisati zbroj svih prethodno unesenih brojeva.

## vjezba 05

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

## vjezba 06

Vježba 6: Krenimo "petljati"

    Napišite program koji ispisuje sumu svih parnih brojeva od 1 do 100 (uključivo).

    Napišite program koji ispisuje prvih 10 neparnih brojeva u obrnutom redoslijedu.

    Napišite program koji ispisuje Fibonaccijev niz do 1000. Fibonaccijev niz počinje s brojevima 0 i 1, a svaki sljedeći broj je zbroj prethodna dva broja.

Svaki zadatak riješite for i while petljom.

## vjezba 07

Vježba 7: Validacija i provjera jakosti lozinke

Napišite program koji traži od korisnika da unese lozinku. Lozinka mora zadovoljavati sljedeće uvjete:

    ako duljina lozinke nije između 8 i 15 znakova, ispišite poruku "Lozinka mora sadržavati između 8 i 15 znakova".
    ako lozinka ne sadrži barem jedno veliko slovo i jedan broj, ispišite "Lozinka mora sadržavati barem jedno veliko slovo i jedan broj"
    ako lozinka sadrži riječ "password" ili "lozinka" (bez obzira na velika i mala slova), ispišite: "Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'"
    ako lozinka zadovoljava sve uvjete, ispišite "Lozinka je jaka!"

Metode za normalizaciju stringova: lower(), upper(), islower(), isupper().

Provjera je li znakovni niz broj: isdigit()

Kod za provjeru dodajte u funkciju provjera_lozinke(lozinka).

## vjezba 08

Vježba 8: Filtriranje parnih iz liste

Napišite funkciju koja prima listu cijelih brojeva i vraća novu lista koja sadrži samo parne brojeve iz originalne liste.

Primjer:

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(filtriraj_parne(lista)) # [2, 4, 6, 8, 10]

## vjezba 09

Vježba 9: Uklanjanje duplikata iz liste

Napišite funkciju koja prima listu i vraća novu listu koja ne sadrži duplikate. Implementaciju odradite pomoćnim skupom.

Primjer:

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

print(ukloni_duplikate(lista)) # [1, 2, 3, 4, 5]

## vjezba 10

Vježba 10: Brojanje riječi u tekstu

Napišite funkciju koja broji koliko se puta svaka riječ pojavljuje u tekstu (frekvencija riječi) i vraća rječnik s rezultatima.

Primjer:

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

print(brojanje_riječi(tekst))

# {'Python': 2, 'je': 3, 'programski': 1, 'jezik': 1, 'koji': 1, 'jednostavan': 1, 'za': 1, 'učenje': 1, 'i': 1, 'korištenje.': 1, 'vrlo': 1, 'popularan.': 1}

## vjezba 11

Vježba 11: Grupiranje elemenata po paritetu

Napišite funkciju koja prima listu brojeva i vraća rječnik s dvije liste: jedna za parne brojeve, a druga za neparne brojeve.

Primjer:

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(grupiraj_po_paritetu(lista))

# {'parni': [2, 4, 6, 8, 10], 'neparni': [1, 3, 5, 7, 9]}

## vjezba 12

Vježba 12: Obrnite rječnik

Napišite funkciju koja prima rječnik i vraća novi rječnik u kojem su ključevi i vrijednosti zamijenjeni.

Primjer:

rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

print(obrni_rjecnik(rjecnik))

# {'Ivan': 'ime', 'Ivić': 'prezime', 25: 'dob'}

## vjezba 13

Vježba 13: Napišite sljedeće funkcije:

    Funkcija koja vraća n-torku s prvim i zadnjim elementom liste u jednoj liniji koda.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(prvi_i_zadnji(lista)) # (1, 10)

    Funkcija koja vraća n-torku s maksimalnim i minimalnim elementom liste, bez korištenja ugrađenih funkcija max() i min().

lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]

print(maks_i_min(lista)) # (250, 5)

    Funkcija presjek koja prima dva skupa i vraća novi skup s elementima koji se nalaze u oba skupa.

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}

print(presjek(skup_1, skup_2)) # {4, 5}

## vjezba 14

Vježba 14: Prosti brojevi

    Napišite funkciju isPrime() koja prima cijeli broj i vraća True ako je broj prost, a False ako nije. Prost broj je prirodan broj veći od 1 koji je dijeljiv jedino s 1 i samim sobom.

Primjer:

print(isPrime(7)) # True
print(isPrime(10)) # False

    Napišite funkciju primes_in_range() koja prima dva argumenta: start i end i vraća listu svih prostih brojeva u tom rasponu.

Primjer:

print(primes_in_range(1, 10)) # [2, 3, 5, 7]

## vjezba 15

Vježba 15: Pobroji samoglasnike i suglasnike

Napišite funkciju count_vowels_consonants() koja prima string i vraća rječnik s brojem samoglasnika i brojem suglasnika u tekstu.

vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

Primjer:

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

print(count_vowels_consonants(tekst))

# {'vowels': 30, 'consonants': 48}

## vjezba 16

Vježba 16: Implementacija Dijsktra algoritma za pronalaženje najkraćeg puta

Napišite funkciju dijkstra(graph, start) koja prima graf predstavljen kao rječnik susjedstva i početni čvor te vraća rječnik s najkraćim udaljenostima od početnog čvora do svih ostalih čvorova u grafu koristeći Dijsktra algoritam.

Za rješavanje zadatka možete koristiti modul heapq za gotovu implementaciju prioritetnog reda.

Primjer ulaznih podataka

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

Primjer poziva funkcije:

print(dijkstra(graph, 'A'))
# {'A': 0, 'B': 1, 'C': 3, D': 4}

