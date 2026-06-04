# Advanced Graphs Medium Problems

Curated LeetCode practice for this topic. Solutions are intentionally not included. Solve for pattern recognition, invariant clarity, and interview communication.

## Curation Rules

- Problems are selected for pattern coverage before volume.
- Priority goes to NeetCode 150, Blind 75, Grind 75, and classic high-frequency interview variants.
- Each problem appears once in this repository; related topics should transfer the pattern instead of duplicating the entry.
- Difficulty placement follows the listed LeetCode difficulty and the expected interview reasoning load.

## Practice Order

- First pass: solve in the listed Medium order and write the invariant before coding.
- Second pass: shuffle this file with adjacent topic files to avoid memorizing folder context.
- Retry pass: redo misses after 2 days, 7 days, and 21 days.

## 1. Network Delay Time

LeetCode: [Network Delay Time](https://leetcode.com/problems/network-delay-time/)

Difficulty: Medium

Pattern: Dijkstra

Why It Matters: Core non-negative weighted shortest path problem.

Skills Tested:
- Recognize that all edge weights are non-negative, so Dijkstra with a min-heap finds the shortest distance from `k` to every other node.
- State the invariant: when a node pops from the heap, its `dist` is final; further heap entries for that node are stale and skipped.
- The answer is `max(dist)` if every node is reached, else `-1`.
- Time O((V + E) log V), space O(V + E), and contrast with Bellman-Ford O(V * E) which would be needed for negative weights.

Common Follow-Ups:
- Path with Maximum Probability (LC 1514) is the same scaffold with multiplicative probabilities.
- What if some edges can fail with a probability.
- Generalize to delivery problems with multiple sources.

## 2. Path With Minimum Effort

LeetCode: [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)

Difficulty: Medium

Pattern: Dijkstra On Max-Edge Path Cost

Why It Matters: Shortest path under max-edge path cost.

Skills Tested:
- Recognize that the path cost is `max(|h[u] - h[v]|)` along edges, which is monotone enough for Dijkstra with `effort` as the distance label.
- State the invariant: `effort[v] = min(effort[v], max(effort[u], |h[u] - h[v]|))`; relaxations replace summation with max.
- Use a min-heap keyed on effort and skip stale entries.
- Time O(M * N * log(M * N)), space O(M * N), and binary-search-on-answer is an O(M * N * log(maxEffort)) alternative.

Common Follow-Ups:
- Swim in Rising Water (LC 778) is a closely related max-edge-cost problem.
- What if the metric becomes a percentile rather than the max.
- Generalize to multi-source path effort (start from any boundary cell).

## 3. Cheapest Flights Within K Stops

LeetCode: [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

Difficulty: Medium

Pattern: Bounded Bellman-Ford Or BFS Layers

Why It Matters: Tests bounded-edge relaxation.

Skills Tested:
- Recognize that the stops constraint forbids plain Dijkstra; Bellman-Ford relaxed at most `k + 1` times bounds path length to `k + 1` edges.
- State the invariant: after iteration `i`, `dist[v]` is the cheapest cost using at most `i` edges; copy the array each iteration to avoid same-pass overwrites.
- Track stops carefully (the problem says "stops", which is edges minus one).
- Time O(K * E), space O(V), and contrast with state-augmented Dijkstra `(node, edges_used)`.

Common Follow-Ups:
- Bus Routes (LC 815) is a hop-count BFS over a transformed graph.
- What if multiple constraints exist (cost, stops, time).
- Generalize to k-shortest paths.

## 4. Min Cost to Connect All Points

LeetCode: [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)

Difficulty: Medium

Pattern: Minimum Spanning Tree Over Manhattan Distance

Why It Matters: Classic complete-graph MST over Manhattan distance.

Skills Tested:
- Recognize that the cost is the sum of edge weights in a spanning tree; both Kruskal and Prim solve MST in this dense complete graph.
- State the invariant (Prim): the heap holds the cheapest edges crossing the current MST cut; the pop with a non-visited target adds to the MST.
- For Kruskal, sort edges and run union-find, taking the first `n - 1` non-cycle edges.
- Time O(N^2 log N) for Prim or O(N^2 log N) for Kruskal, space O(N^2).

Common Follow-Ups:
- Connecting Cities With Minimum Cost (LC 1135) is MST with edge list input.
- Critical and Pseudo-critical edges in MST (LC 1489) builds on Kruskal.
- What if some edges must be included or excluded from the MST.

## 5. Evaluate Division

LeetCode: [Evaluate Division](https://leetcode.com/problems/evaluate-division/)

Difficulty: Medium

Pattern: Weighted Graph DFS Or Union-Find

Why It Matters: Models ratios as weighted edges.

Skills Tested:
- Recognize that "a / b = c" defines a weighted edge `a -> b` with weight `c` and `b -> a` with weight `1 / c`; queries are products along paths.
- State the invariant: DFS from `src` to `dst` multiplies edge weights; if `dst` is unreachable or a variable is unknown, return `-1`.
- Alternative: weighted union-find with ratios stored on parent edges (path compression updates the ratio).
- Time O(N + Q * (V + E)) for DFS per query, space O(V + E).

Common Follow-Ups:
- Smallest Equivalent String (LC 1061) uses union-find with character ranks.
- What if some ratios may be inconsistent (detect contradiction).
- Generalize to currency conversion with arbitrage detection.

## 6. Redundant Connection

LeetCode: [Redundant Connection](https://leetcode.com/problems/redundant-connection/)

Difficulty: Medium

Pattern: Union-Find Cycle Detection

Why It Matters: Detects the edge that closes a cycle.

Skills Tested:
- Recognize that the redundant edge is the first edge whose endpoints are already in the same union-find component.
- State the invariant: union-find merges components edge-by-edge; a same-component union signals the cycle-closing edge.
- Implement union-by-rank and path compression for near-linear time.
- Time O(E * alpha(V)), space O(V).

Common Follow-Ups:
- Redundant Connection II (LC 685) handles directed graphs and has subtle case analysis.
- What if multiple redundant edges exist (return all).
- Generalize to dynamic connectivity with link-cut trees.

## 7. Course Schedule II

LeetCode: [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

Difficulty: Medium

Pattern: Topological Sort

Why It Matters: Produces an explicit dependency order.

Skills Tested:
- Recognize that a valid course order is any topological order of the prerequisite DAG; a cycle means no order exists.
- State the invariant (Kahn): the queue holds courses with zero remaining prerequisites; popping appends to the order and decrements neighbors' indegrees.
- The answer is the order if its length is `numCourses`, else an empty list.
- Time O(V + E), space O(V + E).

Common Follow-Ups:
- Alien Dictionary (LC 269) builds a topo-sort over inferred letter precedence.
- Minimum Height Trees (LC 310) finds tree centers via leaf-pruning topo-sort.
- What if prerequisites can be partial (best-effort completion).

## 8. Accounts Merge

LeetCode: [Accounts Merge](https://leetcode.com/problems/accounts-merge/)

Difficulty: Medium

Pattern: Union-Find Over Email Strings

Why It Matters: Merges identities through shared emails.

Skills Tested:
- Recognize that emails are nodes and accounts are hyperedges; union all emails belonging to the same account, then group by root.
- State the invariant: after all unions, every email belongs to exactly one component; build name -> sorted email list per root.
- Sort each component's emails for the required output order.
- Time O(N * L log L) where N is account count and L is average emails per account, space O(total emails).

Common Follow-Ups:
- Number of Connected Components (LC 323) is the underlying counting problem.
- What if some emails must be merged manually.
- Generalize to merging entities that share any of multiple identifier fields.

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
