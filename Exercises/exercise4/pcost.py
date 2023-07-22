import os

def portfolio_cost(file: str) -> float:
    cost = 0
    with open(file, 'r') as f:
        while line := f.readline():
            s = line.split()
            try:
                cost += int(s[1]) * float(s[2])
            except ValueError as v:
                print(f"Couldn't parse: '{line.strip()}'")
                print(f"Reason: {v}")
    return cost

if __name__ == '__main__':
    dat = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', 'Data', 'portfolio.dat'))
    print(portfolio_cost(dat))