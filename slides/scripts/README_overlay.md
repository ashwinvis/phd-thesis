---
title: Pandoc Beamer Filter
author: bwhelm
---

This filter simplifies the creation of beamer slides from markdown. In particular, it will:

1. Replace `<...>` with `\\onslide<...>` when it starts a line; optionally `<...>` can be prepended by either `*` or `+`. For example:

        - <1> text on first slide only
        - <1-2> text on first and second slides only
        - +<3> text on third slide only

    will produce the following (beamer) LaTeX:

        \begin{frame}

        \begin{itemize}
        \tightlist
        \item
        \onslide<1> text on first slide only
        \item
        \onslide<1-2> text on first and second slides only
        \item
        \onslide+<3> text on third slide only
        \end{itemize}

        \end{frame}

    In all other formats, the `<...>` will be removed, but everything else will remain.

2. Replace `[...]{slides="<spec>"}` with `\\onslide<spec>{...}`. Thus

        - Text on all slides. [Text only on second slide.]{slides="<2>"}

    will produce the following (beamer) LaTeX:

        \begin{frame}

        \begin{itemize}
        \tightlist
        \item
        Text on all slides. \onslide<2>{Text only on second slide.}
        \end{itemize}

        \end{frame}

    In all other formats, the `span` will be removed, but the content will remain.
