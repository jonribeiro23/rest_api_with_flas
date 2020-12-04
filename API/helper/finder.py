def search(sequence, expected, finder):
    for element in sequence:
        if finder(element) == expected:
            return element
    return RuntimeError(f"Could not find an element with '{expected}'")