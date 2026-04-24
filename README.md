# minimum_cost
# 🧠 Problem 1: Minimum Cost to Split Array into K Segments

## 📌 Problem Statement
Given an array `A` of `N` integers. The task is to split the array into exactly **K consecutive segments** such that:
- Each element belongs to exactly one segment
- The **total cost** of all segments is minimized
---

## 💰 Cost Definition
For a segment:
- For every **unique element**, find:
  - First occurrence index
  - Last occurrence index
- Cost of that element = `(last_index - first_index)`
- Segment cost = sum of all such values
---

## ⚡ Optimization
A naive solution leads to **O(N² × K)**, which is too slow.

To optimize:
### ✅ Use:
- **Sliding Window Technique**
  - Efficiently maintain cost of current segment
- **Divide & Conquer DP Optimization**
  - Reduces transition complexity
---

## 🧠 Key Idea
- Maintain a window `[L, R]`
- Track frequency of elements
- Update cost dynamically when expanding/shrinking window
---

## ⏱ Time Complexity
O(N log N x K)

---

## 🚀 Techniques Used
- Dynamic Programming  
- Divide & Conquer Optimization  
- Two Pointers / Sliding Window  
- Frequency Counting  
---

## ✨ Highlights
- Handles constraints up to **N = 35,000**
- Efficient cost computation using incremental updates
---
