def my_recursive_digit_sum(N):
    print(f"called my_recursive_digit_sum({N}) --- **SPECIAL STRING**")
    # SPECIAL STRING will be changed while grading your codes to ensure that your implementation indeed recursively calls my_recursive_digit_sum(...)

# DO NOT CHANGE THE CODE ABOVE

    if N == 0:
        return 0
    return my_recursive_digit_sum(int(N/10)) + N%10


# DO NOT CHANGE THE CODE BELOW

num = int(input())
result = my_recursive_digit_sum(num)

print(f"DIGIT_SUM({num}) == {result}")