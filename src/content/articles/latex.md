---
type: "memo"
title: "Latex 語法測試"
date: 2026-03-09
lang: "zh"
tags: ["reading"]
description: "hihihi"
draft: True
---

# Latex

## LaTeX for Obsidian 
- ref: https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference
### Display
- inline mode: $\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$
- display mode: 

$$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$$

### Greek letters
$$A\ B\ \Gamma\ \Delta\ E\ Z\ H\ \Theta\ I\ K\ \Lambda\ M\ N\ \Xi\ O\ \Pi\ P\ \Sigma\ T\ Y\ \Phi\ X\ \Psi\ \Omega\ $$
$$\alpha\ \beta\ \gamma\ \delta\ \epsilon\ \zeta\ \eta\ \theta\ \iota\ \kappa\ \lambda\ \mu\ \nu\ \xi\ \omicron\ \pi\ \rho\ \sigma\ \tau\ \upsilon\ \phi\ \chi\ \psi\ \omega\ $$
$$\epsilon\ \varepsilon \quad \phi\ \varphi\ $$
### Superscripts & Subscripts
$$x_i^2 \quad \log_2x$$
### Groups
$$x_i^2 \quad x_{i^2} \quad {x_i}^2$$
### Parentheses
$$ \left(\frac{\sqrt x}{y^3}\right)$$
$$(\ [\ \{\ |\ \vert\ \Vert\ \langle\ \rangle\ \lceil\ \rceil\ \lfloor\ \rfloor\ $$
$$\left.x^2\right\rvert_3^5 = 5^2-3^2$$
### Sums and integrals
$$\sum_{i=0}^\infty i^2$$
$$\prod\ \int\ \bigcup\ \bigcap\ \iint\ \iiint\ \idotsint\
$$
### Fractions
$$\frac ab$$
$$\frac{a+1}{b+1}$$
$${a+1\over b+1}$$
### Fonts
$$\Bbb {abcdefghijklmnopqrstuvwxyz}$$
$$\mathbf {abcdefghijklmnopqrstuvwxyz}$$
$$\mathit {abcdefghijklmnopqrstuvwxyz}$$
$$\pmb {abcdefghijklmnopqrstuvwxyz}$$
$$\mathtt {abcdefghijklmnopqrstuvwxyz}$$
$$\mathrm {abcdefghijklmnopqrstuvwxyz}$$
$$\mathsf {abcdefghijklmnopqrstuvwxyz}$$
$$\mathcal {ABCDEFGHIJKLMNOPQRSTUVWXYZ}$$
$$\mathscr {abcdefghijklmnopqrstuvwxyz}$$
$$\mathfrak {abcdefghijklmnopqrstuvwxyz}$$
### Radical signs/roots
$$\sqrt{x^3}$$
$$ sqrt[3] {\frac xy} $$
### Special functions
$$\lim_{x\to \infty} n \quad \sin x \quad \operatorname{iampoo}(x)$$
### Special symbols and notations
[Comprehensive LaTeX Symbol List](https://www.ctan.org/tex-archive/info/symbols/comprehensive/symbols-a4.pdf)

$$\lt\ \gt\ \le\ \ge\ \neq$$$$\times\ \div\ \pm\ \mp\ $$
$$\cup\ \cap\ \setminus\ \subset\ \subseteq\ \subsetneq\ \supset\ \in\ \notin\ \emptyset\ \varnothing\ $$
$${n+1 \choose 2k}\ \binom{n+1}{2k}$$
$$\to\ \gets\ \rightarrow\ \leftarrow\ \Rightarrow\ \Leftarrow\ \mapsto\ \implies\ \iff\ $$
$$\land\ \lor\ \lnot\ \forall\ \exists\ \top\ \bot\ \vdash\ \vDash\ $$
$$\star\ \ast\ \oplus\ \circ\ \bullet\ $$
$$\approx\ \sim\ \simeq\ \cong\ \equiv\ \prec\ \lhd\ $$
$$\infty\ \aleph_0\ \nabla\ \partial\ \Im\ \Re\ $$
$$a\equiv b\pmod n \quad a\bmod 17$$
$$\dots$$
$$\ell$$
$$\hat x\ \widehat {xy}\ \bar x\ \overline {xyz}\ \vec x\  \overrightarrow {xy}\ \overleftrightarrow{xy}\ \dot x\ \ddot x\ $$


## LaTeX for Overleaf
### Getting Started
```tex
\documentclass{article}
\begin{document}
First document. This is a simple example, with no 
extra parameters or packages included.
\end{document}
```
[Classes in LaTeX](https://www.ctan.org/topic/class)
### Preamble
- everything before `\begin{document}`
```tex
\documentclass[12pt, letterpaper]{article} %default 10px
\usepackage{graphicx} %enable external graph
```
### Including title, author and date information
```tex
\title{My first LaTeX document}
\author{Hubert Farnsworth\thanks{Funded by the Overleaf team.}}
\date{August 2022}
```
```tex
\maketitle
```
### Bold, italics and underlining
```tex
Some of the \textbf{greatest}
discoveries in \underline{science} 
were made by \textbf{\textit{accident}}.
```
### Adding images
```tex
\documentclass{article}
\usepackage{graphicx} %LaTeX package to import graphics
\graphicspath{{images/}} %configuring the graphicx package
 
\begin{document}
The universe is immense and it seems to be homogeneous, 
on a large scale, everywhere we look.

% The \includegraphcs command is 
% provided (implemented) by the 
% graphicx package
\includegraphics{universe}  
 
There's a picture of a galaxy above.
\end{document}
```
### Captions, labels and references
```tex
\documentclass{article}
\usepackage{graphicx}
\graphicspath{{images/}}
 
\begin{document}

\begin{figure}[h]
    \centering
    \includegraphics[width=0.75\textwidth]{mesh} %0.75 text width
    \caption{A nice plot.} 
    \label{fig:mesh1}
\end{figure}
 
As you can see in figure \ref{fig:mesh1}, the function grows near the origin. This example is on page \pageref{fig:mesh1}.

\end{document}
```
### Lists
- unordered lists
```tex
\begin{itemize}
  \item The individual entries are indicated with a black dot, a so-called bullet.
  \item The text in the entries may be of any length.
\end{itemize}
```
- ordered lists
```tex
\begin{enumerate}
  \item This is the first entry in our list.
  \item The list numbers increase with each entry we add.
\end{enumerate}
```
### Math
$$E=mc^2$$
$$T^{i_1 i_2 \dots i_p}_{j_1 j_2 \dots j_q} = T(x^{i_1},\dots,x^{i_p},e_{j_1},\dots,e_{j_q})$$
$$\int_0^1 \frac{dx}{e^x} =  \frac{e-1}{e}$$
$$\sqrt{x^2+1}$$
### Basic document structure
```tex
\begin{abstract}
Sample abstract
\end{abstract}

After our abstract we can begin the first paragraph, then press ``enter'' twice to start the second one.

This line will start a second paragraph.

I will start the third paragraph and then add \\ a manual line break which causes this text to start on a new line but remains part of the same paragraph. Alternatively, I can use the \verb|\newline|\newline command to start a new line, which is also part of the same paragraph.
```
### Chapters and sections
```tex
\chapter{First Chapter}

\section{Introduction}

This is the first section.

Lorem  ipsum  dolor  sit  amet,  consectetuer  adipiscing  
elit. Etiam  lobortisfacilisis sem.  Nullam nec mi et 
neque pharetra sollicitudin.  Praesent imperdietmi nec ante. 
Donec ullamcorper, felis non sodales...

\section{Second Section}

Lorem ipsum dolor sit amet, consectetuer adipiscing elit.  
Etiam lobortis facilisissem.  Nullam nec mi et neque pharetra 
sollicitudin.  Praesent imperdiet mi necante...

\subsection{First Subsection}
Praesent imperdietmi nec ante. Donec ullamcorper, felis non sodales...

\section*{Unnumbered Section}
Lorem ipsum dolor sit amet, consectetuer adipiscing elit.  
Etiam lobortis facilisissem...
```
-   `\part{part}`
-   `\chapter{chapter}`
-   `\section{section}`
-   `\subsection{subsection}`
-   `\subsubsection{subsubsection}`
-   `\paragraph{paragraph}`
-   `\subparagraph{subparagraph}`
### Creating tables
```tex
\begin{center}
\begin{tabular}{c c c}
 cell1 & cell2 & cell3 \\ 
 cell4 & cell5 & cell6 \\  
 cell7 & cell8 & cell9    
\end{tabular}
\end{center}
```
- with borders
```tex
\begin{center}
\begin{tabular}{|c|c|c|} 
 \hline
 cell1 & cell2 & cell3 \\ 
 cell4 & cell5 & cell6 \\ 
 cell7 & cell8 & cell9 \\ 
 \hline
\end{tabular}
\end{center}
```

```tex
\begin{center}
 \begin{tabular}{||c c c c||} 
 \hline
 Col1 & Col2 & Col2 & Col3 \\ [0.5ex] 
 \hline\hline
 1 & 6 & 87837 & 787 \\ 
 \hline
 2 & 7 & 78 & 5415 \\
 \hline
 3 & 545 & 778 & 7507 \\
 \hline
 4 & 545 & 18744 & 7560 \\
 \hline
 5 & 88 & 788 & 6344 \\ [1ex] 
 \hline
\end{tabular}
\end{center}
```
- with captions, labels and references
```tex
Table \ref{table:data} shows how to add a table caption and reference a table.
\begin{table}[h!]
\centering
\begin{tabular}{||c c c c||} 
 \hline
 Col1 & Col2 & Col2 & Col3 \\ [0.5ex] 
 \hline\hline
 1 & 6 & 87837 & 787 \\ 
 2 & 7 & 78 & 5415 \\
 3 & 545 & 778 & 7507 \\
 4 & 545 & 18744 & 7560 \\
 5 & 88 & 788 & 6344 \\ [1ex] 
 \hline
\end{tabular}
\caption{Table to test captions and labels.}
\label{table:data}
\end{table}
```
### Adding table of contents
```tex
\tableofcontents
```




- - -
### Reference