def q(n, i=1):
    print(f"called q({n}, {i}) --- **SPECIAL STRING**")
    # SPECIAL STRING will be changed while grading your codes to ensure that your implementation indeed recursively calls q(...)

# DO NOT CHANGE THE CODE ABOVE
    if i == n:
        return n + 1/(n+1)
    elif i == 1:
        return 1 + 1/q(n, i+2)
    else:
        return i + 1/q(n, i+2)

# DO NOT CHANGE THE CODE BELOW

num = int(input())
result = q(num)

print(f"q({num}) == {result:.6f}")