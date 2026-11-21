def my_recursive_series_sum(N):
    print(f"called my_recursive_series_sum({N}) --- **SPECIAL STRING**")
    # SPECIAL STRING will be changed while grading your codes to ensure that your implementation indeed recursively calls my_recursive_series_sum(...)

# DO NOT CHANGE THE CODE ABOVE
    if N == 0:
        return 0
    return my_recursive_series_sum(N-1)+N
        

   

# DO NOT CHANGE THE CODE BELOW

num = int(input())
result = my_recursive_series_sum(num)

print(f"SERIES_SUM({num}) == {result}")