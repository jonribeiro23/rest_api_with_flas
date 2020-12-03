from typing import List

def avarage(sequence: List) -> float:
    return sum(sequence) / len(sequence)

print(avarage([1, 2, 3]))