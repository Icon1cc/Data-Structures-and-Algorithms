# Trees Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

A tree is an acyclic connected graph with a root in rooted tree problems. Each node can have children, and a binary tree has at most two children.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Traversal | O(n) |
| Balanced BST search | O(log n) |
| Skewed BST search | O(n) |
| LCA general tree | O(n) |

## Space Table

| Case | Complexity |
|---|---:|
| Balanced recursive DFS | O(log n) stack |
| Skewed recursive DFS | O(n) stack |
| BFS queue | O(width) |

## Pattern Summary

| Pattern | Use When |
|---|---|
| Recursive DFS | Use for height, diameter, balance, path sums, and subtree checks. |
| Iterative DFS | Use when recursion depth is risky or traversal state must be customized. |
| BFS Level Order | Use for level order, right side view, minimum depth, and nearest target. |
| Path Problems | Use for root-to-leaf sums, all paths, and ancestor-dependent checks. |
| Tree DP | Use for rob/not rob, max path, cameras, and subtree optimization. |
| Lowest Common Ancestor | Use for ancestor questions in binary trees and BSTs. |
| BST Bounds | Use for validation, search, insert, and kth-order traversal. |

## Recognition Hints

Look for subtree, ancestor, descendant, path sum, balanced, diameter, serialize, kth in BST, level order, or lowest common ancestor.

## Templates

### Recursive DFS

```text
def dfs(node):
    if not node: return base
    left = dfs(node.left)
    right = dfs(node.right)
    return combine(node, left, right)
```

### Iterative DFS

```text
stack = [root]
while stack:
    node = stack.pop()
    process(node)
    push children in reverse visit order
```

### BFS Level Order

```text
queue = deque([root])
while queue:
    for _ in range(len(queue)):
        node = queue.popleft()
```

### Path Problems

```text
path.append(node.val)
explore children
path.pop()
```

## Common Traps

- Using global state without defining when it updates.
- Returning the wrong value from recursive helpers.
- Forgetting null base cases.
- Assuming a binary tree is a BST.

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
