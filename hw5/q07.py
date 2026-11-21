def h(n):
    n = int(n)
    print(f"called h({n}) --- **SPECIAL STRING**")
    # SPECIAL STRING will be changed while grading your codes to ensure that your implementation indeed recursively calls h(...)

# DO NOT CHANGE THE CODE ABOVE

    if n <= 1:
        return n
    elif n%2 == 0:
        return h(n/2)
    else:
        return h((n-1)/2) + h((n+1)/2)



# DO NOT CHANGE THE CODE BELOW

num = int(input())
result = h(num)

print(f"h({num}) == {result}")