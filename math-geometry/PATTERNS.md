# Math & Geometry Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern Selection Table

| Pattern | Strongest Signal | Avoid When |
|---|---|---|
| Modulo Arithmetic | mod | Do not forget negative values may need normalization |
| GCD And LCM | gcd | Do not compute lcm before reducing if overflow is possible |
| Prime Sieve | prime | Do not test divisibility from scratch for every number if n is large |
| Matrix Traversal | matrix | Do not mutate dimensions without checking crossing bounds |
| Coordinate Geometry | slope | Do not compare floating point slopes for exact equality |
| Randomized Prefix | random | Do not use modulo bias when uniform weighted choice is required |

## Pattern: Modulo Arithmetic

### Beginner Intuition

Normalize repeating cycles and keep values inside a bounded range.

### When To Use It

Use for cyclic arrays, clocks, hashes, and large counts.

### When Not To Use It

Do not forget negative values may need normalization.

### Recognition Signals

- mod
- cycle
- wrap around

### Example Problems

- Happy Number
- Add Digits

### Common Mistakes

- Assuming `(-1) % m` equals `m - 1` in C, Java, or JavaScript; only Python returns the non-negative result. Use `((x % m) + m) % m` for portability.
- Combining mod inside an arithmetic expression but skipping it on the running total; intermediate values can overflow.
- Distributing mod across an unsafe operation like division; modular inverse is required for division under a prime modulus.

### Pseudocode Or Template

```text
normalized = ((x % m) + m) % m
```

### Complexity Notes

O(1) per operation.

### Interview Explanation

Modulo preserves remainders, which are the only part that matters in cyclic state.

## Pattern: GCD And LCM

### Beginner Intuition

Use Euclid's algorithm to normalize ratios and divisibility.

### When To Use It

Use for fractions, slopes, grouping by ratio, and common periods.

### When Not To Use It

Do not compute lcm before reducing if overflow is possible.

### Recognition Signals

- gcd
- divisibility
- ratio

### Example Problems

- Greatest Common Divisor of Strings
- Max Points on a Line

### Common Mistakes

- Computing `lcm(a, b) = a * b // gcd(a, b)` directly when `a * b` overflows; reduce first via `a // gcd(a, b) * b`.
- Forgetting to normalize signs when keying slopes; `(2, 3)` and `(-2, -3)` are the same line and need a single canonical form.
- Calling `gcd(0, 0)` and treating the result as 0 silently; some libraries return 0, which makes the "key" hashable but mathematically ambiguous.

### Pseudocode Or Template

```text
while b:
    a, b = b, a % b
```

### Complexity Notes

O(log min(a,b)) time.

### Interview Explanation

GCD gives the canonical unit for a ratio or repeated pattern.

## Pattern: Prime Sieve

### Beginner Intuition

Mark multiples to precompute primality or prime counts.

### When To Use It

Use when many prime queries share an upper bound.

### When Not To Use It

Do not test divisibility from scratch for every number if n is large.

### Recognition Signals

- prime
- count primes
- sieve

### Example Problems

- Count Primes

### Common Mistakes

- Marking from `2 * p` instead of `p * p`; smaller multiples were already marked by smaller primes.
- Iterating `p` past `sqrt(n)`; once `p * p > n`, no new composites can be marked.
- Sizing the sieve as `n` instead of `n + 1` when the problem asks "primes less than n"; off-by-one matters.

### Pseudocode Or Template

```text
is_prime = [True] * n
for p in range(2, sqrt(n)):
    if is_prime[p]: mark multiples
```

### Complexity Notes

O(n log log n) time, O(n) space.

### Interview Explanation

Each composite is eliminated by its smallest prime factor.

## Pattern: Matrix Traversal

### Beginner Intuition

Control row and column bounds or direction vectors explicitly.

### When To Use It

Use for spiral order, rotation, and diagonal traversal.

### When Not To Use It

Do not mutate dimensions without checking crossing bounds.

### Recognition Signals

- matrix
- spiral
- rotate
- coordinates

### Example Problems

- Spiral Matrix
- Rotate Image

### Common Mistakes

- For spiral, processing the inner row twice when `top == bottom` after the top-row pass; gate the bottom-row and left-column passes.
- For rotation, transposing in place but reversing the wrong axis; clockwise rotation reverses each row, counter-clockwise reverses each column.
- Mixing up `(r, c)` and `(c, r)` mid-function; settle on a convention and document it.

### Pseudocode Or Template

```text
top, bottom, left, right = bounds
while top <= bottom and left <= right:
    traverse edges and shrink
```

### Complexity Notes

O(mn) time.

### Interview Explanation

The boundaries define which ring remains unprocessed.

## Pattern: Coordinate Geometry

### Beginner Intuition

Normalize slopes, distances, and orientation tests.

### When To Use It

Use for lines, hulls, and nearest or collinear points.

### When Not To Use It

Do not compare floating point slopes for exact equality.

### Recognition Signals

- slope
- line
- distance
- orientation

### Example Problems

- Max Points on a Line
- Erect the Fence

### Common Mistakes

- Storing slopes as floats and comparing with `==`; use reduced integer pairs `(dy / g, dx / g)` with sign normalization.
- Not handling duplicate points; they share every line and must be counted once per anchor.
- Treating vertical lines (`dx == 0`) as a divide-by-zero case; the reduced form `(1, 0)` handles them cleanly.

### Pseudocode Or Template

```text
dy = y2 - y1; dx = x2 - x1
g = gcd(abs(dy), abs(dx))
key = normalized(dy // g, dx // g)
```

### Complexity Notes

Often O(n^2) for pairwise line counting.

### Interview Explanation

A normalized integer slope is a stable key for collinearity.

## Pattern: Randomized Prefix

### Beginner Intuition

Use prefix sums to map a random integer to a weighted bucket.

### When To Use It

Use for weighted random pick and reservoir sampling variants.

### When Not To Use It

Do not use modulo bias when uniform weighted choice is required.

### Recognition Signals

- random
- weights
- prefix
- reservoir

### Example Problems

- Random Pick with Weight
- Random Pick Index

### Common Mistakes

- Picking `random.randint(0, total - 1)` and looking up via `bisect_right` instead of `bisect_left`; the convention determines which weight bucket the value falls into.
- Computing the prefix on every call; build it once in the constructor.
- Using `random() * total` and rounding; floating-point bias and rounding errors break uniformity.

### Pseudocode Or Template

```text
prefix weights
r = random integer in [1, total]
return lower_bound(prefix, r)
```

### Complexity Notes

O(log n) pick after O(n) preprocessing.

### Interview Explanation

Prefix sums turn weights into contiguous integer ranges.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
