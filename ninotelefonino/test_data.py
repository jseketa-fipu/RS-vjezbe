import pytest

import ninotelefonino as nt

# test data
test_cases = [
    # --- Mobile (valid) ---
    {
        "input": "091 721 7633",
        "expected": {
            "pozivni_broj": "091",
            "broj_ostatak": "7217633",
            "vrsta": "Mobilna mreža",
            "mjesto": None,
            "operater": "A1 Hrvatska",
            "validan": True,
        },
    },
    {
        "input": "+385 91 721 7633",
        "expected": {
            "pozivni_broj": "091",
            "broj_ostatak": "7217633",
            "vrsta": "Mobilna mreža",
            "mjesto": None,
            "operater": "A1 Hrvatska",
            "validan": True,
        },
    },
    {
        "input": "00385 91 721 7633",
        "expected": {
            "pozivni_broj": "091",
            "broj_ostatak": "7217633",
            "vrsta": "Mobilna mreža",
            "mjesto": None,
            "operater": "A1 Hrvatska",
            "validan": True,
        },
    },
    {
        "input": "(385)917217633",
        "expected": {
            "pozivni_broj": "091",
            "broj_ostatak": "7217633",
            "vrsta": "Mobilna mreža",
            "mjesto": None,
            "operater": "A1 Hrvatska",
            "validan": True,
        },
    },
    {
        "input": "098 123 4567",
        "expected": {
            "pozivni_broj": "098",
            "broj_ostatak": "1234567",
            "vrsta": "Mobilna mreža",
            "mjesto": None,
            "operater": "Hrvatski Telekom",
            "validan": True,
        },
    },
    {
        "input": "099123456",
        "expected": {
            "pozivni_broj": "099",
            "broj_ostatak": "123456",
            "vrsta": "Mobilna mreža",
            "mjesto": None,
            "operater": "Hrvatski Telekom",
            "validan": True,
        },
    },
    {
        "input": "095-765-4321",
        "expected": {
            "pozivni_broj": "095",
            "broj_ostatak": "7654321",
            "vrsta": "Mobilna mreža",
            "mjesto": None,
            "operater": "Telemach",
            "validan": True,
        },
    },
    {
        "input": "092 123 456",
        "expected": {
            "pozivni_broj": "092",
            "broj_ostatak": "123456",
            "vrsta": "Mobilna mreža",
            "mjesto": None,
            "operater": "Tomato",
            "validan": True,
        },
    },
    {
        "input": "0971234567",
        "expected": {
            "pozivni_broj": "097",
            "broj_ostatak": "1234567",
            "vrsta": "Mobilna mreža",
            "mjesto": None,
            "operater": "bonbon",
            "validan": True,
        },
    },
    # --- Fixed line (valid) ---
    {
        "input": "01 234 5678",
        "expected": {
            "pozivni_broj": "01",
            "broj_ostatak": "2345678",
            "vrsta": "Fiksna mreža",
            "mjesto": "Grad Zagreb i Zagrebačka županija",
            "operater": None,
            "validan": True,
        },
    },
    {
        "input": "051-123-456",
        "expected": {
            "pozivni_broj": "051",
            "broj_ostatak": "123456",
            "vrsta": "Fiksna mreža",
            "mjesto": "Primorsko-goranska županija",
            "operater": None,
            "validan": True,
        },
    },
    {
        "input": "0521234567",
        "expected": {
            "pozivni_broj": "052",
            "broj_ostatak": "1234567",
            "vrsta": "Fiksna mreža",
            "mjesto": "Istarska županija",
            "operater": None,
            "validan": True,
        },
    },
    {
        "input": "020 123456",
        "expected": {
            "pozivni_broj": "020",
            "broj_ostatak": "123456",
            "vrsta": "Fiksna mreža",
            "mjesto": "Dubrovačko-neretvanska županija",
            "operater": None,
            "validan": True,
        },
    },
    {
        "input": "(385)51 123 456",
        "expected": {
            "pozivni_broj": "051",
            "broj_ostatak": "123456",
            "vrsta": "Fiksna mreža",
            "mjesto": "Primorsko-goranska županija",
            "operater": None,
            "validan": True,
        },
    },
    # --- Special services (valid) ---
    {
        "input": "0800 123456",
        "expected": {
            "pozivni_broj": "0800",
            "broj_ostatak": "123456",
            "vrsta": "Posebne usluge",
            "mjesto": None,
            "operater": None,
            "validan": True,
        },
    },
    {
        "input": "060123456",
        "expected": {
            "pozivni_broj": "060",
            "broj_ostatak": "123456",
            "vrsta": "Posebne usluge",
            "mjesto": None,
            "operater": None,
            "validan": True,
        },
    },
    {
        "input": "072123456",
        "expected": {
            "pozivni_broj": "072",
            "broj_ostatak": "123456",
            "vrsta": "Posebne usluge",
            "mjesto": None,
            "operater": None,
            "validan": True,
        },
    },
    # --- International/edge (valid) ---
    {
        "input": "385917217633",
        "expected": {
            "pozivni_broj": "091",
            "broj_ostatak": "7217633",
            "vrsta": "Mobilna mreža",
            "mjesto": None,
            "operater": "A1 Hrvatska",
            "validan": True,
        },
    },
    {
        "input": "+385981234567",
        "expected": {
            "pozivni_broj": "098",
            "broj_ostatak": "1234567",
            "vrsta": "Mobilna mreža",
            "mjesto": None,
            "operater": "Hrvatski Telekom",
            "validan": True,
        },
    },
    {
        "input": "00385(0)91 721 7633",
        "expected": {
            "pozivni_broj": "091",
            "broj_ostatak": "7217633",
            "vrsta": "Mobilna mreža",
            "mjesto": None,
            "operater": "A1 Hrvatska",
            "validan": True,
        },
    },
    # --- Invalid: wrong country / unknown prefix ---
    {
        "input": "+386 40 123 456",
        "expected": {
            "pozivni_broj": None,
            "broj_ostatak": None,
            "vrsta": None,
            "mjesto": None,
            "operater": None,
            "validan": False,
        },
    },
    {
        "input": "071123456",
        "expected": {
            "pozivni_broj": None,
            "broj_ostatak": None,
            "vrsta": None,
            "mjesto": None,
            "operater": None,
            "validan": False,
        },
    },
    # highly doubtful - what to do with numbers without leading zero?
    {
        "input": "91 721 7633",  # missing leading 0 and no 385
        "expected": {
            "pozivni_broj": "091",
            "broj_ostatak": "7217633",
            "vrsta": "Mobilna mreža",
            "mjesto": None,
            "operater": "A1 Hrvatska",
            "validan": True,
        },
    },
    # --- Invalid: bad lengths (prefix can still be determined) ---
    {
        "input": "091 12345",  # too short mobile
        "expected": {
            "pozivni_broj": "091",
            "broj_ostatak": "12345",
            "vrsta": "Mobilna mreža",
            "mjesto": None,
            "operater": "A1 Hrvatska",
            "validan": False,
        },
    },
    {
        "input": "091 12345678",  # too long mobile
        "expected": {
            "pozivni_broj": "091",
            "broj_ostatak": "12345678",
            "vrsta": "Mobilna mreža",
            "mjesto": None,
            "operater": "A1 Hrvatska",
            "validan": False,
        },
    },
    {
        "input": "0800 12345",  # too short special
        "expected": {
            "pozivni_broj": "0800",
            "broj_ostatak": "12345",
            "vrsta": "Posebne usluge",
            "mjesto": None,
            "operater": None,
            "validan": False,
        },
    },
    {
        "input": "0800 1234567",  # too long special
        "expected": {
            "pozivni_broj": "0800",
            "broj_ostatak": "1234567",
            "vrsta": "Posebne usluge",
            "mjesto": None,
            "operater": None,
            "validan": False,
        },
    },
    {
        "input": "(385)05112345",  # fixed too short
        "expected": {
            "pozivni_broj": "051",
            "broj_ostatak": "12345",
            "vrsta": "Fiksna mreža",
            "mjesto": "Primorsko-goranska županija",
            "operater": None,
            "validan": False,
        },
    },
    {
        "input": "(385)05112345678",  # fixed too long
        "expected": {
            "pozivni_broj": "051",
            "broj_ostatak": "12345678",
            "vrsta": "Fiksna mreža",
            "mjesto": "Primorsko-goranska županija",
            "operater": None,
            "validan": False,
        },
    },
    # --- Invalid: junk ---
    {
        "input": "abc",
        "expected": {
            "pozivni_broj": None,
            "broj_ostatak": None,
            "vrsta": None,
            "mjesto": None,
            "operater": None,
            "validan": False,
        },
    },
    {
        "input": "",
        "expected": {
            "pozivni_broj": None,
            "broj_ostatak": None,
            "vrsta": None,
            "mjesto": None,
            "operater": None,
            "validan": False,
        },
    },
    {
        "input": "   095 12A 345",
        "expected": {
            "pozivni_broj": "095",
            "broj_ostatak": "12A345",  # non-digit → overall invalid; your cleaner may strip or keep letters
            "vrsta": "Mobilna mreža",
            "mjesto": None,
            "operater": "Telemach",
            "validan": False,
        },
    },
]


@pytest.mark.parametrize("case", test_cases, ids=lambda c: c["input"])
def test_cleanup_number(case):

    assert case["expected"] == nt.validate_and_identify_number(
        nt.cleanup_number(case["input"])
    )
