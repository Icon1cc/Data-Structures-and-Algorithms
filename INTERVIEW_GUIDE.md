# Interview Guide

This guide explains how to turn data structures and algorithms knowledge into interview performance.

## How Coding Interviews Work

A typical coding interview is 35 to 50 minutes. The interviewer gives a problem, expects clarifying questions, watches how you reason, and evaluates both the final code and the path you took to reach it.

The usual flow is:

1. Clarify input, output, constraints, and edge cases.
2. Propose a brute force solution.
3. Identify wasted work.
4. Choose a data structure or algorithmic pattern.
5. Explain the optimized approach.
6. Code while narrating important decisions.
7. Test with examples and edge cases.
8. Analyze time and space complexity.

## What Interviewers Evaluate

Interviewers usually care about:

- Problem understanding.
- Pattern recognition.
- Correctness and edge-case handling.
- Code clarity.
- Communication.
- Complexity analysis.
- Ability to respond to hints.
- Debugging discipline.

They are not only checking whether you have seen the exact problem before.

## Communication Strategy

Start with concise questions. Then state your assumptions. Keep the interviewer synchronized with your reasoning, especially when you change approach.

Useful phrases:

- "I want to confirm whether the input can be empty."
- "A brute force approach would be..."
- "The repeated work is..."
- "The invariant I want to maintain is..."
- "This data structure helps because..."
- "Before coding, I will test this against..."

## Clarification Questions

Ask questions that change the algorithm or edge cases:

- Can the input be empty?
- Are values unique?
- Are values sorted?
- Are negative numbers allowed?
- Can there be duplicates?
- Is the graph directed or undirected?
- Are edge weights non-negative?
- Should the answer preserve input order?
- What should happen if no valid answer exists?
- Are we optimizing for time, space, or both?

## Brute Force To Optimized Thinking

Do not skip brute force. Brute force reveals the search space.

A good optimization path looks like this:

1. State the brute force idea.
2. Name the repeated work.
3. Ask what summary would remove that work.
4. Choose a pattern.
5. State the invariant.
6. Derive complexity.

Example:

- Brute force checks every pair in O(n^2).
- The repeated work is searching for a complement.
- A hash map stores previous values.
- The invariant is that `seen` contains exactly the values before the current index.
- The optimized solution is O(n) time and O(n) space.

## Complexity Analysis

Be precise:

- Time complexity counts how many operations grow with input size.
- Space complexity counts auxiliary memory, including recursion stack.
- Sorting is usually O(n log n).
- Hash maps are expected O(1) per operation, but can degrade in pathological cases.
- BFS and DFS over graphs are O(V + E).
- Dynamic programming is usually number of states times transition cost.

## Common Mistakes

- Coding before clarifying constraints.
- Memorizing solutions without understanding invariants.
- Using DFS for shortest path in an unweighted graph when BFS is needed.
- Using Dijkstra with negative weights.
- Forgetting duplicates in sorted two-pointer problems.
- Missing empty input and single-element cases.
- Claiming O(1) space while recursion uses O(n) stack.
- Treating a greedy idea as correct without proof.
- Compressing DP state before the recurrence is stable.

## Mock Interview Strategy

Use mocks to practice execution, not only correctness.

- Week 1 to 2: untimed walkthroughs with full explanation.
- Week 3 to 4: one 45-minute timed problem twice per week.
- Week 5 onward: two full mocks per week.
- After every mock, write what failed and which pattern would have helped.
- Redo the same problem after 3 days without reading the old code.

## Revision Strategy

Use spaced repetition:

- Same day: rewrite the solution idea without code.
- Next day: re-solve from scratch.
- One week later: re-solve under time pressure.
- One month later: explain the pattern and solve a variant.

## Interview Day Checklist

- Read the prompt twice.
- Clarify constraints before solving.
- State brute force.
- Name the pattern.
- Maintain an invariant.
- Code in small, testable chunks.
- Test normal, edge, and adversarial cases.
- Give exact complexity.


---

## Navigation

[Previous](STUDY_PLAN.md) | [Home](README.md) | [Next](REPO_INDEX.md)
