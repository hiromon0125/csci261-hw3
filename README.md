# csci261-hw3
2025/10/28
Recursive multiplication problem

---
## Problem 2 Recursive Multiplication
---
1. function recursive_multiply(x, y)
2. x = 2^fl(n/2) * xh + xl
3. y = 2^fl(n/2) * yh + yl
4. cx = xh + xl
5. cy = yh + yl
6. zh = recursive_multiply(xh, yh)
7. zc = recursive_multiply(cx, cy)
8. zl = recursive_multiply(xl, yl)
9. return 2^(2fl(n/2)) * zh + 2^(fl(n/2)) * (zc − zh − zl) + zl
---

• Note that we can obtain xh, xl, yh, and yl with AND and MOD
• These are O(n), as is the addition we will need to use (i.e. we have a constant number of O(n)
operations, and thus have O(n) runtime overall at the level of each function call)
• Since we split the input in half and now have only three recursive calls, our recurrence becomes
T (n) = 3T (n/2) + O(n)
• And this has O(nlog2(3)) ≈ O(n1.59), which strictly improves upon the "grade-school" multiplication


---
## Problem 3
---

Add instruction count on mult calculation from problem 2 and new mult_pub.py.