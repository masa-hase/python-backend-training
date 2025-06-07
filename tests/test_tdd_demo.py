"""
TDD Demo - String Formatter Example

This demonstrates the Red-Green-Refactor cycle of TDD.
"""

import pytest
from src.string_formatter import StringFormatter  # This doesn't exist yet!


class TestStringFormatter:
    """Test-driven development example"""
    
    def test_capitalize_first_letter(self):
        """Test capitalizing first letter of each word"""
        # Red Phase: Write a test that fails
        formatter = StringFormatter()
        result = formatter.capitalize_words("hello world")
        assert result == "Hello World"
    
    def test_capitalize_multiple_words(self):
        """Test with multiple words"""
        formatter = StringFormatter()
        assert formatter.capitalize_words("test driven development") == "Test Driven Development"
        assert formatter.capitalize_words("python is awesome") == "Python Is Awesome"
    
    def test_capitalize_empty_string(self):
        """Test edge case: empty string"""
        formatter = StringFormatter()
        assert formatter.capitalize_words("") == ""
    
    def test_capitalize_single_word(self):
        """Test with single word"""
        formatter = StringFormatter()
        assert formatter.capitalize_words("hello") == "Hello"
        assert formatter.capitalize_words("WORLD") == "World"
    
    def test_capitalize_with_extra_spaces(self):
        """Test handling of extra spaces"""
        formatter = StringFormatter()
        assert formatter.capitalize_words("  hello   world  ") == "Hello World"
        assert formatter.capitalize_words("python    is    great") == "Python Is Great"
    
    def test_capitalize_with_special_characters(self):
        """Test words with special characters"""
        formatter = StringFormatter()
        assert formatter.capitalize_words("hello-world") == "Hello-world"
        assert formatter.capitalize_words("test@example.com") == "Test@example.com"