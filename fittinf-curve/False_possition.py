class FalsePositionSolver:
    def __init__(self, polynomial):
        """
        Initialize the False Position solver with a polynomial.
        
        Args:
        polynomial (list): Coefficients of the polynomial from highest degree to constant term
        Example: [1, -3, 2] represents x^2 - 3x + 2
        """
        self.polynomial = polynomial
    
    def evaluate_polynomial(self, x):
        """
        Evaluate the polynomial at a given x value.
        
        Args:
        x (float): Value at which to evaluate the polynomial
        
        Returns:
        float: Value of the polynomial at x
        """
        return sum(coeff * (x ** (len(self.polynomial) - 1 - power)) 
                for power, coeff in enumerate(self.polynomial))
    
    def false_position_method(self, a, b, max_iterations=100, tolerance=1e-6):
        """
        Solve for a root of the polynomial using False Position method.
        
        Args:
        a (float): Lower bound of the interval
        b (float): Upper bound of the interval
        max_iterations (int): Maximum number of iterations
        tolerance (float): Convergence tolerance
        
        Returns:
        dict: Results of the root-finding process
        """
        # Validate initial interval
        fa = self.evaluate_polynomial(a)
        fb = self.evaluate_polynomial(b)
        
        # Check if root is bracketed
        if fa * fb >= 0:
            raise ValueError("Root is not bracketed in the given interval")
        
        iterations = 0
        while iterations < max_iterations:
            # False Position formula
            x = ((a * fb) - (b * fa)) / (fb - fa)
            fx = self.evaluate_polynomial(x)
            
            # Check convergence
            if abs(fx) < tolerance:
                return {
                    'root': x,
                    'iterations': iterations + 1,
                    'converged': True,
                    'function_value': fx
                }
            
            # Update interval
            if fa * fx < 0:
                b = x
                fb = fx
            else:
                a = x
                fa = fx
            
            iterations += 1
        
        # Failed to converge
        return {
            'root': x,
            'iterations': iterations,
            'converged': False,
            'function_value': fx
        }
    
    def find_roots(self, a, b):
        """
        Find roots in the given interval.
        
        Args:
        a (float): Lower bound of the interval
        b (float): Upper bound of the interval
        
        Returns:
        list: Roots found in the interval
        """
        try:
            result = self.false_position_method(a, b)
            return [result['root']] if result['converged'] else []
        except ValueError:
            return []

def main():
    """
    Enter your code here\n
    Note : when you enter polynomial you must enter it as list for example
    X^2+4x-1=0 => [1,4,-1]
    """
if __name__ == "__main__":
    main()