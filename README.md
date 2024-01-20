# Probability-Problems
Some interesting probability problems, some which are possible to solve by hand and some which are harder or near impossible. I will solve them (or at least get estimates) via simulations.

The first 5 problems are simulated and the simulations are provided in the respective Python script. In the last section I have an added bonus part, which is purely mathematical without any simulations. The purpose of this is to showcase a beautiful connection between analysis and the distribution of prime numbers, derived from elementary probability theory, which I think anyone interested in probability should see. We derive the Euler product formula for the Riemann zeta function, which connects the Riemann hypothesis, a conjecture that many mathematicians consider the most important unsolved problem in pure mathematics, to the distribution of the primes.
## Problem 1: An elementary but fiendishly difficult probability problem
**Problem**: Consider the following recurrence relation in two variables:
$$f(a, b) = \frac{a}{a+b} f(a-1,b)+ \frac{b}{a+b}f(a+1,b-1) $$
for positive integers $a$ and $b$,
with the boundary conditions $f(0,b)=0$ for integers $b>0$ and $f(a,0)=1$ for integers $a\ge0$.
Is it true that $f(1,n)$ converges to $1$ as $n$ tends to infinity?

**Idea**: The recurrence can be reformulates as a probability question which we simulate in Problem1.py. 
Consider the following process - start with $m$ white balls and $n$ black balls in an urn. Draw a ball uniformly at random. If it is white, throw it away; if it is black, colour it white and put it back into the urn. Repeat this process.

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

## Problem 4: Random Walks and Pólya's Theorem
**Problem**:In mathematics, a random walk, sometimes known as a drunkard's walk, is a random process that describes a path that consists of a succession of random steps on some mathematical space. Let $p(d)$ be the probability that a random walk on a $d$-dimensional lattice returns to the origin, then an interesting question is what values $p(1)$, $p(2)$ and $p(3)$ take. Indeed, Pólya's theorem states that $p(1) = p(2) = 1$, but $p(d)<1$ for $d>2$. In particular it has been shown that
$$p(3) = 1 - \frac{1}{u(3)} \approx 0.340537...,$$ where $u(3)$ is given by the third of the Watson's Triple Integrals which has the exact solution, $$u(3)=\frac{\sqrt{6}}{32\pi^3} \Gamma{\left(\frac{1}{24}\right)} \Gamma{\left(\frac{5}{24}\right)} \Gamma{\left(\frac{7}{24}\right)} \Gamma{\left(\frac{11}{24}\right)}.$$ A very peculiar result, to say the least. Let's simulate it!

**Idea**: Straightforward simulation, see code.

**Source**: [Wolfram MathWorld](https://mathworld.wolfram.com/PolyasRandomWalkConstants.html)

## Problem 5: Infamous Putnam Problem
**Problem**: In the 1992 Putnam competition the following problem can be found: Four points are chosen independently and at random on the surface of a sphere (using the uniform distribution). What is the probability that the center of the sphere lies inside the resulting tetrahedron?

The Putnam competition is widely considered to be the most prestigious university-level mathematics competition in the world, and its difficulty is such that the median score is often zero (out of 120) despite being attempted by students specializing in mathematics. It is needless to say that this is a hard problem to solve by hand.

**Idea**: First we need to generate four random points uniformly on a sphere. Deceivingly, it is incorrect to select spherical coordinates $\theta$ and $\phi$ from uniform distributions $\theta \in[0,2 \pi)$ and $\phi \in[0, \pi]$, since the area element $d \Omega=\sin \phi\ d\theta d\phi$ is a function of $\phi$, and hence points picked in this way will be "bunched" near the poles. Instead one should generate three random numbers $x,\ y,\ z$ using a Gaussian distribution and ultiply each number by $r/\sqrt{x^2+y^2+z^2}$ (a.k.a. Normalise). Once we have generated four points via this method we must determine if the center of the sphere lies inside the tetrahedron with the four points as vertexes. We do this utilizing simple linear algebra: for each plane of the tetrahedron, check if the point is on the same side as the remaining vertex. If it is for all the planes, then the point (the center of the sphere) lies inside the tetrahedron. Simulate this numerous times and estimate the probability

**Source**: [Putnam 1992](https://kskedlaya.org/putnam-archive/1992.pdf), [Wolfram MathWorld](https://mathworld.wolfram.com/SpherePointPicking.html)


## Bonus: A Beautiful Connection
The Riemann zeta function or Euler-Riemann zeta function, denoted by the Greek letter $\zeta$ (zeta), is a mathematical function of a complex variable defined as
$$\zeta(s)=\sum_{n=1}^{\infty} \frac{1}{n^s}=\frac{1}{1^s}+\frac{1}{2^s}+\frac{1}{3^s}+\cdots$$
for $\text{Re}(s)>1$, and its analytic continuation elsewhere. Let $X$ be a discrete random variable with the probability mass density functions $$p_X(n) = \text{P}(X=n) =\frac{1}{n^s}\frac{1}{\zeta(s)},\ n\geq 1,\ n \in \mathbb{Z}$$

### a) Prove that $p_X(n)$ is indeed a probability mass density function.
It is evident that $p_X(n)$ is non negative. It is left to show that the probabilities sum up to 1. $$\sum_{n=1}^\infty \text{P}(X=n) = \sum_{n=1}^\infty \frac{1}{n^s}\frac{1}{\zeta(s)} = \frac{1}{\zeta(s)} \sum_{n=1}^\infty \frac{1}{n^s} = \frac{1}{\zeta(s)} \zeta(s) = 1,$$ and we are done.

### b) Let $k \geq 2$ be an integer. What is the probability that $X$ is divisible by $k$?
For $X$ to be divisible by $k$ it needs to be a multiple of $k$, meaning $$\text{P}(X \equiv 0\ \text{mod}\ k) = \text{P}(X = k) + \text{P}(X = 2k) + \text{P}(X = 3k) \cdots$$ In other words we want to find the sum $$\sum_{n=1}^\infty \text{P}(X = nk) = \sum_{n=1}^\infty \frac{1}{(nk)^s}\frac{1}{\zeta(s)} = \frac{1}{k^s}\sum_{n=1}^\infty \frac{1}{n^s}\frac{1}{\zeta(s)} = \frac{1}{k^s}.$$ Thus we have found that the probability of $X$ being divisible by $k$ is $\frac{1}{k^s}$.

### c) What is the probability that $X$ is not divisible by any prime numbers.
Let $D_k$ be the event that $X$ is divisible by $k$, then we are seeking after $$\text{P}\left( \bigcap_{\text{prime}\ p} D_p'\right).$$ Since $D_i$ and $D_j$, where $i$ and $j$ are primes, are independent (being divisible by the prime $i$ does not impact being divisible by the prime $j$), it is a simple excersice to show that the complements are also independent. Using this we have $$\text{P}\left( \bigcap_{\text{prime}\ p} D_p'\right) =\prod_{\text{prime}\ p} \text{P}(D_p') = \prod_{\text{prime}\ p} 1-\text{P}(D_p) = \prod_{\text{prime}\ p} 1-\frac{1}{p^s},$$ where we also used the results from the b) problem.

On the other hand note that the only integer $X = n,\ n\geq 1$, which is not divisible by any primes is $1$, so in fact we have $$\text{P}\left( \bigcap_{\text{prime}\ p} D_p'\right) = \text{P} (X = 1).$$ But we know that $$\text{P} (X = 1) = \frac{1}{1^s}\frac{1}{\zeta(s)} = \frac{1}{\zeta(s)}$$ which yields $$\prod_{\text{prime}\ p} 1-\frac{1}{p^s}=\frac{1}{\zeta(s)}$$ or, rewritten $$\zeta(s)=\sum_{n=1}^{\infty} \frac{1}{n^s} = \prod_{\text{prime}\ p} \frac{1}{1-p^{-s}}$$. A remarkable connection between the Riemann zeta function and the prime numbers, the famous Euler product formula for the Riemann zeta function!
