# Linked List Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern Selection Table

| Pattern | Strongest Signal | Avoid When |
|---|---|---|
| Dummy Head | delete head | Do not expose the dummy as part of the returned list |
| Two Pointer Gap | nth from end | Do not use when the list length can be shorter without guarding null |
| Fast And Slow Pointers | cycle | Do not use when random access or length is already cheaper |
| In-place Reversal | reverse | Do not use when node identity order must remain unchanged |
| Merge Lists | merge sorted | Do not allocate new nodes if the problem expects node reuse |

## Pattern: Dummy Head

### Beginner Intuition

Add a stable node before the real head so head edits become ordinary edits.

### When To Use It

Use for deletion, insertion, merging, and partitioning near the head.

### When Not To Use It

Do not expose the dummy as part of the returned list.

### Recognition Signals

- delete head
- merge
- sentinel
- dummy

### Example Problems

- Merge Two Sorted Lists
- Remove Nth Node From End of List

### Common Mistakes

- Returning dummy instead of dummy.next.
- Ignoring the exclusion case for Dummy Head: Do not expose the dummy as part of the returned list.
- Failing to test empty lists, head replacement, tail links, cycles, and pointer save order against the stated invariant.

### Pseudocode Or Template

```text
dummy = ListNode(0, head)
prev = dummy
# mutate prev.next safely
return dummy.next
```

### Complexity Notes

O(n) time, O(1) space for traversal edits.

### Interview Explanation

The dummy removes special cases because every real node has a predecessor.

## Pattern: Two Pointer Gap

### Beginner Intuition

Advance one pointer k steps so the distance between pointers encodes the target.

### When To Use It

Use for nth from end and fixed-distance deletion.

### When Not To Use It

Do not use when the list length can be shorter without guarding null.

### Recognition Signals

- nth from end
- fixed gap
- distance

### Example Problems

- Remove Nth Node From End of List

### Common Mistakes

- Advancing past null when n equals length.
- Ignoring the exclusion case for Two Pointer Gap: Do not use when the list length can be shorter without guarding null.
- Failing to test empty lists, head replacement, tail links, cycles, and pointer save order against the stated invariant.

### Pseudocode Or Template

```text
fast = slow = dummy
for _ in range(n): fast = fast.next
while fast.next:
    fast = fast.next
    slow = slow.next
```

### Complexity Notes

O(n) time, O(1) space.

### Interview Explanation

When fast reaches the end, slow is exactly before the node to remove.

## Pattern: Fast And Slow Pointers

### Beginner Intuition

Use speed difference to find middle or detect a cycle.

### When To Use It

Use for cycle detection, palindrome split, and middle node.

### When Not To Use It

Do not use when random access or length is already cheaper.

### Recognition Signals

- cycle
- middle
- slow fast

### Example Problems

- Linked List Cycle
- Middle of the Linked List

### Common Mistakes

- Not checking fast and fast.next before moving two steps.
- Ignoring the exclusion case for Fast And Slow Pointers: Do not use when random access or length is already cheaper.
- Failing to test empty lists, head replacement, tail links, cycles, and pointer save order against the stated invariant.

### Pseudocode Or Template

```text
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### Complexity Notes

O(n) time, O(1) space.

### Interview Explanation

The speed difference makes cycle detection inevitable if a cycle exists.

## Pattern: In-place Reversal

### Beginner Intuition

Flip links one at a time while preserving the next node before mutation.

### When To Use It

Use for reverse list, reverse sublist, and palindrome checks.

### When Not To Use It

Do not use when node identity order must remain unchanged.

### Recognition Signals

- reverse
- prev current next
- in place

### Example Problems

- Reverse Linked List
- Reverse Nodes in k-Group

### Common Mistakes

- Losing next before reassigning current.next.
- Ignoring the exclusion case for In-place Reversal: Do not use when node identity order must remain unchanged.
- Failing to test empty lists, head replacement, tail links, cycles, and pointer save order against the stated invariant.

### Pseudocode Or Template

```text
prev = None
cur = head
while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
```

### Complexity Notes

O(n) time, O(1) space.

### Interview Explanation

I save next first, then flip current to point backward.

## Pattern: Merge Lists

### Beginner Intuition

Repeatedly attach the smaller current node and advance that list.

### When To Use It

Use for sorted lists and k-way merge with a heap.

### When Not To Use It

Do not allocate new nodes if the problem expects node reuse.

### Recognition Signals

- merge sorted
- attach
- tail

### Example Problems

- Merge Two Sorted Lists
- Merge k Sorted Lists

### Common Mistakes

- Forgetting to attach the remaining tail after one list ends.
- Ignoring the exclusion case for Merge Lists: Do not allocate new nodes if the problem expects node reuse.
- Failing to test empty lists, head replacement, tail links, cycles, and pointer save order against the stated invariant.

### Pseudocode Or Template

```text
tail = dummy
while a and b:
    attach smaller node to tail
attach remaining a or b
```

### Complexity Notes

O(n + m) for two lists, O(N log k) for k lists with heap.

### Interview Explanation

The merged prefix is always sorted and tail points to its end.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
