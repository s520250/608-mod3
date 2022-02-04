# Sammie Bever

def maximum(value1, value2, value3):
    """Return the maximum of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

print('Maximum value of 12, 27, and 36 is:', maximum(12, 27, 36))

print('Max value of 12, 27, and 36 is:', max(12, 27, 36))

def minimum(value1, value2, value3):
    """Return the minimum of three values."""
    min_value = value1
    if value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value3
    return min_value

print('Custom minimum value of 35, 48, and 77 is:', minimum(35, 48, 77))

print('Min value of 15, 9, 27, and 14 is:', min(15, 9, 27, 14))

# Sammie Bever

