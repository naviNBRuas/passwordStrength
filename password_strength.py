'''
This file contains the PasswordStrength class which analyzes the strength of passwords.
'''
import re
class PasswordStrength:
    @staticmethod
    def get_strength(password):
        """
        Calculates the strength of a password based on length, complexity, and special characters.
        Args:
            password (str): The password to evaluate.
        Returns:
            float: The strength of the password, ranging from 0 to 100.
        """
        length_strength = PasswordStrength._check_length(password) * 0.4
        complexity_strength = PasswordStrength._check_complexity(password) * 0.3
        special_chars_strength = PasswordStrength._check_special_chars(password) * 0.3
        strength = length_strength + complexity_strength + special_chars_strength
        return min(strength, 100)
    @staticmethod
    def get_suggestions(password):
        """
        Provides suggestions for creating a stronger password.
        Args:
            password (str): The password to evaluate.
        Returns:
            list: A list of suggestions for creating a stronger password.
        """
        suggestions = []
        if len(password) < 8:
            suggestions.append("Password should be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
            suggestions.append("Password should contain at least one digit.")
        if not any(char.isalpha() for char in password):
            suggestions.append("Password should contain at least one letter.")
        if not any(char.isupper() for char in password):
            suggestions.append("Password should contain at least one uppercase letter.")
        if not any(char.islower() for char in password):
            suggestions.append("Password should contain at least one lowercase letter.")
        if not any(char in "!@#$%^&*()-_=+[]{};:'\"<>,.?/~`" for char in password):
            suggestions.append("Password should contain at least one special character.")
        return suggestions
    @staticmethod
    def _check_length(password):
        """
        Checks the length of the password and returns a strength score.
        Args:
            password (str): The password to evaluate.
        Returns:
            int: The strength score based on the length of the password.
        """
        length = len(password)
        if length < 8:
            return 0
        elif length < 12:
            return 25
        elif length < 16:
            return 50
        else:
            return 75
    @staticmethod
    def _check_complexity(password):
        """
        Checks the complexity of the password and returns a strength score.
        Args:
            password (str): The password to evaluate.
        Returns:
            int: The strength score based on the complexity of the password.
        """
        complexity = 0
        if any(char.isdigit() for char in password):
            complexity += 25
        if any(char.isalpha() for char in password):
            complexity += 25
        if any(char.isupper() for char in password):
            complexity += 25
        if any(char.islower() for char in password):
            complexity += 25
        return complexity
    @staticmethod
    def _check_special_chars(password):
        """
        Checks the presence of special characters in the password and returns a strength score.
        Args:
            password (str): The password to evaluate.
        Returns:
            int: The strength score based on the presence of special characters in the password.
        """
        special_chars = "!@#$%^&*()-_=+[]{};:'\"<>,.?/~`"
        if any(char in special_chars for char in password):
            return 25
        else:
            return 0