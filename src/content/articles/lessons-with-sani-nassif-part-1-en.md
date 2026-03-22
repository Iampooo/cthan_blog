---
type: "note"          
title: "Lessons with Sani Nassif, Part 1"    
date: 2026-03-12
lang: "en"
tags: ["engineering", "lesson", "modeling"]
draft: false
---

Dr. Sani R. Nassif is the founder and CEO of Radyalis, an IEEE Life Fellow, former president of IEEE CEDA, General Chair of ICCAD 2008, and an IBM Master Inventor with over 75 patents. He has received numerous Best Paper Awards at top conferences including DAC, ICCAD, CICC, and ISQED.

Our university invited him to teach a six-week course. Sani is a pure "engineer" and researcher — funny in his delivery, but full of wisdom. I want to record what I've learned.

<div class="styled-quote">
<div class="styled-quote-mark">"</div>
<div class="styled-quote-text">

The most important thing to ask in an interview: How will I be evaluated?

</div>
<div class="styled-quote-source">－ Sani R. Nassif</div>
</div>



## How Engineers Solve Problems: The MASO Framework

Sani believes schools never teach us how to actually solve problems. Engineers, he says, have an important problem-solving framework — **MASO**:
- **M**odeling
- **A**nalysis
- **S**imulation
- **O**ptimization

He illustrated this with a vivid example: how to optimize his commute.

Suppose he needs to walk 468 meters from campus to the metro station. There are two things to optimize: he can walk fast, burning more energy but saving time; or walk slowly, saving energy but spending more time. Turning this into something we can analyze and simulate — that's modeling.

What do we simulate? Time and energy. Time can be split into walking time and waiting time. Using basic intuition and probability: walking time is $\frac{468}{v}$; assuming the train comes every 600s, the expected waiting time is 300s, so $T_{total}=\frac{468}{v}+300$.

But how do you model energy? Neither I nor Sani knew off the top of our heads how much energy a walk consumes — but someone does. A quick search turns up existing research with a formula: $P_{walk}=\frac{mg}{\pi}\sqrt{ \frac{3gL}{2} }\left( 1-\sqrt{ \frac{\pi^2v^2}{6gL} } \right)$. Just use it. **When engineers encounter something they don't know, they don't invent new formulas — they're good at searching for and applying what's already known.**

With these two formulas, we can combine them linearly and plot them for analysis. Sani calls this the goodness metric — how you design it depends on your objective. If you care more about time, increase its weight; otherwise, decrease it.

<picture>
  <source srcset="/figures/sani-fig1-goodness-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="/figures/sani-fig1-goodness-light.svg" alt="Goodness Metric">
</picture>


The next step is Simulation. We don't actually know if the goodness metric we just computed is accurate — only after simulating can we tell whether the error is acceptable. But during simulation, we can expect plenty of uncertainty: will I stop to tie my shoes? Will my walking speed fluctuate? Will the metro be delayed? When there's this much uncertainty, we have an incredibly useful mathematical tool — the [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem). The sum of independent random variables tends toward a normal distribution. This is a powerful tool and intuition.

So we take our analysis, add normal distributions, and get closer to reality. This is the famous [Monte Carlo Method](https://en.wikipedia.org/wiki/Monte_Carlo_method).^[Named because the discoverer Ulam's uncle used to lose money at the Monte Carlo casino.]

<picture>
  <source srcset="/figures/sani-fig2-montecarlo-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="/figures/sani-fig2-montecarlo-light.svg" alt="Monte Carlo">
</picture>


Finally, optimization. There are many approaches — one is the [Karush-Kuhn-Tucker Conditions](https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions), essentially setting the derivative to zero to find the optimum.

That's roughly the MASO process Sani described. Pick a problem, run it through MASO, and along the way you'll use some calculus, algebra, statistics, numerical analysis, and other tools. Whatever knowledge you're missing, find a way to get it (the internet and AI are good leverage). In the end, you arrive at an answer that feels roughly right. It's not that hard, is it?

Of course, real-world problems aren't this simple. Sani then went into detail about Modeling and the challenges it brings.

## Modeling

The ultimate goal of modeling is always simulation — the level of complexity depends on your simulator's capabilities.

Take a resistor as an example. When we see a resistor, we naturally think of $V=IR$, voltage dividers — things we learned in high school. But we've already made many assumptions in our heads, and they're not necessarily correct.

We assume the resistor obeys Ohm's law, so $V=IR$. The voltage divider formula assumes current conservation and voltage conservation (KVL and KCL for those who've taken circuit theory). We assume wire resistance is zero… This reminds me that **our thinking often stays at the first level — dig deeper and things aren't as obvious as they seem.**

> We often forget how complicated things are

Especially in EE, we can — and sometimes must — drill down to extreme detail. Where does resistance come from? We can explain it simply with Ohm's law, or go one level deeper: the [Drude Model](https://en.wikipedia.org/wiki/Drude_model) tells us resistance depends on electron drift velocity, which in turn depends on the mean free path (how long, on average, before an electron collides with something). We can go even deeper — quantum mechanics says electrons exhibit wave-particle duality, behaving more like waves with interference and diffraction…

Sani calls this the abstraction layer. We can always ask for more detail, but we must decide where to stop — too much complexity makes simulation impossible.

Moving into actual modeling: essentially, we have a plot with many data points, and we want to draw a line through them. The simplest example is Linear Regression. We use $y=a_{1}x+a_{0}$ to fit a line, minimizing the distance from each point to the line. A counterintuitive point: "linear" actually refers to being linear in the *coefficients*, so $y=a_{2}x^2+a_{1}x+a_{0}$ is also linear regression. You can even transform $x$ in all sorts of ways — log, sin — and plug it in. The same goes for $y$. These all fall under linear regression.

Implementation is straightforward with Python libraries, and AI can do it easily nowadays.

<picture>
  <source srcset="/figures/sani-fig4-linreg-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="/figures/sani-fig4-linreg-light.svg" alt="Linear Regression">
</picture>

Sani specifically warned: plots can be deceiving — pay attention to the scale, and more importantly, look at the residuals. They're more useful than the regression line itself. If the residuals show a pattern — high at both ends, low in the middle — you might suspect you're missing an $x^2$ term.

<picture>
  <source srcset="/figures/sani-fig5-residual-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="/figures/sani-fig5-residual-light.svg" alt="Residual">
</picture>

I won't go into more detail here — those interested can study [Linear Regression](https://en.wikipedia.org/wiki/Linear_regression) and [Numerical Analysis](https://en.wikipedia.org/wiki/Numerical_analysis). Here are a few more key points Sani mentioned:
- In the workplace you need rear protection^[lol] — like a safety margin. Give yourself room for error; don't always give overly certain answers.
- Engineers need to know just enough math to do their work, not invent new math.
- You will get data. They are, by nature, shitty.

There's a small story worth mentioning. Sani talked about how he did modeling for the legendary [Hermann K. Gummel](https://en.wikipedia.org/wiki/Hermann_Gummel) at Bell Labs. They were modeling [ring oscillators](https://en.wikipedia.org/wiki/Ring_oscillator)^[Sani says the semiconductor world can be divided into two ends: one is foundries like TSMC, the other is design houses like Apple and Nvidia. In between sits the ring oscillator — the bridge that communicates the most critical timing performance between both sides.]. Sani was quite pleased with his results — a nice-looking regression line with some error, but seemingly not too bad.

<picture>
  <source srcset="/figures/sani-fig3-regression-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="/figures/sani-fig3-regression-light.svg" alt="Regression">
</picture>


Hermann looked at it and politely asked: Good, but **what does your model predict for distance=0 and distance=∞?**

Look carefully and you'll notice the regression line doesn't pass through the origin (0,0) — which is obviously wrong. The extreme case of infinity can't be modeled by a simple linear equation either. This experience teaches us: before starting any simulation, consider the physical properties and extreme values first — nail down the things that **must** be correct before refining the rest.

> Start from the asymptotes and then refine the model

## Office Hour

In the following weeks I'll add some questions I asked Sani after class. I try to ask questions every session.
