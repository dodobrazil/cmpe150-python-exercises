def my_recursive_factorial(N):
    print(f"called my_recursive_factorial({N}) --- **SPECIAL STRING**")
    # SPECIAL STRING will be changed while grading your codes to ensure that your implementation indeed recursively calls my_recursive_factorial(...)

# DO NOT CHANGE THE CODE ABOVE

    if N == 0:
        return 1
    
    return my_recursive_factorial(N-1)*N
        



# DO NOT CHANGE THE CODE BELOW

num = int(input())
result = my_recursive_factorial(num)

print(f"Fact({num}) == {result}")