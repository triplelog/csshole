---
title: "Sudoku Game with only CSS/HTML"
date: 2018-06-20
tags: []
draft: false
type: "howto"
layout: "basic"
---

Sudoku is a relatively simple game to program in just about any programming language. Create a grid with 9 rows and columns and let the user input any number from 1-9 into each cell. 

But there are features that a computer makes possible that paper and pencil cannot match. One feature is blocking a user from inputting a number into row, column, or 3x3 block that already has that number. Another feature is to highlight the row, column, and 3x3 block of each cell to avoid any confusion. And everyone likes to see a congratulatory message when the game is complete.

All of these features (and more) are easy enough if you are using javascript or any scripting language. However, CSS is meant to make it easy to store or manipulate variables. In particular, the C in CSS stands for cascading which means that data can really only be passed down to child and younger sibling elements. We are going to have to be both creative and use brute force to create a game that looks like a normal sudoku game.

There are many ways to create a sudoku game with just HTML and CSS, but I am going to describe the method that is probably easiest to understand. I encourage you to try to build your own better version of the game or another game. You will probably learn a thing or two along the way about how HTML and CSS work together to create a web page. 

First, we need a way to add numbers to the grid. I wanted to be able to play without any keyboard input, but it actually is possible to match the functionality of this game with text input in each cell. Challenge 1: Read the CSS documentation and figure out how keyboard input can be used without any javascript. 

We will add a row of buttons that allow the user to choose which number they want to input into the puzzle. Using a group of nine radio buttons we can easily make such a row. And the :checked selector allows us to highlight the selected number. 

If the 5 button has been checked then we can use #radio5:checked ~ #elementID {} to change the look of any sibling element. What does this CSS mean? #radio5 identifies the element with id="radio5" and :checked means that any element with this id that is checked will be found. Then ~ looks for any sibling after the 5 button so ~ #elementID looks for any younger sibling with id="elementID". So if we make our puzzle grid a younger sibling of our radio buttons then we can change them based on which button is currently checked.

Normal people would create grids and rows by nesting elements in divs or tables, but the cascading nature of CSS means we need a flat collection of elements in order to pass our data. Our next task is to create the puzzle grid. In order to make to register which cell was clicked we need to make the grid a collection of 81 checkboxes. But each cell can be one of 9 numbers so we actually need to create 729 checkboxes. 

With one checkbox for each number for each cell, we can easily create a simple game. Position the cells so that there are 9 grids stacked on top of each other, but set them all to display:none. Then when a radio button from the top row is clicked, the grid associated with that number is changed to display: inline-block. Then clicking on a cell within the grid clicks a checkbox that can store the information for that cell.

Now we have a game that matches a pen and paper version. 