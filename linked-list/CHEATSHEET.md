# Linked List Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

A linked list is a sequence of nodes where each node stores data and one or more references to neighboring nodes. Access by position is O(n).

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Visit all nodes | O(n) |
| Insert after known node | O(1) |
| Delete after known node | O(1) |
| Find by index | O(n) |

## Space Table

| Case | Complexity |
|---|---:|
| Iterative mutation | O(1) |
| Recursive traversal | O(n) stack |
| Hash visited set | O(n) |

## Pattern Summary

| Pattern | Use When |
|---|---|
| Dummy Head | Use for deletion, insertion, merging, and partitioning near the head. |
| Two Pointer Gap | Use for nth from end and fixed-distance deletion. |
| Fast And Slow Pointers | Use for cycle detection, palindrome split, and middle node. |
| In-place Reversal | Use for reverse list, reverse sublist, and palindrome checks. |
| Merge Lists | Use for sorted lists and k-way merge with a heap. |

## Recognition Hints

Look for head deletion, nth from end, reverse in place, cycle, merge sorted lists, split list, random pointer, or cache eviction.

## Templates

### Dummy Head

```text
dummy = ListNode(0, head)
prev = dummy
# mutate prev.next safely
return dummy.next
```

### Two Pointer Gap

```text
fast = slow = dummy
for _ in range(n): fast = fast.next
while fast.next:
    fast = fast.next
    slow = slow.next
```

### Fast And Slow Pointers

```text
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### In-place Reversal

```text
prev = None
cur = head
while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
```

## Common Traps

- Losing the rest of the list before saving next.
- Forgetting that the head may change.
- Creating cycles accidentally during reversal.
- Using value swaps when node identity matters.

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
