# Advanced Graphs Hard Problems

Curated LeetCode practice for this topic. Solutions are intentionally not included. Solve for pattern recognition, invariant clarity, and interview communication.

## Curation Rules

- Problems are selected for pattern coverage before volume.
- Priority goes to NeetCode 150, Blind 75, Grind 75, and classic high-frequency interview variants.
- Each problem appears once in this repository; related topics should transfer the pattern instead of duplicating the entry.
- Difficulty placement follows the listed LeetCode difficulty and the expected interview reasoning load.

## Practice Order

- First pass: solve in the listed Hard order and write the invariant before coding.
- Second pass: shuffle this file with adjacent topic files to avoid memorizing folder context.
- Retry pass: redo misses after 2 days, 7 days, and 21 days.

## 1. Swim in Rising Water

LeetCode: [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/)

Difficulty: Hard

Pattern: Dijkstra On Bottleneck Path

Why It Matters: Minimizes maximum edge/cell cost along a path.

Skills Tested:
- Recognize that the time to reach `(n - 1, n - 1)` is the minimum over paths of `max(grid[r][c])` along the path, a bottleneck shortest path.
- State the invariant: Dijkstra with a min-heap keyed on `max-so-far` finds the bottleneck minimum to every cell.
- Use binary search on the answer as a clean alternative: feasibility checks via flood-fill.
- Time O(N^2 log N), space O(N^2).

Common Follow-Ups:
- Path With Minimum Effort (LC 1631) is the absolute-difference variant.
- What if some cells block movement entirely.
- Generalize to multi-source bottleneck problems.

## 2. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

LeetCode: [Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)

Difficulty: Hard

Pattern: Kruskal With Per-Edge Re-run

Why It Matters: Advanced Kruskal reasoning.

Skills Tested:
- Recognize that an edge is critical if forcing its absence increases the MST weight, and pseudo-critical if including it does not change the MST weight (and excluding does not).
- State the invariant: compute the baseline MST weight; for each edge, run Kruskal twice (skip the edge, then force the edge first).
- Sort edges once and reuse the sorted order across Kruskal calls.
- Time O(E^2 * alpha(V)), space O(E + V).

Common Follow-Ups:
- Min Cost to Connect All Points (LC 1584) is the underlying MST.
- What if edge weights tie heavily.
- Generalize to second-best MST.

## 3. Critical Connections in a Network

LeetCode: [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/)

Difficulty: Hard

Pattern: Tarjan Bridges Via Low-Link

Why It Matters: Classic bridge-finding problem.

Skills Tested:
- Recognize that an edge is a bridge iff its removal disconnects the graph, characterized by `low[v] > disc[u]` in Tarjan's DFS.
- State the invariant: `disc[u]` is u's DFS discovery time; `low[u]` is the smallest `disc` reachable from u's subtree via a single back edge.
- Skip the parent edge correctly when computing `low` to avoid false back-edge claims.
- Time O(V + E), space O(V + E).

Common Follow-Ups:
- Articulation Points (cut vertices) reuse the same DFS with a different predicate.
- What if the graph is dynamic and edges arrive online (offline incremental algorithms).
- Generalize to bridge-detection in directed graphs (strongly connected components).

## 4. Shortest Path Visiting All Nodes

LeetCode: [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)

Difficulty: Hard

Pattern: BFS Over (Node, Visited Bitmask)

Why It Matters: Combines graph traversal with state compression.

Skills Tested:
- Recognize that the state `(node, visitedMask)` is finite (`N * 2^N`), so BFS finds the shortest sequence of moves visiting all nodes.
- State the invariant: each enqueued state's distance is the shortest known sequence to reach that node with that visited set.
- Initialize the queue with all `(i, 1 << i)` and stop when a state has `mask == (1 << N) - 1`.
- Time O(N * 2^N), space O(N * 2^N).

Common Follow-Ups:
- Travelling Salesperson DP (LC 943) uses the same state with cost minimization.
- What if some nodes can be skipped at a cost.
- Generalize to k-coverage with multiple agents.

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
