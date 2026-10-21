# Maximum Vertex-Disjoint Climbing Paths

## Description

This project solves the problem of finding the maximum number of pairwise vertex-disjoint upward paths of exactly \(k\) edges in a rooted tree.

The algorithm uses dynamic programming and runs in \(O(nk)\) time, with \(O(nk)\) space complexity.

## Input Format

The algorithm accepts:
- `T`: a list of directed edges `(parent, child)`.
- `n`: the number of vertices, labelled from `0` to `n-1`.
- `k`: the required number of edges in each path.

Vertex `0` is the root.

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project directory.
3. Run:

   ```bash
   python climbing.py
   ```

The file includes test cases that can be used to check the implementation.

## Implementation

The implementation is available in `climbing.py`.

## Authors

Anshul Raj Singh and Gauransh Kapur

## Institution
Indian Statistical Institute, Bangalore