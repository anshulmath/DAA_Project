def code(T, n, k):
    children = {v : [] for v in range(n)}

    # Storing children of each node
    for u, v in T:
        children[u].append(v)

    temp = -67777777777

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
            other_children = total - max(G(u), H(u, k))
            max_value = H(u, d-1) + other_children

            if d == k:
                max_value += 1

            count = max(count, max_value)

        h[(v, d)] = count
        return count

    if k == 0:
        return n

    return max(G(0), H(0, k))

# Test cases
print(code([(0, 1), (1, 2), (2, 3)], 4, 2))  # Expected output: `1`
print(code([(0, 1), (0, 2), (0, 3)], 4, 1))  # Expected output: `1`