import numpy as np
class ModifiedEuler:
    def __init__(self, f, x0, y0, h, n):
        self.f = f     # The function f(x, y)
        self.x0 = x0   # Initial x value
        self.y0 = y0   # Initial y value
        self.h = h     # Step size
        self.n = n     # Number of steps

    def solve(self):
        x = self.x0
        y = self.y0
        results = [(x, y)]
        
        for i in range(1, self.n + 1):
            k1 = self.h * self.f(x, y)
            k2 = self.h * self.f(x + self.h, y + k1)
            y += 0.5 * (k1 + k2)
            x += self.h
            results.append((x, y))
        
        return results

# Example usage
if __name__ == "__main__":
    f = lambda x, y: x * np.sqrt(y)
    x0 = 0
    y0 = 1
    h = 0.1
    n = 10
    solver = ModifiedEuler(f, x0, y0, h, n)
    results = solver.solve()
    for x, y in results:
        print(f"x = {x:.2f}, y = {y:.4f}")
