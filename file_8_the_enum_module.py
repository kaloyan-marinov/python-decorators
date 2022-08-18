"""
This file is _temporarily_ added to this repository,
the file does not fit in the name of the repository.

This file is based on the following video tutorials:
- Enums in Python are SO useful
- Learn Enum in Object-oriented Python 
- Enums in Python | Python Tutorial
"""

from enum import Enum, auto


class State(Enum):
    PLAYING = auto()
    PAUSED = auto()
    GAME_OVER = auto()


class Suit(Enum):
    CLUBS = "CLUBS"
    DIAMONDS = "DIAMONDS"
    HEARTS = "HEARTS"
    SPADE = "SPADE"


if __name__ == "__main__":
    print()
    print(f"{State.PLAYING = }")  # State.PLAYING = <State.PLAYING: 1>
    print(f"{State.PLAYING.value = }")  # State.PLAYING.value = 1
    print(f"{type(State.PLAYING) = }")  # type(State.PLAYING) = <enum 'State'>

    print()
    hearts = Suit.HEARTS
    print(f"{(hearts == Suit.HEARTS,) = }")  # (hearts == Suit.HEARTS,) = (True,)
    print(f"{(hearts is Suit.HEARTS,) = }")  # (hearts is Suit.HEARTS,) = (True,)
    try:
        Suit.HEARTS = "not HEARTS"
    except AttributeError:
        print("Cannot reassign members.")  # Cannot reassign members.
    print(f"{Suit('HEARTS') = }")  # Suit('HEARTS') = <Suit.HEARTS: 'HEARTS'>
