'''
14,047,378,800 possible combinations of 4 cards 2 discards 1 draw
generating the combinations becomes a little impractical.

This should not be used... Only keeping for notes/reminder.
'''

# for combination
import math
# for combination generation
from itertools import combinations

from deck import Deck

class CardCombos:
    # returns a set of tuples
    # (4 cards kept, 2 cards crib, turned over)
    @staticmethod
    def generate(deck: set) -> set:
        hands = set()
        for d4 in {i for i in combinations(deck, 4)}:
            remain = deck - set(d4)
            for d2 in {i for i in combinations(remain, 2)}:
                for d in remain - set(d2):
                    hands.add((d4, d2, d))
        return hands

    @staticmethod
    def generate_file(deck: set, file) -> int:
        c = 0
        e = 52 * math.comb(51,2) * math.comb(49,4)
        p = e // 1000
        for d in deck:
            remain = deck - {d}
            for d2 in {i for i in combinations(remain, 2)}:
                for d4 in {i for i in combinations(remain - set(d2), 4)}:
                    print(d4, d2, d, file=file)
                    c += 1
                    p -= 1
                    if p == 0:
                        print(c // e * 100)
                        p = e // 1000
        return c

if __name__ == '__main__':
    # https://docs.python.org/3/library/argparse.html
    import argparse
    import sys

    msg = "Generate all possible hands for Cribbage."

    parser = argparse.ArgumentParser(description = msg)
    parser.add_argument(
        "-f", "--file",
        help = "File to output card combinations",
        # type=ascii
    )
    
    # def output(cc: list[tuple], f = sys.stdout) -> None:
    #     for c in cc:
    #         print(c, file = f)

    args = parser.parse_args()
    with open(args.file, 'w') as file:
        c = CardCombos.generate_file(Deck.deck(), file)
        print(c, "Hand, Flip, Discard", file = file)
        print(c, "Hand, Flip, Discard")

    # if args.file:
    #     print("Outputting to:", args.file)
    #     with open(args.file, 'w') as file:
    #         g = CardCombos.generate(Deck.deck())
    #         print(len(g), "possible combinations (hand, crib, turn)", file=file)
    #         output(g, file)
    # else:
    #     g = CardCombos.generate(Deck.deck())
    #     print(len(g), "possible combinations (hand, crib, turn)")
    #     output(g)