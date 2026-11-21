def my_recursive_gcd(a, b):
    print(f"called my_recursive_gcd({a}, {b}) --- **SPECIAL STRING**")
    # SPECIAL STRING will be changed while grading your codes to ensure that your implementation indeed recursively calls my_recursive_gcd(...)

# DO NOT CHANGE THE CODE ABOVE

    if b == 0:
        return a
    return my_recursive_gcd(b,a%b)

# DO NOT CHANGE THE CODE BELOW

num1 = int(input())
num2 = int(input())
result = my_recursive_gcd(num1, num2)

print(f"GCD({num1}, {num2}) == {result}")