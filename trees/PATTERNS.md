# Trees Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern Selection Table

| Pattern | Strongest Signal | Avoid When |
|---|---|---|
| Recursive DFS | subtree | Do not use recursion blindly if depth can exceed stack limits |
| Iterative DFS | explicit stack | Do not use if recursive code is clearer and depth is safe |
| BFS Level Order | level | Do not use DFS when shortest edge count by level is required |
| Path Problems | path sum | Do not keep one mutable path without undoing after recursion |
| Tree DP | choose skip | Do not collapse state if parent needs to know different choices |
| Lowest Common Ancestor | ancestor | Do not use BST ordering on a non-BST |
| BST Bounds | BST | Do not validate a BST by comparing only parent and child |

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

- Returning the global answer (e.g., diameter) when the parent needs the local height to combine.
- Updating the global answer before recursing into both children, which loses the through-node candidate.
- Returning before the null base case; missing `if not node: return base` is the most common bug source.

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

- Pushing children left-then-right when you wanted preorder; the LIFO stack reverses the order.
- For iterative inorder, walking left forever without pushing each visited node onto the stack.
- Mutating the tree while iterating; if the structure changes mid-traversal, your stack invariant breaks.

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

- Reading `len(queue)` inside the inner loop, which sees the changing size and mixes levels.
- Forgetting to skip null children before enqueueing; the queue fills with nulls and corrupts level counts.
- Using a list instead of a deque; `pop(0)` on a list is O(n) per call and turns the BFS into O(n^2).

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

- Appending the live `path` list to results instead of `path[:]`; later mutations corrupt the saved answer.
- Forgetting to `path.pop()` after recursing; the path bleeds into siblings of the recursion subtree.
- Treating "path" as "any sequence" when the problem requires root-to-leaf; check the leaf condition explicitly.

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

- Caching by node value instead of node identity; same-value subtrees can mislead the cache.
- Returning only the optimum when the parent must combine "this node included" with "this node excluded".
- Forgetting that null returns must contribute neutral values (0 for sums, `(0, 0)` for tuple states).

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

- Returning the first match without checking both subtrees; without that, an ancestor of `p` is wrongly returned when `q` lives elsewhere.
- For BST LCA, descending past the split point where one target is left and the other is right; the current node is the answer.
- Failing the case where one node is an ancestor of the other; the recursion still works because the ancestor returns first and propagates upward.

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

- Validating with parent-child comparisons only; a left grandchild may exceed the right grandparent and still pass.
- Using `int(-inf)` or sentinels that fall inside the value range; use Python `-inf, +inf` floats or pass `None` and treat null as no-bound.
- Allowing equality on the wrong side when duplicates are forbidden; usually `low < val < high` (strict).

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
