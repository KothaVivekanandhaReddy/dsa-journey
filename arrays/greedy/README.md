# Greedy Pattern (Arrays)

## What is the Greedy Approach?
Greedy algorithms make a **locally optimal choice at each step** with the expectation that these choices lead to a **globally optimal solution**.

In array problems, this usually means:
- Making the best decision using **current information**
- Not revisiting past decisions
- No need to explore all possibilities (unlike DP)

---

## When to Use Greedy
Use greedy when:
- A local decision does not affect future feasibility
- The problem allows independent, step-by-step optimization
- You are asked to **maximize / minimize** something with clear rules

## Core Greedy Thought Process
At each step, ask:
1. What information from the past still helps me?
2. What information is now harmful?
3. Can I safely discard something forever?

## Core Greedy Ideas in Arrays
- Track the **best value so far** (min / max)
- Take advantage of **monotonic changes**
- Avoid unnecessary holding or waiting

---

## Greedy Intuitions (Very Important)

### 1. Drop Negative Contribution
If a running value becomes worse than starting fresh, discard it.
Used in:
- Maximum Subarray (Kadane)
---

### 2. Take All Positive Gains
If an action yields immediate profit without blocking future gains, take it.
Used in:
- Stock Buy & Sell II

---

### 3. Keep the Best So Far
Track the best candidate so far and update greedily.

Used in:
- Stock Buy & Sell I
- Interval scheduling

---

## Kadane’s Algorithm (Greedy Foundation)

### Core Insight
At index `i`:
- Either extend previous subarray
- Or start fresh from `nums[i]`

## Greedy vs DP (Important Distinction)

| Greedy | Dynamic Programming |
|------|-------------------|
| One-pass decisions | Decisions depend on subproblems |
| No state table | Uses dp states |
| Fast & simple | More general, but heavier |
| Works when local = global | Needed when local may fail |

Example:
- LC 121, 122 → Greedy
- LC 152 → DP (greedy intuition fails)

---

## When Greedy Fails (Important)
Greedy fails when:
- Future decisions depend on **multiple past choices**
- Local optimum blocks a better future outcome

Examples:
- Maximum Product Subarray (needs DP)
- Circular Subarray (needs math + greedy)

---


## Common Mistakes
- Forcing greedy when future decisions matter
- Confusing Kadane intuition with true DP
- Overcomplicating simple one-pass problems

---

## Takeaway
If a problem allows you to:
- Decide at the current index
- Never regret that decision later  

Then **Greedy is the right tool**.
