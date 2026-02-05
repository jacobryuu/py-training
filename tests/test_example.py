"""
Test suite for algorithm examples
"""
import pytest


def test_example() -> None:
    """Example test case"""
    assert 1 + 1 == 2


def test_list_operations() -> None:
    """Test basic list operations"""
    test_list = [1, 2, 3, 4, 5]
    assert len(test_list) == 5
    assert sum(test_list) == 15
    assert max(test_list) == 5
    assert min(test_list) == 1


def test_string_operations() -> None:
    """Test basic string operations"""
    test_str = "Hello, World!"
    assert test_str.lower() == "hello, world!"
    assert test_str.upper() == "HELLO, WORLD!"
    assert "World" in test_str
