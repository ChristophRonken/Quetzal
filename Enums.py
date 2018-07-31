from enum import Enum, auto


class ChocolateShotType(Enum):
    milk = auto()
    white = auto()
    dark = auto()
    brown = auto()


class HashTableType(Enum):
    Linear = auto()
    Quadratic = auto()
    Seperate = auto()


class OrderStates(Enum):
    NotOrdered = auto()
    NewOrder = auto()
    WaitingOrder = auto()
    BeingMade = auto()
    Finished = auto()
    PickedUp = auto()

