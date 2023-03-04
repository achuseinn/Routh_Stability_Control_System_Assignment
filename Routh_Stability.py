import numpy as np

def calculate_polynomial(coefficients, s):
    """Calculate the value of a polynomial for a given value of 's'."""
    result = 0
    for i in range(len(coefficients)):
        result += coefficients[i] * (s ** (len(coefficients) - i - 1))
    return result

def create_routh_table(coefficients, K):
    """Create the Routh table for a given polynomial and K value."""
    n = len(coefficients)
    routh_table = np.zeros((n, (n+1)//2))

    # Fill in the first two rows of the Routh table
    routh_table[0, :] = coefficients[::2]
    routh_table[1, :] = coefficients[1::2]

    # Compute the remaining rows of the Routh table
    for i in range(2, n):
        for j in range((n+1)//2):
            if j == 0:
                routh_table[i, j] = -routh_table[i-1, j+1] / K
            else:
                r1 = routh_table[i-1, j]
                r2 = routh_table[i-2, j-1]
                if r1 == 0:
                    r1 = 1e-10  # Avoid divide-by-zero errors
                routh_table[i, j] = -1 / r1 * r2

    return routh_table

def is_system_stable(routh_table):
    """Determine whether the system is stable or unstable based on its Routh table."""
    # Check if any element in the first column of the Routh table is zero
    if any(routh_table[:, 0] == 0):
        return False

    # Check if all elements in the first column have the same sign
    sign = np.sign(routh_table[0, 0])
    if not np.all(np.sign(routh_table[:, 0]) == sign):
        return False

    # If both checks pass, the system is stable
    return True

# Example usage
coefficients = [1, 6, 11, 6]
K = 2

# Calculate the polynomial for s = 2
s = 2
polynomial_value = calculate_polynomial(coefficients, s)
print(f"Polynomial value for s={s}: {polynomial_value}")

# Create the Routh table
routh_table = create_routh_table(coefficients, K)
print("Routh table:")
print(routh_table)

# Determine if the system is stable or unstable
stable = is_system_stable(routh_table)
if stable:
    print("The system is stable.")
else:
    print("The system is unstable.")

# Change the value of K
new_K = float(input("Enter a new value of K: "))
new_routh_table = create_routh_table(coefficients, new_K)
print("New Routh table:")
print(new_routh_table)

# Determine if the system is stable or unstable for the new value of K
stable = is_system_stable(new_routh_table)
if stable:
    print("The system is stable.")
else:
    print("The system is unstable.")