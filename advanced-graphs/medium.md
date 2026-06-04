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
- Identify the Dijkstra signal before choosing a template.
- State the invariant for Network Delay Time: core non-negative weighted shortest path problem.
- Handle negative weights, disconnected graphs, stale heap entries, and dense-graph constraints.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Network Delay Time toward basic BFS, DAG DP, Bellman-Ford, Floyd-Warshall, Kruskal, Prim, or low-link DFS?
- Which negative weights case would break the first implementation?
- Can the Dijkstra invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Path With Minimum Effort

LeetCode: [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)

Difficulty: Medium

Pattern: Dijkstra Or Binary Search

Why It Matters: Shortest path under max-edge path cost.

Skills Tested:
- Identify the Dijkstra Or Binary Search signal before choosing a template.
- State the invariant for Path With Minimum Effort: shortest path under max-edge path cost.
- Handle negative weights, disconnected graphs, stale heap entries, and dense-graph constraints.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Path With Minimum Effort toward basic BFS, DAG DP, Bellman-Ford, Floyd-Warshall, Kruskal, Prim, or low-link DFS?
- Which negative weights case would break the first implementation?
- Can the Dijkstra Or Binary Search invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Cheapest Flights Within K Stops

LeetCode: [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

Difficulty: Medium

Pattern: Bellman-Ford Variant

Why It Matters: Tests bounded-edge relaxation.

Skills Tested:
- Identify the Bellman-Ford Variant signal before choosing a template.
- State the invariant for Cheapest Flights Within K Stops: tests bounded-edge relaxation.
- Handle negative weights, disconnected graphs, stale heap entries, and dense-graph constraints.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Cheapest Flights Within K Stops toward basic BFS, DAG DP, Bellman-Ford, Floyd-Warshall, Kruskal, Prim, or low-link DFS?
- Which negative weights case would break the first implementation?
- Can the Bellman-Ford Variant invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Min Cost to Connect All Points

LeetCode: [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)

Difficulty: Medium

Pattern: Minimum Spanning Tree

Why It Matters: Classic complete-graph MST over Manhattan distance.

Skills Tested:
- Identify the Minimum Spanning Tree signal before choosing a template.
- State the invariant for Min Cost to Connect All Points: classic complete-graph MST over Manhattan distance.
- Handle negative weights, disconnected graphs, stale heap entries, and dense-graph constraints.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Min Cost to Connect All Points toward basic BFS, DAG DP, Bellman-Ford, Floyd-Warshall, Kruskal, Prim, or low-link DFS?
- Which negative weights case would break the first implementation?
- Can the Minimum Spanning Tree invariant survive streaming input, in-place restrictions, or lower memory limits?

## 5. Evaluate Division

LeetCode: [Evaluate Division](https://leetcode.com/problems/evaluate-division/)

Difficulty: Medium

Pattern: Weighted Graph DFS

Why It Matters: Models ratios as weighted edges.

Skills Tested:
- Identify the Weighted Graph DFS signal before choosing a template.
- State the invariant for Evaluate Division: models ratios as weighted edges.
- Handle negative weights, disconnected graphs, stale heap entries, and dense-graph constraints.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Evaluate Division toward basic BFS, DAG DP, Bellman-Ford, Floyd-Warshall, Kruskal, Prim, or low-link DFS?
- Which negative weights case would break the first implementation?
- Can the Weighted Graph DFS invariant survive streaming input, in-place restrictions, or lower memory limits?

## 6. Redundant Connection

LeetCode: [Redundant Connection](https://leetcode.com/problems/redundant-connection/)

Difficulty: Medium

Pattern: Union Find

Why It Matters: Detects the edge that closes a cycle.

Skills Tested:
- Identify the Union Find signal before choosing a template.
- State the invariant for Redundant Connection: detects the edge that closes a cycle.
- Handle negative weights, disconnected graphs, stale heap entries, and dense-graph constraints.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Redundant Connection toward basic BFS, DAG DP, Bellman-Ford, Floyd-Warshall, Kruskal, Prim, or low-link DFS?
- Which negative weights case would break the first implementation?
- Can the Union Find invariant survive streaming input, in-place restrictions, or lower memory limits?

## 7. Course Schedule II

LeetCode: [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

Difficulty: Medium

Pattern: Topological Sort

Why It Matters: Produces an explicit dependency order.

Skills Tested:
- Identify the Topological Sort signal before choosing a template.
- State the invariant for Course Schedule II: produces an explicit dependency order.
- Handle negative weights, disconnected graphs, stale heap entries, and dense-graph constraints.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Course Schedule II toward basic BFS, DAG DP, Bellman-Ford, Floyd-Warshall, Kruskal, Prim, or low-link DFS?
- Which negative weights case would break the first implementation?
- Can the Topological Sort invariant survive streaming input, in-place restrictions, or lower memory limits?

## 8. Accounts Merge

LeetCode: [Accounts Merge](https://leetcode.com/problems/accounts-merge/)

Difficulty: Medium

Pattern: Union Find

Why It Matters: Merges identities through shared emails.

Skills Tested:
- Identify the Union Find signal before choosing a template.
- State the invariant for Accounts Merge: merges identities through shared emails.
- Handle negative weights, disconnected graphs, stale heap entries, and dense-graph constraints.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Accounts Merge toward basic BFS, DAG DP, Bellman-Ford, Floyd-Warshall, Kruskal, Prim, or low-link DFS?
- Which negative weights case would break the first implementation?
- Can the Union Find invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
