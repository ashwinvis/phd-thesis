# Norman's Pandoc Filter Collection

## History

This origins of this project are the old *moreblocks* filters, written by the author in 2015 in Haskel.
In 2015 the autor tries to write some lecture presenations for math using markdown and pandoc to create PDF-Presentations via beamer and LaTeX.

As he wanted some better and different colors for his definitions, theorems, exercises etc. without touching the
tex-code he started using pandoc-filters and Haskel.

This worked fine until pandoc changed the API in 0.17.0.3, so the ever more growing changes in moreblocks.hs collapsed and a the author thought it would be a nice idear to start rather fresh with Python3 and panflute instead of Haskel.

So NPFC is a completly new version of the old **morblocks**-filter (witch was written in Haskel) with much more filters to come.

## What do you need?

As this is now written in Python, you need **Python3** and **panflute**

You can find **Python** here: (Phyton)[http://pyton.org]
And you can find **panfulte** here: (panflute github)[https://github.com/sergiocorreia/panflute]

I recommend **Python3.5** or newer and the actual **panflute**!


## First steps

After you have installed **Pyhton3.5** (or newer) and **panflute** via

```bash
pip install git+git://github.com/sergiocorreia/panflute.git
```

or 

```bash
pip3 install git+git://github.com/sergiocorreia/panflute.git
```

you might start with **NPFC**.


### Why Python3 and not Python2?

Really? - Did you asked that?

I guess you want to know, what to do if you have Python2 already installed? - Well, install Python3 also and use both, as long, as you can change compledly to **Python3**.

If you have both **Python2** and **Python3** please check the first lines of the .py-files

As on my development system, the first list always looks like

```bash
#!/usr/bin/env python3
```

because I have to use both Releases of **Python**.

If you just use **Python3** you can change them to:

```bash
#!/usr/bin/env python
```

## Why this filter?

When you write a lecture (esp. a math lecture) in Markdown and use pandoc to create a 
LaTeX or LaTeX-beamer output, you might want not only blocks, but have control over the 
type of blocks pandoc adds.

## What does it do for you?

Take a look at the following input:

```markdown
#### from Vieta {.theorem}

For a polynom $x^2+px+q$ with zeros $x_1$ and $x_2$, the formulars 
$p = -(x_1+x_2)$ and $q=x_1 \cdot x_2$ always holds.
```

Normally this would lead to the following output:

```latex
\begin{block}{from Vieta}
For a polynom $x^2+px+q$ with zeros $x_1$ and $x_2$, the formulars 
$p = -(x_1+x_2)$ and $q=x_1 \cdot x_2$ always holds.
\end{block}
```

Using the pandoc-moreblock-filter, we map the option {.theorem} to the *amslatex*-package enviroment 

```latex
\begin{theorem}...\end{theorem}
``` 

instead. so we get the output:

```latex
\begin{theorem}[from Vieta]
For a polynom $x^2+px+q$ with zeros $x_1$ and $x_2$, the formulars 
$p = -(x_1+x_2)$ and $q=x_1 \cdot x_2$ always holds.
\end{theorem}
```

as an output. 

With the **{.endblock}** option it is even possible to end a block at will.
So the input 

```markdown
#### from Vieta {.theorem}

For a polynom $x^2+px+q$ with zeros $x_1$ and $x_2$, the formulars 
$p = -(x_1+x_2)$ and $q=x_1 \cdot x_2$ always holds.

#### {.endblock}

We can use this theorem to guess a root of 
a polynom where p and q are integers. 

####  {.lemma}

A root must allways be a divisor of $q$!
```

will lead to the output

```latex
\begin{theorem}[from Vieta]
For a polynom $x^2+px+q$ with zeros $x_1$ and $x_2$, the formulars 
$p = -(x_1+x_2)$ and $q=x_1 \cdot x_2$ always holds.
\end{theorem}

We can use this theorem to guess a root of 
a polynom where p and q are integers. 

\begin{lemma}
A root must allways be a divisor of $q$!
\end{lemma}
```
	
## How to use it with pandoc

Using this filter is easy, if you **Python3** and **panflute** installed.

To test the filter you might use

```bash
pandoc --from=markdown --to=json **test.md** | \ 
./moreblocks.py beamer | \
pandoc --from=json --to=beamer -o **test.pdf**
```
or

```bash
pandoc --from=markdown --to=beamer --filter moreblocks.py \
**test.md** -o **test.pdf**
```

instead.

## How does it work?

Simple! - The filter seaches for a "{.theorem}", "{.example}", "{.examples}", "{.fact}", 
... ,or "{.endblock}" option in the Markdown block "####", just like in the example above.
This is replaced by a RawLatexBlock or RawLatexInline in the *JSON* represenation of the **AST** by

```latex
\begin{Satz}...\end{Satz}

\begin{Beispiel}...\end{Beispiel}

\begin{Beispiele}...\end{Beispiele}

etc.

```

You might change the options name in "moreblocks.py". This all interacts with the 
"moreblocks.tex" file in wich all new blocks are defined and the color is set.
You may also change the LateX theorem enviroment used by YAML within the markdown-file:

```markdown
---
author: Norman Markgraf
title: Pandoc some block examples
lang: en
theme: Boadilla
papersize: A4
fontsize: 10pt
header-includes: \input{moreblocks.tex}
moreblocks:
    theorem: theorem
---
```

## Okay, I do need more help!

Feel free to ask me. Send a message to nmarkgraf (at) hotmail (dot) com with the 
subject "pandoc-moreblocks-filter", and I tried to help you asap!


## By the way

The **README.rst** is the ReStructedText version of the **README.md**. Automaticaly generated via **pandoc**, so please do the editing in the **README.md** rather than in the **README.rst**! -- *Thanks*!

You can get a RST version (**README.rst**) of this **README.md** via
```bash
make README.rst
```

and a PDF version (**README.pdf**) of this **README.md** via

```bash
make README.pdf
```

as log as you have a running *make* on your system. 
## Releases

- Release 1.0.0 nm (09.12.2016) 
	New name, new programming language, new code base! And yes, I knew the documentation needs a lot of updates!
		
