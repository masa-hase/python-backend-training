"""
String Formatter - TDD Example Implementation

This module demonstrates Test-Driven Development (TDD) with a simple
string formatting utility.
"""


class StringFormatter:
    """A string formatting utility class built using TDD
    
    This class provides methods for formatting strings in various ways.
    It was developed using the Red-Green-Refactor cycle of TDD.
    """
    
    def capitalize_words(self, text: str) -> str:
        """Capitalize the first letter of each word in the text
        
        Args:
            text: The input string to capitalize
            
        Returns:
            A string with the first letter of each word capitalized
            
        Examples:
            >>> formatter = StringFormatter()
            >>> formatter.capitalize_words("hello world")
            'Hello World'
            >>> formatter.capitalize_words("  python   is   great  ")
            'Python Is Great'
        """
        if not text:
            return ""
        
        # Split by whitespace and filter out empty strings
        # This handles multiple spaces correctly
        words = text.split()
        
        # Capitalize each word (first letter upper, rest lower)
        capitalized_words = [word.capitalize() for word in words]
        
        # Join with single spaces
        return " ".join(capitalized_words)