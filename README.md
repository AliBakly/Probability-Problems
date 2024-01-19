# Probability-Problems
Some interesting probability problems, some which are possible to solve by hand and some which are harder or near impossible. I will solve them (or at least get estimates) via simulations.
## Problem 1: An elementary but fiendishly difficult probability problem
**Problem**: Consider the following recurrence relation in two variables:
$$f(a, b) = \frac{a}{a+b} f(a-1,b)+ \frac{b}{a+b}f(a+1,b-1) $$
for positive integers $a$ and $b$,
with the boundary conditions $f(0,b)=0$ for integers $b>0$ and $f(a,0)=1$ for integers $a\ge0$.
Is it true that $f(1,n)$ converges to $1$ as $n$ tends to infinity?

**Idea**: The recurrence can be reformulates as a probability question which we simulate in Problem1.py. 
Consider the following process - start with m white balls and n black balls in an urn. Draw a ball uniformly at random. If it is white, throw it away; if it is black, colour it white and put it back into the urn. Repeat this process.

Stop the process when all the remaining balls in the urn become the same colour. Let’s write $P(m, n)$ for the probability that, starting with $m$ white balls and $n$ black balls, all the balls are white when the process is stopped. Then the question becomes Is it true that $P(1, n)$ converges to $1$ as $n \to \infty$?

**Source**: [mathoverflow user](https://mathoverflow.net/questions/460095/how-to-show-a-function-converges-to-1)

## Problem 2: The birthday problem
**Problem**:In probability theory, the birthday problem asks for the probability that, in a set of $n$ randomly chosen people, at least two will share a birthday. The birthday paradox refers to the counterintuitive fact that only 23 people are needed for that probability to exceed 50%. We will implement a simulation to find the probability that in a set of $n$ randomly chosen people, at least $m$ will share a birthday.

**Idea**: Generate $n$ random values between 0-364 uniformly. Sort the values and note that duplicate values will always be adjacent. Now do a linear search comparing element at index $i$ with index $i - (m - 1)$. If there is an instance where the values compared are equal, then at least $m$ persons will share a birthday. Simulate this numerous times.

**Source**: [Wikipedia](https://en.wikipedia.org/wiki/Birthday_problem)

## Problem 3: Monte Carlo method for approximating $\pi$ using Buffon's needle problem
**Problem**:In probability theory, Buffon's needle problem is a question first posed in the 18th century by Georges-Louis Leclerc, Comte de Buffon:
Suppose we have a floor made of parallel strips of wood, each the same width, and we drop a needle onto the floor. What is the probability that the needle will lie across a line between two strips?

**Idea**: It can be shown analyticaly that the solution for the sought probability $p$, in the case where the needle length $l$ is not greater than the width $t$ of the strips, is $$p = \frac{2}{\pi} \cdot \frac{l}{t},$$ which means that we can estimate $\pi$ with
$$\pi \approx \frac{2}{\hat{p}} \cdot \frac{l}{t},$$ where $\hat{p}$ is the estimated probability from the simulation.

**Source**: [Wikipedia](https://en.wikipedia.org/wiki/Buffon%27s_needle_problem)

