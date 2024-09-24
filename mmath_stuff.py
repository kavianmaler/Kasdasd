def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    return a + b

def calculate_mean(values):
    if not isinstance(values, list) or not values:
        raise ValueError("Input must be a non-empty list.")
    if not all(isinstance(v, (int, float)) for v in values):
        raise ValueError("All elements in the list must be numbers.")

    return sum(values) / len(values)


def squared_error(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers.")

    return (a - b) ** 2