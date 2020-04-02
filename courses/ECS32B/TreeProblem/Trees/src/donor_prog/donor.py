class Donor(object):
    """
    Maybe it would be a good idea to a make a simple donor class
    """
    def __init__(self, name : int, amount : int) -> None:
        self.name = name
        self.amount = amount

    def __str__(self) -> str:
        return f'{self.name}  with a donation of {self.amount}'


