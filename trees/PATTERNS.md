# Trees Patterns

This file is the main pattern-recognition reference for trees. Each pattern explains why it works, when it fits, when to avoid it, and how to start coding it.

## Pattern: Recursive DFS

### Intuition

Let each recursive call solve one subtree and return exactly the fact the parent needs.

### When To Use It

Use for height, path sums, validation, subtree checks, and postorder aggregation.

### When Not To Use It

Do not use recursion blindly when tree depth may exceed language limits.

### Recognition Signals

- recursive dfs
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Binary Tree Level Order Traversal
- Validate Binary Search Tree

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
def dfs(node):
    if not node: return base
    left = dfs(node.left)
    right = dfs(node.right)
    return combine(node, left, right)
```

## Pattern: Iterative DFS

### Intuition

Use an explicit stack to control depth-first traversal and avoid recursive stack limits.

### When To Use It

Use for preorder, inorder, postorder simulations, and deep trees.

### When Not To Use It

Do not make the stack state so complex that recursion would be clearer and safe.

### Recognition Signals

- iterative dfs
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Validate Binary Search Tree
- Binary Tree Maximum Path Sum

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
stack = [root]
while stack:
    node = stack.pop()
    push children in desired order
```

## Pattern: Level Order BFS

### Intuition

Use a queue to process all nodes at the same depth before moving deeper.

### When To Use It

Use for level order, minimum depth, right side view, and shortest tree distance.

### When Not To Use It

Do not use when the parent needs child summaries before processing itself.

### Recognition Signals

- level order bfs
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Binary Tree Maximum Path Sum
- Binary Tree Level Order Traversal

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
queue = deque([root])
while queue:
    for _ in range(len(queue)):
        node = queue.popleft()
```

## Pattern: BST Invariant

### Intuition

Every node carries lower and upper bounds inherited from its ancestors.

### When To Use It

Use for BST validation, search, kth smallest, and range queries.

### When Not To Use It

Do not compare only a node with its immediate parent.

### Recognition Signals

- bst invariant
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Binary Tree Level Order Traversal
- Validate Binary Search Tree

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
def valid(node, low, high):
    if not node: return True
    return low < node.val < high and valid(node.left, low, node.val) and valid(node.right, node.val, high)
```

## Pattern: Lowest Common Ancestor

### Intuition

The answer is where target paths split, or where one target is ancestor of the other.

### When To Use It

Use for ancestor queries in binary trees and BSTs.

### When Not To Use It

Do not ignore the case where root is one of the targets.

### Recognition Signals

- lowest common ancestor
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Validate Binary Search Tree
- Binary Tree Maximum Path Sum

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
if root in (p, q): return root
left = dfs(root.left); right = dfs(root.right)
if left and right: return root
return left or right
```

## Pattern: Tree DP

### Intuition

Return multiple states from each subtree so the parent can choose among them.

### When To Use It

Use for maximum path, cameras, robbing nodes, and subtree optimization.

### When Not To Use It

Do not force a single return value when parent decisions need more context.

### Recognition Signals

- tree dp
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Binary Tree Maximum Path Sum
- Binary Tree Level Order Traversal

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
def dfs(node):
    left_state = dfs(node.left)
    right_state = dfs(node.right)
    return states_for_parent
```
---

## Navigation

[Previous](../trees/CHEATSHEET.md) | [Home](../README.md) | [Next](../trees/easy.md)
