class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self) -> float:
        return self.shares * self.price
    def __repr__(self) -> str:
        return f"{self.name} : {self.shares} shares at {self.price}"