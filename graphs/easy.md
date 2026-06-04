# Graphs Easy Problems

Curated LeetCode practice for this topic. Solutions are intentionally not included. Solve for pattern recognition, invariant clarity, and interview communication.

## Curation Rules

- Problems are selected for pattern coverage before volume.
- Priority goes to NeetCode 150, Blind 75, Grind 75, and classic high-frequency interview variants.
- Each problem appears once in this repository; related topics should transfer the pattern instead of duplicating the entry.
- Difficulty placement follows the listed LeetCode difficulty and the expected interview reasoning load.

## Practice Order

- First pass: solve in the listed Easy order and write the invariant before coding.
- Second pass: shuffle this file with adjacent topic files to avoid memorizing folder context.
- Retry pass: redo misses after 2 days, 7 days, and 21 days.

## 1. Flood Fill

LeetCode: [Flood Fill](https://leetcode.com/problems/flood-fill/)

Difficulty: Easy

Pattern: Grid DFS Or BFS

Why It Matters: Baseline grid traversal with color constraints.

Skills Tested:
- Recognize that "fill the connected region of cells with the original color" is a DFS or BFS over 4-directional neighbors gated by the original color.
- State the invariant: every visited cell originally had the source color and now has the new color; the frontier only adds cells matching the source color.
- Save the original color before mutation; if `oldColor == newColor`, return immediately to avoid an infinite loop.
- Time O(M * N), space O(M * N) recursion or queue.

Common Follow-Ups:
- Number of Islands (LC 200) reuses the connected-region traversal with counting.
- What if the grid uses 8-directional connectivity.
- Generalize to weighted-region budgets.

## 2. Find if Path Exists in Graph

LeetCode: [Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/)

Difficulty: Easy

Pattern: Reachability Search Or Union-Find

Why It Matters: Simple graph connectivity check.

Skills Tested:
- Recognize that "is there a path from `source` to `destination`" is reachability, solvable by BFS, DFS, or union-find on the edges.
- State the invariant (search): a `visited` set always contains every node enqueued so far; the answer is true once `destination` is enqueued.
- For union-find, after processing all edges, the answer is `find(source) == find(destination)`.
- Time O(V + E), space O(V).

Common Follow-Ups:
- Number of Connected Components in an Undirected Graph (LC 323) returns the component count.
- What if edges arrive online (incremental union-find).
- Generalize to k-source/k-sink reachability.

## 3. Island Perimeter

LeetCode: [Island Perimeter](https://leetcode.com/problems/island-perimeter/)

Difficulty: Easy

Pattern: Grid Edge Counting

Why It Matters: Introduces grid neighbor reasoning.

Skills Tested:
- Recognize that perimeter equals `4 * islandCells - 2 * sharedEdges`, so a single pass over land cells suffices.
- State the invariant: each land cell contributes 4; each adjacent land neighbor (only need to check up and left) subtracts 2.
- Avoid DFS; this is O(M * N) regardless of island shape.
- Time O(M * N), space O(1) extra.

Common Follow-Ups:
- Number of Distinct Islands (LC 694) classifies islands by shape signature.
- What if water cells have non-trivial weights.
- Generalize to perimeter on hexagonal grids.

## 4. Employee Importance

LeetCode: [Employee Importance](https://leetcode.com/problems/employee-importance/)

Difficulty: Easy

Pattern: DFS Sum Aggregation

Why It Matters: Traverses implicit management relationships.

Skills Tested:
- Recognize that the total importance under a manager is `self.importance + sum(importance(sub) for sub in directReports)`, solved by DFS.
- State the invariant: each call returns the subtree-sum rooted at the given employee.
- Build a hash map from id to employee for O(1) lookup before recursing.
- Time O(N), space O(N) for the map and recursion.

Common Follow-Ups:
- Sum of Distances in Tree (LC 834) does a similar aggregation with a re-rooting technique.
- What if the hierarchy can be cyclic (need cycle detection).
- Generalize to weighted importance with attenuation per level.

## 5. Find Center of Star Graph

LeetCode: [Find Center of Star Graph](https://leetcode.com/problems/find-center-of-star-graph/)

Difficulty: Easy

Pattern: Degree Recognition

Why It Matters: Uses graph structure instead of traversal.

Skills Tested:
- Recognize that in a star graph, the center is the only node that appears in every edge, so checking the first two edges is enough.
- State the invariant: the node common to `edges[0]` and `edges[1]` is the unique center; no traversal is needed.
- Handle the trivial case `n == 2` separately if the graph is degenerate.
- Time O(1), space O(1), and contrast with degree-counting which is O(E).

Common Follow-Ups:
- Find If Path Exists in Graph (LC 1971) is a more general reachability problem.
- What if the graph is "almost" a star with one extra edge.
- Generalize to detecting a wheel or complete bipartite structure.

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
