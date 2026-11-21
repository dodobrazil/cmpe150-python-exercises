def my_recursive_multiply(a, b):
    print(f"called my_recursive_multiply({a}, {b}) --- **SPECIAL STRING**")
    # SPECIAL STRING will be changed while grading your codes to ensure that your implementation indeed recursively calls my_recursive_multiply(...)

# DO NOT CHANGE THE CODE ABOVE

    if b == 0:
        return 0
    return my_recursive_multiply(a,b-1)+a

# DO NOT CHANGE THE CODE BELOW

num1 = int(input())
num2 = int(input())
result = my_recursive_multiply(num1, num2)

print(f"{num1} x {num2} == {result}")