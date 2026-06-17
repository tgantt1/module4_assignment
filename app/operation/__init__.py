# operations.py

class Operation:

    @staticmethod
    def addition(a: float, b: float) -> float:
       
        return a + b  # Performs addition of two numbers and returns the result.
    
    @staticmethod
    def subtraction(a: float, b: float) -> float:
        
        return a - b  # Subtracts the second number from the first and returns the difference.
    
    @staticmethod
    def multiplication(a: float, b: float) -> float:
        
        return a * b  # Multiplies the two numbers and returns the product.
    
    @staticmethod
    def division(a: float, b: float) -> float:
       
        if b == 0:
            # Checks if the divisor is zero to prevent undefined division.
            raise ValueError("Division by zero is not allowed.")  # Raises an error if division by zero is attempted.
        return a / b  # Divides `a` by `b` and returns the quotient.
