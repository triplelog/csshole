---
title: "Interactive Web Pages using only CSS and HTML"
description: "How and why to create web pages without Javascript or server-side code."
date: 2018-06-20
tags: []
draft: false
type: "howto"
layout: "basic"
---

<div style="margin-left: auto; margin-right: auto; width: calc(200px + 40vw); display: block; position: relative;">

<p>
Every web page on this domain is created using only HTML and CSS. No Javascript and no server interaction (other than navigating to a new static page). There is no good reason to make an interactive website completely static and avoid Javascript. Most of these web pages could be improved and made smaller by using just a few lines of Javascript because CSS is really not designed to do the things I use it for. If you are trying to learn HTML and CSS for the first time, you may not want to look at the source.
</p>

<p>
With those caveats out of the way, why might throwing out Javascript and server scripts be a good exercise? The best reason is that you want a fun challenge that combines creativity with brute force perseverance. If you are trying to reduce your dependence on Javascript/JQuery/Python/PHP/... then being restricted to CSS may teach you a trick or two that actually improves your web page.
</p>

<p>
What exactly can be done with CSS? It is important to know that CSS stands for cascading style sheets. The key word is cascading. Passing information from one element on the page to another is generally restricted to passing information from a parent to its child or from a sibling to a younger sibling. In order to use CSS for interactive elements, a rather flat structure is required.
</p>

<p>
Good HTML tutorials will suggest nesting elements because HTML and CSS do a good job of placing nested elements in the correct way. However, an element in one div cannot pass information to another div. Even elements with the same parent cannot pass information back and forth because a sibling can only talk to its younger siblings.
</p>

<p>
A flat structure means that much of the work of positioning elements needs to be done manually, so you need to know the difference between relative, absolute, and fixed positions. Elements will be on top of each other so knowing how to use z-index to change the stack ordering is imperative.
</p>

<p>
Creating an interactive web page with just HTML and CSS is like a magic trick. If you see how it is done, then you will probably be disappointed by its simplicity. There is a lot of deception by placing smoke and mirrors in just the right places. If you try to figure out how things are done on your own it will be much more satisfying. However, I am working on posts for the future that describe how the pages work. In the meantime, looking at the source may give you some clues. All the answers are in the source, but figuring out what each line does can be tricky.
</p>

<p>
I use Hugo to generate static sites. There is lots of repetition so I strongly suggest using something like Hugo if you are trying to create a complicated web page.
</p>

</div>
