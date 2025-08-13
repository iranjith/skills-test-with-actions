# System Modules
import math
import sys
import os

# Installed Modules
# None

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    # Assert
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1


def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    # Arrange
    n = 10

    # Act
    result = get_nth_fibonacci(n)

# Assert
def test_area_of_circle_negative_radius():
    """Test with a negative radius (should raise ValueError)."""
    radius = -1
    try:
        area_of_circle(radius)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Radius cannot be negative"


def test_get_nth_fibonacci_negative():
    """Test with negative n (should raise ValueError)."""
    n = -5
    try:
        get_nth_fibonacci(n)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "n cannot be negative"


def test_get_nth_fibonacci_two():
    """Test with n=2."""
    n = 2
    result = get_nth_fibonacci(n)
    assert result == 1


def test_get_nth_fibonacci_large_n():
    """Test with a large n."""
    n = 20
    result = get_nth_fibonacci(n)
    assert result == 6765


def test_get_nth_fibonacci_three():
    """Test with n=3."""
    n = 3
    result = get_nth_fibonacci(n)
    assert result == 2

def test_get_nth_fibonacci_five():
    """Test with n=5."""
    n = 5
    result = get_nth_fibonacci(n)
    assert result == 5

def test_get_nth_fibonacci_large():
    """Test with a very large n."""
    n = 50
    result = get_nth_fibonacci(n)
    assert result == 12586269025
def test_area_of_circle_float_radius():
    """Test with a float radius."""
    radius = 2.5
    result = area_of_circle(radius)
    assert abs(result - (math.pi * 2.5 ** 2)) < 1e-10

def test_area_of_circle_large_radius():
    """Test with a large radius."""
    radius = 1e6
    result = area_of_circle(radius)
    assert abs(result - (math.pi * radius ** 2)) < 1e-5

def test_area_of_circle_type_error():
    """Test with a non-numeric radius (should raise TypeError)."""
    try:
        area_of_circle("a string")
        assert False, "Expected TypeError"
    except TypeError:
        pass

def test_get_nth_fibonacci_type_error():
    """Test with a non-integer n (should raise TypeError)."""
    try:
        get_nth_fibonacci("string")
        assert False, "Expected TypeError"
    except TypeError:
        pass

def test_get_nth_fibonacci_float():
    """Test with a float n (should raise TypeError)."""
    try:
        get_nth_fibonacci(5.5)
        assert False, "Expected TypeError"
    except TypeError:
        pass

