# Maximum Vertex-Disjoint Climbing Paths

## Description

This project solves the problem of finding the maximum number of pairwise vertex-disjoint upward paths of exactly $k$ edges in a rooted tree.

The algorithm uses dynamic programming and runs in $O(nk)$ time, with $O(nk)$ space complexity.

## Input Format

The algorithm accepts:
- `T`: a list of directed edges `(parent, child)`.
- `n`: the number of vertices, labelled from `0` to `n-1`.
- `k`: the required number of edges in each path.

Vertex `0` is the root.

For example, `T = [(0, 1), (1, 2), (2, 3)]` is the linear tree with `0` as the root and `3` as the leaf node, `n = 4`.

The following six test cases are included in `climbing.py`:

| Test Case | Number of vertices (`n`) | Path length (`k`) | Expected output |
|---|---:|---:|---:|
| 1 | 1 | 1 | 0 |
| 2 | 4 | 2 | 1 |
| 3 | 6 | 2 | 2 |
| 4 | 4 | 1 | 1 |
| 5 | 5 | 2 | 0 |
| 6 | 7 | 2 | 1 |

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project directory.
3. Run:

   ```bash
   python climbing.py
   ```

   If your system uses `python3` to run Python 3, use:

   ```bash
   python3 climbing.py
   ```

The file includes test cases that can be used to check the implementation.

It should give the following output:
   ```Test Case 1: Expected Output: 0, Actual Output: 0
   Test Case 2: Expected Output: 1, Actual Output: 1
   Test Case 3: Expected Output: 2, Actual Output: 2
   Test Case 4: Expected Output: 1, Actual Output: 1
   Test Case 5: Expected Output: 0, Actual Output: 0
   Test Case 6: Expected Output: 1, Actual Output: 1
   ```

## Authors

Anshul Raj Singh and Gauransh Kapur

## Institution
Indian Statistical Institute, Bangalore