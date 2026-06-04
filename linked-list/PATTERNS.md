# Linked List Patterns

This file is the main pattern-recognition reference for linked list. Each pattern explains why it works, when it fits, when to avoid it, and how to start coding it.

## Pattern: Dummy Head

### Intuition

Add a sentinel node before the real head so deleting or inserting near the head has the same logic as every other position.

### When To Use It

Use when the head can change or when list construction needs a stable tail pointer.

### When Not To Use It

Do not use it as a substitute for understanding which real node should be returned.

### Recognition Signals

- dummy head
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Add Two Numbers
- Copy List with Random Pointer

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
dummy = Node(0)
dummy.next = head
prev = dummy
# mutate prev.next
return dummy.next
```

## Pattern: Fast and Slow Pointers

### Intuition

Move two references at different speeds or with a fixed gap to reveal cycles, middles, and nth-from-end positions.

### When To Use It

Use for linked-list cycles, middle nodes, palindrome splits, and kth-from-end deletion.

### When Not To Use It

Do not use when random access makes a simpler index calculation available.

### Recognition Signals

- fast and slow pointers
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Copy List with Random Pointer
- Reverse Nodes in k-Group

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

## Pattern: In-place Reversal

### Intuition

Reverse links one node at a time while preserving the next node before rewiring.

### When To Use It

Use for full reversal, sublist reversal, and k-group reversal.

### When Not To Use It

Do not use recursively when list length can exceed the call stack.

### Recognition Signals

- in-place reversal
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Reverse Nodes in k-Group
- Add Two Numbers

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
prev = None
curr = head
while curr:
    nxt = curr.next
    curr.next = prev
    prev, curr = curr, nxt
```

## Pattern: Merge Lists

### Intuition

Always attach the smaller available head from sorted lists and advance that source.

### When To Use It

Use for sorted linked lists, sorted arrays, and k-way merge with a heap.

### When Not To Use It

Do not use if the inputs are not sorted by the same key.

### Recognition Signals

- merge lists
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Add Two Numbers
- Copy List with Random Pointer

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
tail = dummy
while a and b:
    attach the smaller node
attach the remaining tail
```

## Pattern: Cycle Detection

### Intuition

A faster pointer eventually catches a slower pointer if a cycle exists.

### When To Use It

Use for linked lists and functional graphs where each node has one next state.

### When Not To Use It

Do not use plain Floyd logic on general graphs with many outgoing edges.

### Recognition Signals

- cycle detection
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Copy List with Random Pointer
- Reverse Nodes in k-Group

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
slow = fast = start
while fast and next(fast):
    slow = next(slow)
    fast = next(next(fast))
```

## Pattern: Copy with Random Pointer

### Intuition

Create a mapping from original node identity to cloned node, then wire next and random references.

### When To Use It

Use when nodes have extra cross references that must be deep-copied.

### When Not To Use It

Do not key the map by value because values may repeat.

### Recognition Signals

- copy with random pointer
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Reverse Nodes in k-Group
- Add Two Numbers

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
old_to_new = {None: None}
for node in nodes: old_to_new[node] = Node(node.val)
for node in nodes: wire clone links
```
---

## Navigation

[Previous](../linked-list/CHEATSHEET.md) | [Home](../README.md) | [Next](../linked-list/easy.md)
