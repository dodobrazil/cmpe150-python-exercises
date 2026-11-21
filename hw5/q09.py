def hakans_number_of_ways_recursive(n):
    print(f"called hakans_number_of_ways_recursive({n}) --- **SPECIAL STRING**")
    # SPECIAL STRING will be changed while grading your codes to ensure that your implementation indeed recursively calls hakans_number_of_ways_recursive(...)

# DO NOT CHANGE THE CODE ABOVE

    if n == 0:
        return 1
    elif n < 0:
        return 0
    
    return hakans_number_of_ways_recursive(n-1) + hakans_number_of_ways_recursive(n-3)
     



# DO NOT CHANGE THE CODE BELOW

num_candies = int(input())
result = hakans_number_of_ways_recursive(num_candies)

print(f"number of ways Hakan can eat candies == {result}")