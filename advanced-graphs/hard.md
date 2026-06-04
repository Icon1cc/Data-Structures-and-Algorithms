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

Pattern: Dijkstra Or MST

Why It Matters: Minimizes maximum edge/cell cost along a path.

Skills Tested:
- Identify the Dijkstra Or MST signal before choosing a template.
- State the invariant for Swim in Rising Water: minimizes maximum edge/cell cost along a path.
- Handle negative weights, disconnected graphs, stale heap entries, and dense-graph constraints.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Swim in Rising Water toward basic BFS, DAG DP, Bellman-Ford, Floyd-Warshall, Kruskal, Prim, or low-link DFS?
- Which negative weights case would break the first implementation?
- Can the Dijkstra Or MST invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

LeetCode: [Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)

Difficulty: Hard

Pattern: MST Edge Classification

Why It Matters: Advanced Kruskal reasoning.

Skills Tested:
- Identify the MST Edge Classification signal before choosing a template.
- State the invariant for Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree: advanced Kruskal reasoning.
- Handle negative weights, disconnected graphs, stale heap entries, and dense-graph constraints.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree toward basic BFS, DAG DP, Bellman-Ford, Floyd-Warshall, Kruskal, Prim, or low-link DFS?
- Which negative weights case would break the first implementation?
- Can the MST Edge Classification invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Critical Connections in a Network

LeetCode: [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/)

Difficulty: Hard

Pattern: Bridges And Low-link

Why It Matters: Classic bridge-finding problem.

Skills Tested:
- Identify the Bridges And Low-link signal before choosing a template.
- State the invariant for Critical Connections in a Network: classic bridge-finding problem.
- Handle negative weights, disconnected graphs, stale heap entries, and dense-graph constraints.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Critical Connections in a Network toward basic BFS, DAG DP, Bellman-Ford, Floyd-Warshall, Kruskal, Prim, or low-link DFS?
- Which negative weights case would break the first implementation?
- Can the Bridges And Low-link invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Shortest Path Visiting All Nodes

LeetCode: [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)

Difficulty: Hard

Pattern: BFS With Bitmask State

Why It Matters: Combines graph traversal with state compression.

Skills Tested:
- Identify the BFS With Bitmask State signal before choosing a template.
- State the invariant for Shortest Path Visiting All Nodes: combines graph traversal with state compression.
- Handle negative weights, disconnected graphs, stale heap entries, and dense-graph constraints.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Shortest Path Visiting All Nodes toward basic BFS, DAG DP, Bellman-Ford, Floyd-Warshall, Kruskal, Prim, or low-link DFS?
- Which negative weights case would break the first implementation?
- Can the BFS With Bitmask State invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
