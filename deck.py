class Deck:
    # creates 52 card deck as ints [0, 51]
    @staticmethod
    def deck() -> set:
        return {i for i in range(52)}

    # creates 52 card deck with unicode cards
    @staticmethod
    def deck_unicode_card() -> set:
        s = set()
        suit = '🂡🂱🃁🃑'
        for i in range(13):
            for j in suit:
                s.add(chr(ord(j)+i))
                print(chr(ord(j)+i))
        return s

    # helper for string and unicode_suite methods
    @staticmethod
    def __deck_help(card: list[str], suit: list[str]) -> set:
        s = set()
        for i in card:
            for j in suit:
                s.add(i + " " + j)
        return s

    # creates 52 card deck as strings
    @staticmethod
    def deck_string() -> set:
        card = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        suit = ["Spade", "Heart", "Diamond", "Clubs"]
        return Deck.__deck_help(card, suit)

    # creates 52 card deck with string names and unicode suits
    @staticmethod
    def deck_unicode_suit() -> set:
        card = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        suit = "♠♥♦♣"
        return Deck.__deck_help(card, suit)

if __name__ == '__main__':
    d = Deck.deck()
    print(d, len(d))
    print('-' * 80)
    d = Deck.deck_string()
    print(d, len(d))
    print('-' * 80)
    d = Deck.deck_unicode_suit()
    print(d, len(d))
    print('-' * 80)
    d = Deck.deck_unicode_card()
    print(d, len(d))
