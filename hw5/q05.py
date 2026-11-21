def my_recursive_pow(m, n):
    print(f"called my_recursive_pow({m}, {n}) --- **SPECIAL STRING**")
    # SPECIAL STRING will be changed while grading your codes to ensure that your implementation indeed recursively calls my_recursive_pow(...)

# DO NOT CHANGE THE CODE ABOVE

    if n == 0:
        return 1
    
    return my_recursive_pow(m,n-1)*m
    


# DO NOT CHANGE THE CODE BELOW

num1 = int(input())
num2 = int(input())
result = my_recursive_pow(num1, num2)

print(f"{num1} ** {num2} == {result}")