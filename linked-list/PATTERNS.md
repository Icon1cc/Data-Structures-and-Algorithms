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

- Returning `dummy` instead of `dummy.next`; the caller receives the sentinel and prints garbage.
- Forgetting to set `dummy.next = head` at construction; the dummy floats with no connection to the input.
- Treating the dummy as immutable; sometimes you must rewire `dummy.next` directly when the new head changes.

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

- Walking past null when `n` equals or exceeds the list length; guard the inner loop with `fast` non-null.
- Stopping when `fast` is null instead of when `fast.next` is null; the latter leaves `slow` pointing one before the target.
- Removing the head without a dummy node; the head case becomes a special branch you can avoid entirely.

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

- Skipping the `fast.next` null guard before `fast.next.next`, crashing on odd-length lists.
- Returning the meeting point as the cycle entrance; a second walk from `head` and `meet` lands at the entrance.
- Confusing the two middle conventions: `while fast and fast.next` returns the second middle for even length; `while fast.next and fast.next.next` returns the first.

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

- Reassigning `cur.next = prev` before saving `cur.next`, which orphans the rest of the list.
- Returning `cur` (now null) instead of `prev` (the new head) at loop end.
- Forgetting to splice the reversed segment back into the original list when reversing only a sublist.

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

- Forgetting to attach the leftover tail of the longer list after the loop exits.
- Comparing `a < b` on nodes when you meant `a.val < b.val`; nodes do not implement comparison by default.
- Pushing a heap of nodes without a tiebreak in tuples; equal values force a node-comparison error in Python.

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
