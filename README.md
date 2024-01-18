# Probability-Problems
## Problem 1
**Problem**: Consider the following recurrence relation in two variables:
$$f(a, b) = \frac{a}{a+b} f(a-1,b)+ \frac{b}{a+b}f(a+1,b-1) $$
for positive integers $a$ and $b$,
with the boundary conditions $f(0,b)=0$ for integers $b>0$ and $f(a,0)=1$ for integers $a\ge0$.
Is it true that $f(1,n)$ converges to $1$ as $n$ tends to infinity?

**Idea**: The recurrence can be reformulates as a probability question which we simulate in Problem1.py. 
Consider the following process - start with m white balls and n black balls in an urn. Draw a ball uniformly at random. If it is white, throw it away; if it is black, colour it white and put it back into the urn. Repeat this process.

Stop the process when all the remaining balls in the urn become the same colour. Let’s write $P(m, n)$ for the probability that, starting with $m$ white balls and $n$ black balls, all the balls are white when the process is stopped. Then the question becomes Is it true that $P(1, n)$ converges to $1$ as $n \to \infty$?


