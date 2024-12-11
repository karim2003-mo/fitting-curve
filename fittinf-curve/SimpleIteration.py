class SimpleIteration:
    def __init__(self, g, initial_guess, tolerance=1e-7, max_iterations=1000):
        self.g = g
        self.x = initial_guess
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def iterate(self):
        for i in range(self.max_iterations):
            x_new = self.g(self.x)
            if abs(x_new - self.x) < self.tolerance:
                print(f"Converged to {x_new} after {i+1} iterations.")
                return x_new
            self.x = x_new
        print("Did not converge within the maximum number of iterations.")
        return None

# Example usage
if __name__ == "__main__":
    g = lambda x: (x**2 + 2) / 3

    initial_guess = 2.0
    solver = SimpleIteration(g, initial_guess)

    root = solver.iterate()
    if root is not None:
        print(f"Root found: {root}")
