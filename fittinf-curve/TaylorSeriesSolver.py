import numpy as np
class TaylorSeriesSolver:
    def __init__(self, f, df, x0, y0, h, n):
        self.f = f     # The function f(x, y)
        self.df = df   # The derivative function df(x, y, dy/dx)
        self.x0 = x0   # Initial x value
        self.y0 = y0   # Initial y value
        self.h = h     # Step size
        self.n = n     # Number of steps

    def solve(self):
        x = self.x0
        y = self.y0
        results = [(x, y)]
        
        for _ in range(self.n):
            y += self.h * self.f(x, y) + (self.h**2 / 2) * self.df(x, y, self.f(x, y))
            x += self.h
            results.append((x, y))
        
        return results

# Example usage
if __name__ == "__main__":
    f = lambda x, y: x + y
    df = lambda x, y, dydx: 1 + dydx
    x0 = 0
    y0 = 1
    h = 0.1
    n = 10
    solver = TaylorSeriesSolver(f, df, x0, y0, h, n)
    results = solver.solve()
    for x, y in results:
        print(f"x = {x:.2f}, y = {y:.4f}")
