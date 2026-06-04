# Graphs Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

A graph is a set of vertices and edges. Edges may be directed or undirected, weighted or unweighted, explicit or implicit.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Adjacency traversal | O(V + E) |
| Grid traversal | O(rows * cols) |
| Topological sort | O(V + E) |
| Union Find operations | Almost O(1) amortized |

## Space Table

| Case | Complexity |
|---|---:|
| Adjacency list | O(V + E) |
| Visited set | O(V) |
| BFS queue | O(V) |
| DFS stack | O(V) |

## Pattern Summary

| Pattern | Use When |
|---|---|
| DFS Traversal | Use for components, cycle detection, island shape, and reachability. |
| BFS Traversal | Use for shortest path in unweighted graphs and level spread. |
| Connected Components | Use for islands, provinces, and disconnected graphs. |
| Cycle Detection | Use for directed course prerequisites and undirected graph validation. |
| Topological Sort | Use for scheduling, course order, build dependencies, and alien dictionary. |
| Union Find | Use for connectivity queries, redundant edges, and MST Kruskal. |
| Grid Graph BFS | Use for islands, rotting spread, walls and gates, and shortest grid paths. |

## Recognition Hints

Look for connected, reachable, shortest path in unweighted graph, dependencies, courses, islands, components, cycles, clone, or transformation steps.

## Templates

### DFS Traversal

```text
def dfs(node):
    if node in visited: return
    visited.add(node)
    for nei in graph[node]: dfs(nei)
```

### BFS Traversal

```text
queue = deque([start])
visited = {start}
while queue:
    node = queue.popleft()
    for nei in graph[node]: enqueue unseen
```

### Connected Components

```text
for node in nodes:
    if node not in visited:
        components += 1
        dfs(node)
```

### Cycle Detection

```text
state: 0 unseen, 1 visiting, 2 done
if neighbor is visiting: cycle
```

## Common Traps

- Mixing directed and undirected edge handling.
- Marking visited too late in BFS.
- Forgetting disconnected components.
- Using DFS for shortest path in an unweighted graph when BFS is required.

## Interview Reminders

- Say the brute force approach first in one or two sentences.
- State the invariant before coding.
- Test one normal case, one smallest case, and one adversarial case.
- Include auxiliary space, not only input and output size.
- Mention when the pattern assumptions would fail.

## Final Checklist

- [ ] I can define the topic in plain language.
- [ ] I can identify at least three recognition signals.
- [ ] I can write the main template from memory.
- [ ] I can explain time and space complexity.
- [ ] I can name two common mistakes and how to avoid them.

---

## Navigation

[Previous](README.md) | [Home](../README.md) | [Next](PATTERNS.md)
