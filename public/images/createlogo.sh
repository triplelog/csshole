#!/bin/bash
for i in familyfarm croprotation populationfrenzy logo;
do
	convert ${i}.png -resize 310 ${i}1p.png
	convert ${i}.png -resize 620 ${i}2p.png
	convert ${i}.png -resize 1000 ${i}3p.png
	convert ${i}.png -resize 700 ${i}1t.png
	convert ${i}.png -resize 1500 ${i}2t.png
done
for i in sflogo;
do
	convert -flatten ${i}.png -resize 20 ${i}20.jpeg
	convert -flatten ${i}.png -resize 29 ${i}29.jpeg
	convert -flatten ${i}.png -resize 40 ${i}40.jpeg
	convert -flatten ${i}.png -resize 60 ${i}60.jpeg
	convert -flatten ${i}.png -resize 58 ${i}58.jpeg
	convert -flatten ${i}.png -resize 76 ${i}76.jpeg
	convert -flatten ${i}.png -resize 87 ${i}87.jpeg
	convert -flatten ${i}.png -resize 80 ${i}80.jpeg
	convert -flatten ${i}.png -resize 120 ${i}120.jpeg
	convert -flatten ${i}.png -resize 152 ${i}152.jpeg
	convert -flatten ${i}.png -resize 167 ${i}167.jpeg
	convert -flatten ${i}.png -resize 180 ${i}180.jpeg
	convert -flatten ${i}.png -resize 1024 ${i}1024.jpeg
done