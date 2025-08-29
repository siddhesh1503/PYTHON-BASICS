from typing import List, Dict, Tuple
#List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

#Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

#Tuple with a string and an integer
person: Tuple[str, int] = ("Alice", 30)



n : int = 5
name: str = "John"

def sum(a: int, b: int) -> int:
    return a + b
print(sum(5, 6))
