#!/usr/bin/python3
def islower(c):
    """
    Checks if a character is lowercase.
    
    Args:
        c: A character to check
        
    Returns:
        True if c is lowercase, False otherwise
    """
    return ord('a') <= ord(c) <= ord('z')
