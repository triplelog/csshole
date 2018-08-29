---
title: "Interactive Maps with only CSS/HTML"
date: 2018-06-20
tags: []
draft: false
type: "howto"
layout: "basic"
---

Creating an interactive map with just HTML and CSS is something that should be possible. We just want to change the colors of certain parts of the map after they have been clicked. What makes certain maps hard?


<ol>
<li>CSS allows for two color choices: checked and not checked. We would like more color choices.</li>
<li>HTML likes rectangles and the U.S. does not consist of rectangular states.</li>
<li>We really would like to display counts and CSS does not like adding user-generated numbers.</li>
</ol>

The easiest problem to solve is adding more colors. We can stack as many radio buttons on top of each other as we want. Clicking on the blue version of South Carolina checks the scblue radio button and displays the light blue version of South Carolina. This process is repeated until clicking the red version of South Carolina displays the blue version and we are back to the beginning. Radio buttons are one of very few ways to pass data backwards in CSS. Thus we can easily rotate among as many colors as desired by adding another radio button associated with a certain color.

Creating a static map is straightforward, but requires downloading shapefiles and generating svg polygons. Generally any map you may want is available on the internet, but you will likely need to convert the coordinates from whatever format they came from. I have found using geojson files to be fairly painless. 

Each state or congressional district needs to be inside one distinct label in order to register which region was selected. Unfortunately, with the svg inside the labels it is actually the labels that are siblings of each other. And labels are rectangles so we need to only check a given label when the click was registered inside the polygon within the label. Fortunately, CSS allows the option to set pointer-events:none and let clicks pass through elements. Set every label to pointer-events:none and then set the polygons inside to pointer-events:all and the clicks are only registered in the correct polygon.

Creating a pretty map is nice, but the sizes of each state are not at all proportional to the number of electoral votes so it is hard to determine which party would win an election without an accurate count of electoral votes. While numbers are a very popular and easy way to display such information, we can also use colored bar of the correct width to display electoral votes. HTML and CSS is good at combining blocks.