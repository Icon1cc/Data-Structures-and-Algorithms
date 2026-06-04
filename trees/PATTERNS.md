# Trees Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern: Recursive DFS

### Beginner Intuition

Let each call solve one subtree and return a value to its parent.

### When To Use It

Use for height, diameter, balance, path sums, and subtree checks.

### When Not To Use It

Do not use recursion blindly if depth can exceed stack limits.

### Recognition Signals

- subtree
- recursive return
- height

### Example Problems

- Maximum Depth of Binary Tree
- Diameter of Binary Tree

### Common Mistakes

- Returning global answer instead of the local value the parent needs.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
def dfs(node):
    if not node: return base
    left = dfs(node.left)
    right = dfs(node.right)
    return combine(node, left, right)
```

### Complexity Notes

O(n) time, O(height) stack.

### Interview Explanation

I define exactly what dfs(node) returns before writing combine logic.

## Pattern: Iterative DFS

### Beginner Intuition

Use an explicit stack to control traversal order without recursion.

### When To Use It

Use when recursion depth is risky or traversal state must be customized.

### When Not To Use It

Do not use if recursive code is clearer and depth is safe.

### Recognition Signals

- explicit stack
- preorder
- inorder

### Example Problems

- Binary Tree Inorder Traversal
- Validate Binary Search Tree

### Common Mistakes

- Pushing children in the wrong order for the desired traversal.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
stack = [root]
while stack:
    node = stack.pop()
    process(node)
    push children in reverse visit order
```

### Complexity Notes

O(n) time, O(height to n) space.

### Interview Explanation

The explicit stack is the call stack made visible.

## Pattern: BFS Level Order

### Beginner Intuition

Use a queue to process nodes by depth.

### When To Use It

Use for level order, right side view, minimum depth, and nearest target.

### When Not To Use It

Do not use DFS when shortest edge count by level is required.

### Recognition Signals

- level
- depth
- queue
- right side

### Example Problems

- Binary Tree Level Order Traversal
- Binary Tree Right Side View

### Common Mistakes

- Mixing nodes from different levels by not capturing level size.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
queue = deque([root])
while queue:
    for _ in range(len(queue)):
        node = queue.popleft()
```

### Complexity Notes

O(n) time, O(width) space.

### Interview Explanation

Capturing the queue size freezes the current level.

## Pattern: Path Problems

### Beginner Intuition

Carry path state from root to current and restore it when returning.

### When To Use It

Use for root-to-leaf sums, all paths, and ancestor-dependent checks.

### When Not To Use It

Do not keep one mutable path without undoing after recursion.

### Recognition Signals

- path sum
- root to leaf
- ancestors

### Example Problems

- Path Sum II
- Binary Tree Maximum Path Sum

### Common Mistakes

- Appending live path objects instead of copies.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
path.append(node.val)
explore children
path.pop()
```

### Complexity Notes

O(n) time plus output, O(height) stack.

### Interview Explanation

The path represents ancestors of the current node only.

## Pattern: Tree DP

### Beginner Intuition

Compute multiple values per node so parent decisions have enough information.

### When To Use It

Use for rob/not rob, max path, cameras, and subtree optimization.

### When Not To Use It

Do not collapse state if parent needs to know different choices.

### Recognition Signals

- choose skip
- subtree optimum
- two returns

### Example Problems

- House Robber III
- Binary Tree Cameras

### Common Mistakes

- Returning only the best value when parent needs selected and unselected cases.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
take_left, skip_left = dfs(node.left)
take_right, skip_right = dfs(node.right)
return take_node, skip_node
```

### Complexity Notes

O(n) time, O(height) stack.

### Interview Explanation

I return a small tuple that represents all states the parent may need.

## Pattern: Lowest Common Ancestor

### Beginner Intuition

Return a node when a subtree contains one target or the answer.

### When To Use It

Use for ancestor questions in binary trees and BSTs.

### When Not To Use It

Do not use BST ordering on a non-BST.

### Recognition Signals

- ancestor
- p and q
- split point

### Example Problems

- Lowest Common Ancestor of a Binary Tree
- Lowest Common Ancestor of a BST

### Common Mistakes

- Continuing past the split point in a BST.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
if not node or node in {p, q}: return node
left = dfs(node.left)
right = dfs(node.right)
if left and right: return node
return left or right
```

### Complexity Notes

O(n) general tree, O(height) BST.

### Interview Explanation

If one target is found on each side, the current node is the first common ancestor.

## Pattern: BST Bounds

### Beginner Intuition

Carry lower and upper allowed values through recursion.

### When To Use It

Use for validation, search, insert, and kth-order traversal.

### When Not To Use It

Do not validate a BST by comparing only parent and child.

### Recognition Signals

- BST
- lower upper bounds
- inorder sorted

### Example Problems

- Validate Binary Search Tree
- Kth Smallest Element in a BST

### Common Mistakes

- Allowing equality on the wrong side when duplicates are not allowed.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
def valid(node, lo, hi):
    if not node: return True
    return lo < node.val < hi and valid(node.left, lo, node.val) and valid(node.right, node.val, hi)
```

### Complexity Notes

O(n) validation, O(height) search in balanced BST.

### Interview Explanation

Every node must satisfy all ancestor bounds, not only its parent.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
