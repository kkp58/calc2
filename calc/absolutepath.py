"""File for paths"""
from pathlib import Path

def absolutepath(filepath):
    """This method is for absolute path"""
    relative = Path(filepath)
    return relative.absolute()
