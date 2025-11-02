import random


class NumberGuesser:
    # initialize the object with the number to be guessed and a counter set to 0
    def __init__(self, low: int, high: int) -> None:
        self.low = low
        self.high = high
        self.random_number = random.randint(self.low, self.high)
        self.number_of_tries = 0

    @property
    def get_secret_number(self) -> int:
        return self.random_number

    def increment_number_of_tries(self) -> None:
        self.number_of_tries = self.number_of_tries + 1

    def get_number_of_tries(self) -> int:
        return self.number_of_tries

    def validate(self, prompt: str) -> int:
        while True:
            s = input(prompt).strip()
            try:
                n = int(s)
            except ValueError:
                print("Unesi cijeli broj (npr. 42).")
                continue

            if not (self.low <= n <= self.high):
                print(f"Broj mora biti u rasponu {self.low}–{self.high}.")
                continue

            return n


def main() -> None:
    # generalized the instantiation of the object to accept any bounds
    pogodibroj = NumberGuesser(1, 100)

    while True:
        get_number = pogodibroj.validate("Unesi broj: ")

        if get_number < pogodibroj.get_secret_number:
            print("Uneseni broj je manji od trazenog.")
            pogodibroj.increment_number_of_tries()
        elif get_number > pogodibroj.get_secret_number:
            print("Uneseni broj je veci od trazenog.")
            pogodibroj.increment_number_of_tries()
        elif get_number == pogodibroj.get_secret_number:
            pogodibroj.increment_number_of_tries()
            print(f"Bravo, pogodio si u {pogodibroj.get_number_of_tries()} pokusaja.")
            break


if __name__ == "__main__":
    main()
