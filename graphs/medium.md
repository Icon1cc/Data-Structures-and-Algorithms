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

Pattern: Connected Components Via DFS Or BFS

Why It Matters: The canonical grid component problem.

Skills Tested:
- Recognize that each contiguous land region is one island, so a sweep over cells launches a DFS or BFS from each unvisited land cell.
- State the invariant: every land cell is eventually visited and marked, and the answer increments once per launch.
- Choose between mutating the grid (O(1) extra) and a separate visited matrix (O(M * N) extra).
- Time O(M * N), space O(M * N) recursion or queue.

Common Follow-Ups:
- Max Area of Island (LC 695) returns the size of the largest region.
- Number of Distinct Islands (LC 694) hashes shape signatures.
- Online variant: Number of Islands II (LC 305) uses union-find with incremental land additions.

## 2. Clone Graph

LeetCode: [Clone Graph](https://leetcode.com/problems/clone-graph/)

Difficulty: Medium

Pattern: DFS/BFS With Identity Map

Why It Matters: Tests graph copying and visited mapping.

Skills Tested:
- Recognize that cloning needs both a traversal (visit every node) and an identity map (original to clone) to wire neighbors correctly.
- State the invariant: every node visited has a clone in the map; recursive calls return existing clones to break cycles.
- Build the clone before recursing into neighbors so cycles do not loop forever.
- Time O(V + E), space O(V) for the map.

Common Follow-Ups:
- Copy List with Random Pointer (LC 138) is the same identity-mapping idea on a linked list.
- What if some nodes carry serialized payloads that must be deep-copied.
- Stream the cloning when only part of the graph is reachable.

## 3. Course Schedule

LeetCode: [Course Schedule](https://leetcode.com/problems/course-schedule/)

Difficulty: Medium

Pattern: Topological Sort Or DFS Cycle Detection

Why It Matters: Classic directed cycle detection.

Skills Tested:
- Recognize that "can finish all courses" is "is the prerequisite graph acyclic", which is detected by Kahn's BFS topo-sort or three-color DFS.
- State the invariant (BFS): nodes are added to the queue only when their indegree drops to zero; if not all nodes are processed, a cycle exists.
- For DFS, use white/gray/black colors; encountering a gray node signals a back edge (cycle).
- Time O(V + E), space O(V + E).

Common Follow-Ups:
- Course Schedule II (LC 210) returns one valid topo order.
- Course Schedule III (LC 630) is a greedy with a heap.
- What if courses can be partially completed.

## 4. Rotting Oranges

LeetCode: [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

Difficulty: Medium

Pattern: Multi-Source BFS

Why It Matters: Models simultaneous spread by levels.

Skills Tested:
- Recognize that all initially rotten oranges spread at the same rate, which is multi-source BFS where the queue starts with all sources.
- State the invariant: at minute `t`, every cell in the queue rots at minute `t + 1`; the answer is the maximum minute reached or `-1` if any fresh remains.
- Track fresh count; decrement when a cell rots; non-zero remainder yields `-1`.
- Time O(M * N), space O(M * N).

Common Follow-Ups:
- 01 Matrix (LC 542) computes distances from any zero using multi-source BFS.
- As Far From Land As Possible (LC 1162) reverses the grid pattern.
- What if rot speed varies per cell.

## 5. Pacific Atlantic Water Flow

LeetCode: [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)

Difficulty: Medium

Pattern: Reverse BFS/DFS From Boundaries

Why It Matters: Tests reachability from boundaries.

Skills Tested:
- Recognize that flowing from a cell to an ocean is hard to verify forward, but flowing backward from each ocean (only ascending heights are reachable) marks every cell that can reach that ocean.
- State the invariant: two visited sets, one per ocean; the answer is their intersection.
- Start BFS/DFS from all boundary cells of each ocean simultaneously.
- Time O(M * N), space O(M * N).

Common Follow-Ups:
- Surrounded Regions (LC 130) uses a similar boundary-then-mark technique.
- What if there are diagonal flows.
- Generalize to k oceans with priorities.

## 6. Surrounded Regions

LeetCode: [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)

Difficulty: Medium

Pattern: Boundary-Reachable Components

Why It Matters: Distinguishes safe regions from captured ones.

Skills Tested:
- Recognize that an `O` is captured unless it is connected (through other `O`s) to a boundary `O`, which is a reachability query from boundary `O`s.
- State the invariant: any `O` reached during the boundary BFS/DFS is safe; the rest are flipped to `X` after the sweep.
- Use a sentinel marker (`#`) during traversal so the final flip is straightforward.
- Time O(M * N), space O(M * N).

Common Follow-Ups:
- Number of Enclaves (LC 1020) counts captured land cells.
- Pacific Atlantic Water Flow (LC 417) reuses boundary-source traversal.
- What if regions can also be captured by certain colors of boundaries.

## 7. Graph Valid Tree

LeetCode: [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)

Difficulty: Medium

Pattern: Connectivity Plus Edge Count

Why It Matters: Combines no-cycle and connected requirements.

Skills Tested:
- Recognize that a valid tree on `n` nodes has exactly `n - 1` edges and is connected; either union-find or DFS handles it.
- State the invariant (UF): every union must succeed (no cycle); after processing all edges, the count of components must be 1.
- Short-circuit early: if `len(edges) != n - 1`, return false.
- Time O(V + E), space O(V).

Common Follow-Ups:
- Number of Connected Components (LC 323) is the component-counting cousin.
- What if the graph is directed (a tree must have a single root with indegree 0).
- Online updates: support edge additions and a "still a tree" query.

## 8. Number of Connected Components in an Undirected Graph

LeetCode: [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

Difficulty: Medium

Pattern: Union-Find Component Count

Why It Matters: Baseline component counting.

Skills Tested:
- Recognize that union-find with path compression and union-by-rank handles dynamic edge insertion in near-constant time per op.
- State the invariant: after every union, components reflect all edges processed so far; the count starts at `n` and decreases by one per successful union.
- Alternative: DFS/BFS over an adjacency list; both approaches are O(V + E).
- Use UF when edges are streamed; use DFS when the full graph is static.

Common Follow-Ups:
- Number of Provinces (LC 547) is the same problem with an adjacency-matrix input.
- What if edge weights matter (minimum spanning forest).
- Online deletion is hard with union-find; how would you support it.

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
