def MaximumClimbers(T, n, k):
    children = {v : [] for v in range(n)}

    # Storing children of each node
    for u, v in T:
        children[u].append(v)

    temp = -67

    g = {}
    h = {}

    def G(v):
        if v in g:
            return g[v]
        
        count = 0
        for u in children[v]:
            count += max(G(u), H(u, k))

        g[v] = count
        return count

    def H(v, d):
        if v in h:
            return h[(v, d)]

        if d == 0:
            h[(v, d)] = G(v)
            return h[(v, d)]

        count = temp
        total = G(v)

        for u in children[v]:
            other = total - max(G(u), H(u, k))
            max_value = H(u, d-1) + other

            if d == k:
                max_value += 1

            count = max(count, max_value)

        h[(v, d)] = count
        return count

    if k == 0:
        return n

    return max(G(0), H(0, k))

#### Test Cases ####

tests = [
    ([], 1, 1, 0),
    ([(0, 1), (1, 2), (2, 3)], 4, 2, 1),
    ([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)], 6, 2, 2),
    ([(0, 1), (0, 2), (0, 3)], 4, 1, 1),
    ([(0, 1), (0, 2), (0, 3), (0, 4)], 5, 2, 0),
    (
        [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)],
        7, 2, 1
    )
]

for i, (T, n, k, expected) in enumerate(tests, start=1):
    actual = MaximumClimbers(T, n, k)
    print(
        f"Test Case {i}: Expected Output: {expected}, "
        f"Actual Output: {actual}"
    )