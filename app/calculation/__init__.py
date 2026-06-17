# calculator_calculations.py

# -----------------------------------------------------------------------------------
# Import Statements
# -----------------------------------------------------------------------------------

# Import ABC (Abstract Base Class) and abstractmethod from Python's abc module.
# Abstract Base Classes (ABCs) allow us to define a contract for our subclasses, specifying 
# methods that they must implement. This helps in establishing a standard interface for 
# similar objects without enforcing specific details on how they should work.
from abc import ABC, abstractmethod

# Import the Operation class from the app.operation module. 
# The Operation class is where our basic mathematical functions (e.g., addition, subtraction) are defined.
# Rather than implementing arithmetic logic within each calculation class, we encapsulate it in a 
# separate class to promote modularity. This makes it easier to modify or extend these functions independently.
from app.operation import Operation

# -----------------------------------------------------------------------------------
# Abstract Base Class: Calculation
# -----------------------------------------------------------------------------------
class Calculation(ABC):
    

    def __init__(self, a: float, b: float) -> None:
       
        self.a: float = a  # Stores the first operand as a floating-point number.
        self.b: float = b  # Stores the second operand as a floating-point number.

    @abstractmethod
    def execute(self) -> float:
      
        pass  # The actual implementation will be provided by the subclass. # pragma: no cover

    def __str__(self) -> str:
        
        result = self.execute()  # Run the calculation to get the result.
        operation_name = self.__class__.__name__.replace('Calculation', '')  # Derive operation name.
        return f"{self.__class__.__name__}: {self.a} {operation_name} {self.b} = {result}"

    def __repr__(self) -> str:
       
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"

# -----------------------------------------------------------------------------------
# Factory Class: CalculationFactory
# -----------------------------------------------------------------------------------
class CalculationFactory:

    # _calculations is a dictionary that holds a mapping of calculation types 
    # (like "add" or "subtract") to their respective classes.
    _calculations = {}

    @classmethod
    def register_calculation(cls, calculation_type: str):
        
        def decorator(subclass):
            # Convert calculation_type to lowercase to ensure consistency.
            calculation_type_lower = calculation_type.lower()
            # Check if the calculation type has already been registered to avoid duplication.
            if calculation_type_lower in cls._calculations:
                raise ValueError(f"Calculation type '{calculation_type}' is already registered.")
            # Register the subclass in the _calculations dictionary.
            cls._calculations[calculation_type_lower] = subclass
            return subclass  # Return the subclass for chaining or additional use.
        return decorator  # Return the decorator function.

    @classmethod
    def create_calculation(cls, calculation_type: str, a: float, b: float) -> Calculation:
        
        calculation_type_lower = calculation_type.lower()
        calculation_class = cls._calculations.get(calculation_type_lower)
        # If the type is unsupported, raise an error with the available types.
        if not calculation_class:
            available_types = ', '.join(cls._calculations.keys())
            raise ValueError(f"Unsupported calculation type: '{calculation_type}'. Available types: {available_types}")
        # Create and return an instance of the requested calculation class with the provided operands.
        return calculation_class(a, b)

# -----------------------------------------------------------------------------------
# Concrete Calculation Classes
# -----------------------------------------------------------------------------------

# Each of these classes defines a specific calculation type (addition, subtraction, 
# multiplication, or division). These classes inherit from Calculation, implementing 
# the `execute` method to perform the specific arithmetic operation. 

@CalculationFactory.register_calculation('add')
class AddCalculation(Calculation):


    def execute(self) -> float:
        # Calls the addition method from the Operation module to perform the addition.
        return Operation.addition(self.a, self.b)

@CalculationFactory.register_calculation('subtract')
class SubtractCalculation(Calculation):

    def execute(self) -> float:
        # Calls the subtraction method from the Operation module to perform the subtraction.
        return Operation.subtraction(self.a, self.b)

@CalculationFactory.register_calculation('multiply')
class MultiplyCalculation(Calculation):

    def execute(self) -> float:
        # Calls the multiplication method from the Operation module to perform the multiplication.
        return Operation.multiplication(self.a, self.b)

@CalculationFactory.register_calculation('divide')
class DivideCalculation(Calculation):

    def execute(self) -> float:
        # Before performing division, check if `b` is zero to avoid ZeroDivisionError.
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        # Calls the division method from the Operation module to perform the division.
        return Operation.division(self.a, self.b)

# @CalculationFactory.register_calculation('power')
# class PowerCalculation(Calculation):
#     def execute(self) -> float:
#         # Calls the multiplication method from the Operation module to perform the multiplication.
#         return Operation.power(self.a, self.b) # pragma: no cover