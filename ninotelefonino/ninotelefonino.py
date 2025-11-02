import pytest

PREFIX_MAP = {
    # Fiksna mreža
    "01": {
        "mjesto_operater": "Grad Zagreb i Zagrebačka županija",
        "vrsta": "Fiksna mreža",
    },
    "020": {
        "mjesto_operater": "Dubrovačko-neretvanska županija",
        "vrsta": "Fiksna mreža",
    },
    "021": {
        "mjesto_operater": "Splitsko-dalmatinska županija",
        "vrsta": "Fiksna mreža",
    },
    "022": {"mjesto_operater": "Šibensko-kninska županija", "vrsta": "Fiksna mreža"},
    "023": {"mjesto_operater": "Zadarska županija", "vrsta": "Fiksna mreža"},
    "031": {"mjesto_operater": "Osječko-baranjska županija", "vrsta": "Fiksna mreža"},
    "032": {
        "mjesto_operater": "Vukovarsko-srijemska županija",
        "vrsta": "Fiksna mreža",
    },
    "033": {
        "mjesto_operater": "Virovitičko-podravska županija",
        "vrsta": "Fiksna mreža",
    },
    "034": {"mjesto_operater": "Požeško-slavonska županija", "vrsta": "Fiksna mreža"},
    "035": {"mjesto_operater": "Brodsko-posavska županija", "vrsta": "Fiksna mreža"},
    "040": {"mjesto_operater": "Međimurska županija", "vrsta": "Fiksna mreža"},
    "042": {"mjesto_operater": "Varaždinska županija", "vrsta": "Fiksna mreža"},
    "043": {
        "mjesto_operater": "Bjelovarsko-bilogorska županija",
        "vrsta": "Fiksna mreža",
    },
    "044": {"mjesto_operater": "Sisačko-moslavačka županija", "vrsta": "Fiksna mreža"},
    "047": {"mjesto_operater": "Karlovačka županija", "vrsta": "Fiksna mreža"},
    "048": {
        "mjesto_operater": "Koprivničko-križevačka županija",
        "vrsta": "Fiksna mreža",
    },
    "049": {"mjesto_operater": "Krapinsko-zagorska županija", "vrsta": "Fiksna mreža"},
    "051": {"mjesto_operater": "Primorsko-goranska županija", "vrsta": "Fiksna mreža"},
    "052": {"mjesto_operater": "Istarska županija", "vrsta": "Fiksna mreža"},
    "053": {"mjesto_operater": "Ličko-senjska županija", "vrsta": "Fiksna mreža"},
    # Mobilna mreža
    "091": {"mjesto_operater": "A1 Hrvatska", "vrsta": "Mobilna mreža"},
    "092": {"mjesto_operater": "Tomato", "vrsta": "Mobilna mreža"},
    "095": {"mjesto_operater": "Telemach", "vrsta": "Mobilna mreža"},
    "097": {"mjesto_operater": "bonbon", "vrsta": "Mobilna mreža"},
    "098": {"mjesto_operater": "Hrvatski Telekom", "vrsta": "Mobilna mreža"},
    "099": {"mjesto_operater": "Hrvatski Telekom", "vrsta": "Mobilna mreža"},
    # Posebne usluge
    "0800": {"mjesto_operater": "Besplatni pozivi", "vrsta": "Posebne usluge"},
    "060": {"mjesto_operater": "Komercijalni pozivi", "vrsta": "Posebne usluge"},
    "061": {"mjesto_operater": "Glasovanje telefonom", "vrsta": "Posebne usluge"},
    "064": {
        "mjesto_operater": "Usluge s neprimjerenim sadržajem",
        "vrsta": "Posebne usluge",
    },
    "065": {"mjesto_operater": "Nagradne igre", "vrsta": "Posebne usluge"},
    "069": {"mjesto_operater": "Usluge namijenjene djeci", "vrsta": "Posebne usluge"},
    "072": {
        "mjesto_operater": "jedinstveni pristupni broj za cijelu državu za posebne usluge",
        "vrsta": "Posebne usluge",
    },
}


test_cases = [
    # --- Mobile (valid formats) ---
    {"input": "091 721 7633", "valid": True, "expected": "0917217633"},
    {"input": "+385 91 721 7633", "valid": True, "expected": "0917217633"},
    {"input": "00385 91 721 7633", "valid": True, "expected": "0917217633"},
    {"input": "(385)917217633", "valid": True, "expected": "0917217633"},
    {"input": "098 123 4567", "valid": True, "expected": "0981234567"},
    {"input": "099123456", "valid": True, "expected": "099123456"},
    {"input": "095-765-4321", "valid": True, "expected": "0957654321"},
    {"input": "092 123 456", "valid": True, "expected": "092123456"},
    {"input": "0971234567", "valid": True, "expected": "0971234567"},
    # --- Fixed line (valid formats) ---
    {"input": "01 234 5678", "valid": True, "expected": "012345678"},
    {"input": "051-123-456", "valid": True, "expected": "051123456"},
    {"input": "0521234567", "valid": True, "expected": "0521234567"},
    {"input": "020 123456", "valid": True, "expected": "020123456"},
    {"input": "(385)51 123 456", "valid": True, "expected": "051123456"},
    # --- Special services (valid formats) ---
    {"input": "0800 123456", "valid": True, "expected": "0800123456"},
    {"input": "060123456", "valid": True, "expected": "060123456"},
    {"input": "061123456", "valid": True, "expected": "061123456"},
    {"input": "064123456", "valid": True, "expected": "064123456"},
    {"input": "065123456", "valid": True, "expected": "065123456"},
    {"input": "069123456", "valid": True, "expected": "069123456"},
    {"input": "072123456", "valid": True, "expected": "072123456"},
    # --- International normalization edge cases (valid) ---
    {"input": "385917217633", "valid": True, "expected": "0917217633"},
    {"input": "+385981234567", "valid": True, "expected": "0981234567"},
    {"input": "00385(0)91 721 7633", "valid": True, "expected": "0917217633"},
    # --- Invalid: wrong prefix / country ---
    {"input": "+386 40 123 456", "valid": False, "expected": None},
    {"input": "071123456", "valid": False, "expected": None},
    {"input": "91 721 7633", "valid": False, "expected": None},
    # --- Invalid: bad lengths ---
    {"input": "091 12345", "valid": False, "expected": None},
    {"input": "091 12345678", "valid": False, "expected": None},
    {"input": "0800 12345", "valid": False, "expected": None},
    {"input": "0800 1234567", "valid": False, "expected": None},
    {"input": "(385)05112345", "valid": False, "expected": None},
    {"input": "(385)05112345678", "valid": False, "expected": None},
    # --- Invalid: non-digits / junk ---
    {"input": "abc", "valid": False, "expected": None},
    {"input": "", "valid": False, "expected": None},
    {"input": "   095 12A 345", "valid": False, "expected": None},
]


def cleanup_number(input: str) -> str:
    # remove leading and trailing whitespace
    clean = input.strip()
    # unwanted common characters
    unwanted: list[str] = [" ", "-", "/", ".", "(", ")"]
    # replace common characters from the string
    for character in unwanted:
        clean = clean.replace(character, "")

    # left strip zeroes and + sign
    clean = clean.lstrip("+0")

    # problem: 385 could be anywhere in the number
    # do not use lstrip for removing 385, because it will chain to other numbers
    # remove 3, remove 8, remove 5, then remove 5 again. 051 numbers affected
    clean = clean.removeprefix("385")
    # detect 385, remove everything before it,
    # then add 0 after it if it doesn't already exist
    # position = clean.find("385")

    # clean = clean[position + 3 :]
    # if the number doesn't start with 0, add one
    if not clean.startswith("0"):
        clean = "0" + clean

    return clean


def validate_and_identify_number(input: str) -> dict:
    return_dict: dict = {}
    for key in PREFIX_MAP.keys():
        if input.startswith(key):
            return_dict["pozivni_broj"] = key
            return_dict["broj_ostatka"] = input.removeprefix(key)
            return_dict["vrsta"] = PREFIX_MAP[key]["vrsta"]

            if PREFIX_MAP[key]["vrsta"] == "Fiksna mreža":
                return_dict["mjesto"] = PREFIX_MAP[key]["mjesto_operater"]
                return_dict["operater"] = None
            elif PREFIX_MAP[key]["vrsta"] == "Mobilna mreža":
                return_dict["mjesto"] = None
                return_dict["operater"] = PREFIX_MAP[key]["mjesto_operater"]
            elif PREFIX_MAP[key]["vrsta"] == "Posebne usluge":
                return_dict["mjesto"] = None
                return_dict["operater"] = None

    return return_dict


print(validate_and_identify_number(cleanup_number("(385)51 123 456")))
# for test, validity in test_cases:
#     print(f"Input: {test}, Valid: {validity}, result: {cleanup_number(test)}")


@pytest.mark.parametrize("case", test_cases, ids=lambda c: c["input"])
def test_cleanup_number(case):
    assert case["expected"] == cleanup_number(case["input"])
