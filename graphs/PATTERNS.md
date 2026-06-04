# Graphs Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern: DFS Traversal

### Beginner Intuition

Explore as far as possible before backtracking.

### When To Use It

Use for components, cycle detection, island shape, and reachability.

### When Not To Use It

Do not use recursive DFS blindly on very deep graphs.

### Recognition Signals

- reachability
- component
- deep explore

### Example Problems

- Number of Islands
- Clone Graph

### Common Mistakes

- Marking visited after recursive calls, allowing cycles to recurse forever.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
def dfs(node):
    if node in visited: return
    visited.add(node)
    for nei in graph[node]: dfs(nei)
```

### Complexity Notes

O(V + E) time, O(V) space.

### Interview Explanation

Visited prevents repeat work and makes cycles safe.

## Pattern: BFS Traversal

### Beginner Intuition

Explore nodes in distance layers from the start.

### When To Use It

Use for shortest path in unweighted graphs and level spread.

### When Not To Use It

Do not use DFS when minimum edge count is required.

### Recognition Signals

- shortest unweighted
- level
- queue

### Example Problems

- Rotting Oranges
- Word Ladder

### Common Mistakes

- Marking visited on pop instead of enqueue, causing duplicates.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
queue = deque([start])
visited = {start}
while queue:
    node = queue.popleft()
    for nei in graph[node]: enqueue unseen
```

### Complexity Notes

O(V + E) time, O(V) space.

### Interview Explanation

The first time BFS reaches a node is the shortest unweighted distance.

## Pattern: Connected Components

### Beginner Intuition

Restart traversal from every unvisited node and count or collect groups.

### When To Use It

Use for islands, provinces, and disconnected graphs.

### When Not To Use It

Do not assume a graph is connected unless stated.

### Recognition Signals

- components
- provinces
- islands

### Example Problems

- Number of Connected Components in an Undirected Graph
- Number of Provinces

### Common Mistakes

- Forgetting to scan every node after one traversal.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
for node in nodes:
    if node not in visited:
        components += 1
        dfs(node)
```

### Complexity Notes

O(V + E) time.

### Interview Explanation

Each restart discovers exactly one previously unseen component.

## Pattern: Cycle Detection

### Beginner Intuition

Track visiting state or parent relationships to detect cycles.

### When To Use It

Use for directed course prerequisites and undirected graph validation.

### When Not To Use It

Do not use the same rule for directed and undirected cycles.

### Recognition Signals

- cycle
- visiting
- prerequisites
- parent

### Example Problems

- Course Schedule
- Graph Valid Tree

### Common Mistakes

- Treating an undirected edge back to parent as a cycle.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
state: 0 unseen, 1 visiting, 2 done
if neighbor is visiting: cycle
```

### Complexity Notes

O(V + E) time, O(V) space.

### Interview Explanation

A directed cycle exists when DFS reaches a node already on the current recursion path.

## Pattern: Topological Sort

### Beginner Intuition

Order DAG nodes so every prerequisite appears before dependents.

### When To Use It

Use for scheduling, course order, build dependencies, and alien dictionary.

### When Not To Use It

Do not use topological sort if cycles are allowed in a valid answer.

### Recognition Signals

- DAG
- prerequisites
- dependency order

### Example Problems

- Course Schedule II
- Alien Dictionary

### Common Mistakes

- Not detecting that fewer output nodes than total means a cycle.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
queue = nodes with indegree 0
while queue:
    node = pop
    for nei in graph[node]: reduce indegree
```

### Complexity Notes

O(V + E) time, O(V) space.

### Interview Explanation

Indegree zero nodes have no remaining prerequisites, so they are safe next.

## Pattern: Union Find

### Beginner Intuition

Maintain components under edge additions with parent pointers.

### When To Use It

Use for connectivity queries, redundant edges, and MST Kruskal.

### When Not To Use It

Do not use when you need actual path order or shortest distance.

### Recognition Signals

- connectivity
- union
- components
- redundant

### Example Problems

- Redundant Connection
- Accounts Merge

### Common Mistakes

- Forgetting path compression or union by rank on large inputs.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]
def union(a, b): connect roots
```

### Complexity Notes

Almost O(1) amortized per operation.

### Interview Explanation

Union Find answers whether two nodes already belong to the same component.

## Pattern: Grid Graph BFS

### Beginner Intuition

Treat each cell as a node and legal moves as edges.

### When To Use It

Use for islands, rotting spread, walls and gates, and shortest grid paths.

### When Not To Use It

Do not build an explicit graph when neighbor generation is simple.

### Recognition Signals

- grid
- cells
- four directions
- shortest spread

### Example Problems

- Flood Fill
- Shortest Path in Binary Matrix

### Common Mistakes

- Mixing row and column bounds.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
for dr, dc in directions:
    nr, nc = r + dr, c + dc
    if inside and valid: visit
```

### Complexity Notes

O(rows * cols) time and space.

### Interview Explanation

The grid is the graph, so neighbor generation replaces adjacency construction.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
