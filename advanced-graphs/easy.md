# Advanced Graphs Easy Problems

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

## 1. Find the Town Judge

LeetCode: [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)

Difficulty: Easy

Pattern: In-degree Out-degree

Why It Matters: Degree accounting before heavier graph algorithms.

Skills Tested:
- Identify the In-degree Out-degree signal before choosing a template.
- State the invariant for Find the Town Judge: degree accounting before heavier graph algorithms.
- Handle negative weights, disconnected graphs, stale heap entries, and dense-graph constraints.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Find the Town Judge toward basic BFS, DAG DP, Bellman-Ford, Floyd-Warshall, Kruskal, Prim, or low-link DFS?
- Which negative weights case would break the first implementation?
- Can the In-degree Out-degree invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Destination City

LeetCode: [Destination City](https://leetcode.com/problems/destination-city/)

Difficulty: Easy

Pattern: Directed Sink Detection

Why It Matters: Builds intuition for sink nodes and missing outgoing edges in a directed graph.

Skills Tested:
- Identify the Directed Sink Detection signal before choosing a template.
- State the invariant for Destination City: builds intuition for sink nodes and missing outgoing edges in a directed graph.
- Handle negative weights, disconnected graphs, stale heap entries, and dense-graph constraints.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Destination City toward basic BFS, DAG DP, Bellman-Ford, Floyd-Warshall, Kruskal, Prim, or low-link DFS?
- Which negative weights case would break the first implementation?
- Can the Directed Sink Detection invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Find Champion I

LeetCode: [Find Champion I](https://leetcode.com/problems/find-champion-i/)

Difficulty: Easy

Pattern: Zero Indegree Champion

Why It Matters: Practices tournament-style graph reasoning with a unique candidate condition.

Skills Tested:
- Identify the Zero Indegree Champion signal before choosing a template.
- State the invariant for Find Champion I: practices tournament-style graph reasoning with a unique candidate condition.
- Handle negative weights, disconnected graphs, stale heap entries, and dense-graph constraints.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Find Champion I toward basic BFS, DAG DP, Bellman-Ford, Floyd-Warshall, Kruskal, Prim, or low-link DFS?
- Which negative weights case would break the first implementation?
- Can the Zero Indegree Champion invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
