def minimalHeaviestSetA(arr):
    # Write your code here
    arr.sort(reverse=True)
    a = []
    for v in arr:
        while sum(a) < sum(arr)/2:
            a.append(v)
            break
    a.sort()
    return a





arr = [4, 2, 5, 1, 6]
print(minimalHeaviestSetA(arr))
