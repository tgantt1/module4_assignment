
import pytest
from app.operation import Operation

# -----------------------------------------------------------------------------------
# Test Addition Method
# -----------------------------------------------------------------------------------

def test_addition_positive():
    
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 15.0

    # Act
    result = Operation.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"


def test_addition_negative_numbers():
    
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = -15.0

    # Act
    result = Operation.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"


def test_addition_positive_negative():
   
    # Arrange
    a = 10.0
    b = -5.0
    expected_result = 5.0

    # Act
    result = Operation.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + ({b}) to be {expected_result}, got {result}"


def test_addition_with_zero():
   
    # Arrange
    a = 10.0
    b = 0.0
    expected_result = 10.0

    # Act
    result = Operation.addition(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Subtraction Method
# -----------------------------------------------------------------------------------

def test_subtraction_positive():
    
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 5.0

    # Act
    result = Operation.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - {b} to be {expected_result}, got {result}"


def test_subtraction_negative_numbers():
    
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = -5.0

    # Act
    result = Operation.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - ({b}) to be {expected_result}, got {result}"


def test_subtraction_positive_negative():
   
    # Arrange
    a = 10.0
    b = -5.0
    expected_result = 15.0

    # Act
    result = Operation.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - ({b}) to be {expected_result}, got {result}"


def test_subtraction_with_zero():
    
    # Arrange
    a = 10.0
    b = 0.0
    expected_result = 10.0

    # Act
    result = Operation.subtraction(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Multiplication Method
# -----------------------------------------------------------------------------------

def test_multiplication_positive():
    
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 50.0

    # Act
    result = Operation.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"


def test_multiplication_negative_numbers():
    
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = 50.0

    # Act
    result = Operation.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"


def test_multiplication_positive_negative():
    
    # Arrange
    a = 10.0
    b = -5.0
    expected_result = -50.0

    # Act
    result = Operation.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * ({b}) to be {expected_result}, got {result}"


def test_multiplication_with_zero():
    
    # Arrange
    a = 10.0
    b = 0.0
    expected_result = 0.0

    # Act
    result = Operation.multiplication(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Division Method
# -----------------------------------------------------------------------------------

def test_division_positive():
    
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 2.0

    # Act
    result = Operation.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"


def test_division_negative_numbers():
    
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = 2.0

    # Act
    result = Operation.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"


def test_division_positive_negative():
    
    # Arrange
    a = 10.0
    b = -5.0
    expected_result = -2.0

    # Act
    result = Operation.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / ({b}) to be {expected_result}, got {result}"


def test_division_with_zero_divisor():
   
    # Arrange
    a = 10.0
    b = 0.0

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        Operation.division(a, b)
    
    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Division by zero is not allowed."


def test_division_with_zero_numerator():
    
    # Arrange
    a = 0.0
    b = 5.0
    expected_result = 0.0

    # Act
    result = Operation.division(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Invalid Input Types (Negative Testing)
# -----------------------------------------------------------------------------------

@pytest.mark.parametrize("calc_method, a, b, expected_exception", [
    (Operation.addition, '10', 5.0, TypeError),
    (Operation.subtraction, 10.0, '5', TypeError),
    (Operation.multiplication, '10', '5', TypeError),
    (Operation.division, 10.0, '5', TypeError),
])
def test_operations_invalid_input_types(calc_method, a, b, expected_exception):
    
    # Arrange
    # No setup needed as the invalid inputs are provided directly

    # Act & Assert
    with pytest.raises(expected_exception):
        calc_method(a, b)