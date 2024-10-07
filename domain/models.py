"""
Core model definition
"""
from dataclasses import dataclass
from typing import Set

@dataclass
class Requirement:
    """
    Requirement model
    """
    name: str
    criteria: Set[str]

    def __repr__(self):
        return f'Requirement(name={self.name}, criteria={self.criteria})'
