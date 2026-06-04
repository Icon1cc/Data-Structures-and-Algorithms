# Graphs Patterns

This file is the main pattern-recognition reference for graphs. Each pattern explains why it works, when it fits, when to avoid it, and how to start coding it.

## Pattern: BFS Traversal

### Intuition

Explore by distance layers from a starting node or set of sources.

### When To Use It

Use for shortest path in unweighted graphs and spreading processes.

### When Not To Use It

Do not use BFS alone for weighted shortest paths.

### Recognition Signals

- bfs traversal
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Number of Islands
- Course Schedule

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
queue = deque(sources)
while queue:
    node = queue.popleft()
    push unvisited neighbors
```

## Pattern: DFS Traversal

### Intuition

Explore one branch fully before returning to other branches.

### When To Use It

Use for reachability, components, cycle checks, and flood fill.

### When Not To Use It

Do not omit visited tracking in cyclic graphs.

### Recognition Signals

- dfs traversal
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Course Schedule
- Word Ladder

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
def dfs(node):
    if node in seen: return
    seen.add(node)
    for nei in graph[node]: dfs(nei)
```

## Pattern: Connected Components

### Intuition

Start traversal from every unvisited node and count or label each independent region.

### When To Use It

Use for islands, provinces, account groups, and disconnected graphs.

### When Not To Use It

Do not assume one source reaches every node.

### Recognition Signals

- connected components
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Word Ladder
- Number of Islands

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
count = 0
for node in nodes:
    if node not in seen:
        count += 1
        dfs(node)
```

## Pattern: Grid Graphs

### Intuition

Treat each cell as a node and neighboring cells as edges.

### When To Use It

Use for islands, surrounded regions, walls, and matrix shortest paths.

### When Not To Use It

Do not build explicit adjacency lists unless they simplify the problem.

### Recognition Signals

- grid graphs
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Number of Islands
- Course Schedule

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
for dr, dc in directions:
    nr, nc = r + dr, c + dc
    if in_bounds(nr, nc): visit
```

## Pattern: Union Find

### Intuition

Maintain component parents and merge sets as edges arrive.

### When To Use It

Use for connectivity, redundant edges, MST, and grouping.

### When Not To Use It

Do not use it when path order or shortest path is required.

### Recognition Signals

- union find
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Course Schedule
- Word Ladder

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]
def union(a, b): parent[find(a)] = find(b)
```

## Pattern: Topological Sort

### Intuition

Process nodes only after all prerequisites have been removed.

### When To Use It

Use for course schedules, build order, and DAG processing.

### When Not To Use It

Do not expect a full order if the directed graph has a cycle.

### Recognition Signals

- topological sort
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Word Ladder
- Number of Islands

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
queue = nodes with indegree 0
while queue:
    node = pop
    reduce indegree of neighbors
```
---

## Navigation

[Previous](../graphs/CHEATSHEET.md) | [Home](../README.md) | [Next](../graphs/easy.md)
