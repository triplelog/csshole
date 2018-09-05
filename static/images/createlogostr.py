circleStr = "convert -size 100x100 xc:transparent"
for i in range(1,25):
	circleStr += ' -fill "rgb('+str(i*9+39)+','+str(i*3+20)+','+str(i*1+10)+')" -draw "circle 50,50 '+str(i*2)+',50"'
	
circleStr += ' circle_logo.png'

print(circleStr)