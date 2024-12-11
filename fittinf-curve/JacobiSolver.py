import numpy as np

class JacobiSolver:
    def __init__(self, A, b, tolerance=1e-10, max_iterations=1000):
        self.A = A
        self.b = b
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def solve(self):
        n = len(self.b)
        x = np.zeros_like(self.b, dtype=np.float64)
        x_new = np.zeros_like(self.b, dtype=np.float64)

        for k in range(self.max_iterations):
            for i in range(n):
                s1 = np.dot(self.A[i, :i], x[:i])
                s2 = np.dot(self.A[i, i + 1:], x[i + 1:])
                x_new[i] = (self.b[i] - s1 - s2) / self.A[i, i]

            if np.linalg.norm(x_new - x, ord=np.inf) < self.tolerance:
                print(f"Converged after {k + 1} iterations")
                return x_new

            x = np.copy(x_new)

        print("Did not converge within the maximum number of iterations")
        return x

# Example usage
if __name__ == "__main__":
    A = np.array([[4, -1, 0, 0],
                  [-1, 4, -1, 0],
                  [0, -1, 4, -1],
                  [0, 0, -1, 3]], dtype=np.float64)

    b = np.array([15, 10, 10, 10], dtype=np.float64)

    solver = JacobiSolver(A, b)
    solution = solver.solve()
    print("Solution:", solution)
