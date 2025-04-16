num1 = 25  
epsilon = 0.01  # Accuracy threshold

# Check if the number is negative
if num1 < 0: 
    print('Does not exist')  # Square root of negative number is not real 
else:
    # Set the range for binary search
    low = 0
    high = max(1, num1)
    ans = (high + low) / 2  # Initial guess
    
    # Continue narrowing down until the square is within the acceptable range
    while abs(ans**2 - num1) >= epsilon:
        if ans**2 < num1:
            low = ans  # Move the lower bound up
        else:
            high = ans  # Move the upper bound down
        ans = (high + low) / 2  # Recalculate the guess
    num1_root = ans  # Store the approximated square root


# Second number to find the cube root of
num2 = -8  

# Handle negative cube roots correctly
if num2 < 0:
    is_pos = False  # Flag for negative input
    num2 = -num2  # Work with the positive value for calculation
else:
    is_pos = True

# Set the search range for cube root
low = 0
high = max(1, num2)
ans = (high + low) / 2  # Initial guess

# Binary search for cube root
while abs(ans**3 - num2) >= epsilon:
    if ans**3 < num2:
        low = ans  # Shift the lower bound
    else:
        high = ans  # Shift the upper bound
    ans = (high + low) / 2  # Update guess

# Restore the sign if the original number was negative
if is_pos:
    num2_root = ans
else:
    num2_root = -ans
    num2 = -num2  # Restore original value

# Print the final result
print('Sum of square root of', num1, 'and cube root of', num2, 'is close to', num1_root + num2_root)