# Graphs Medium Problems

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

## 1. Number of Islands

LeetCode: [Number of Islands](https://leetcode.com/problems/number-of-islands/)

Difficulty: Medium

Pattern: Connected Components

Why It Matters: The canonical grid component problem.

Skills Tested:
- Identify the Connected Components signal before choosing a template.
- State the invariant for Number of Islands: the canonical grid component problem.
- Handle disconnected components, cycles, duplicate enqueues, and directed versus undirected edges.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Number of Islands toward Union Find, topological sort, Dijkstra, dynamic programming, or backtracking?
- Which disconnected components case would break the first implementation?
- Can the Connected Components invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Clone Graph

LeetCode: [Clone Graph](https://leetcode.com/problems/clone-graph/)

Difficulty: Medium

Pattern: DFS/BFS With Map

Why It Matters: Tests graph copying and visited mapping.

Skills Tested:
- Identify the DFS/BFS With Map signal before choosing a template.
- State the invariant for Clone Graph: tests graph copying and visited mapping.
- Handle disconnected components, cycles, duplicate enqueues, and directed versus undirected edges.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Clone Graph toward Union Find, topological sort, Dijkstra, dynamic programming, or backtracking?
- Which disconnected components case would break the first implementation?
- Can the DFS/BFS With Map invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Course Schedule

LeetCode: [Course Schedule](https://leetcode.com/problems/course-schedule/)

Difficulty: Medium

Pattern: Cycle Detection

Why It Matters: Classic directed cycle detection.

Skills Tested:
- Identify the Cycle Detection signal before choosing a template.
- State the invariant for Course Schedule: classic directed cycle detection.
- Handle disconnected components, cycles, duplicate enqueues, and directed versus undirected edges.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Course Schedule toward Union Find, topological sort, Dijkstra, dynamic programming, or backtracking?
- Which disconnected components case would break the first implementation?
- Can the Cycle Detection invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Rotting Oranges

LeetCode: [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

Difficulty: Medium

Pattern: Multi-source BFS

Why It Matters: Models simultaneous spread by levels.

Skills Tested:
- Identify the Multi-source BFS signal before choosing a template.
- State the invariant for Rotting Oranges: models simultaneous spread by levels.
- Handle disconnected components, cycles, duplicate enqueues, and directed versus undirected edges.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Rotting Oranges toward Union Find, topological sort, Dijkstra, dynamic programming, or backtracking?
- Which disconnected components case would break the first implementation?
- Can the Multi-source BFS invariant survive streaming input, in-place restrictions, or lower memory limits?

## 5. Pacific Atlantic Water Flow

LeetCode: [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)

Difficulty: Medium

Pattern: Reverse DFS/BFS

Why It Matters: Tests reachability from boundaries.

Skills Tested:
- Identify the Reverse DFS/BFS signal before choosing a template.
- State the invariant for Pacific Atlantic Water Flow: tests reachability from boundaries.
- Handle disconnected components, cycles, duplicate enqueues, and directed versus undirected edges.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Pacific Atlantic Water Flow toward Union Find, topological sort, Dijkstra, dynamic programming, or backtracking?
- Which disconnected components case would break the first implementation?
- Can the Reverse DFS/BFS invariant survive streaming input, in-place restrictions, or lower memory limits?

## 6. Surrounded Regions

LeetCode: [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)

Difficulty: Medium

Pattern: Boundary Connected Components

Why It Matters: Distinguishes safe regions from captured ones.

Skills Tested:
- Identify the Boundary Connected Components signal before choosing a template.
- State the invariant for Surrounded Regions: distinguishes safe regions from captured ones.
- Handle disconnected components, cycles, duplicate enqueues, and directed versus undirected edges.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Surrounded Regions toward Union Find, topological sort, Dijkstra, dynamic programming, or backtracking?
- Which disconnected components case would break the first implementation?
- Can the Boundary Connected Components invariant survive streaming input, in-place restrictions, or lower memory limits?

## 7. Graph Valid Tree

LeetCode: [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)

Difficulty: Medium

Pattern: Cycle Detection And Connectivity

Why It Matters: Combines no-cycle and connected requirements.

Skills Tested:
- Identify the Cycle Detection And Connectivity signal before choosing a template.
- State the invariant for Graph Valid Tree: combines no-cycle and connected requirements.
- Handle disconnected components, cycles, duplicate enqueues, and directed versus undirected edges.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Graph Valid Tree toward Union Find, topological sort, Dijkstra, dynamic programming, or backtracking?
- Which disconnected components case would break the first implementation?
- Can the Cycle Detection And Connectivity invariant survive streaming input, in-place restrictions, or lower memory limits?

## 8. Number of Connected Components in an Undirected Graph

LeetCode: [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

Difficulty: Medium

Pattern: Connected Components

Why It Matters: Baseline component counting.

Skills Tested:
- Identify the Connected Components signal before choosing a template.
- State the invariant for Number of Connected Components in an Undirected Graph: baseline component counting.
- Handle disconnected components, cycles, duplicate enqueues, and directed versus undirected edges.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Number of Connected Components in an Undirected Graph toward Union Find, topological sort, Dijkstra, dynamic programming, or backtracking?
- Which disconnected components case would break the first implementation?
- Can the Connected Components invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
