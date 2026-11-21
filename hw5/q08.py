def my_recursive_n_to_1(n):
    print(f"called my_recursive_n_to_1({n}) --- **SPECIAL STRING**")
    # SPECIAL STRING will be changed while grading your codes to ensure that your implementation indeed recursively calls my_recursive_n_to_1(...)

# DO NOT CHANGE THE CODE ABOVE

    if n == 1:
        return [1]
    return [n] + my_recursive_n_to_1(n-1)

# DO NOT CHANGE THE CODE BELOW

num = int(input())
result = my_recursive_n_to_1(num)

print(f"[n, n-1, ..., 2, 1] == {result}")