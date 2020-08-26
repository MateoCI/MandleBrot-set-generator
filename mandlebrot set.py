from colour import *

import graphics

colors = 10


pixelSpread = 2#since my code is unoptomized, setting this to 2 will make it faster but only fill in every other pixel

class imaginary():
	num = (0,0) #defines a tuple as the two parts of the imaginary number
	def add(self, other):
		return(self.num[0] + other.num[0], self.num[1] + other.num[1])#adds up the two differnt parts of each one

	def square(self):
		#gets all the regular numbers in order
		doubleI = ((self.num[1] * self.num[1]) * -1)
		regNum = self.num[0] * self.num[0]

		return(doubleI + regNum, self.num[1] * self.num[0] * 2)

def weIn(coords):
	imag = imaginary()
	poop = 0
	while(True):
		imag.num = imag.square()

		imag.num = imag.add(coords)



		poop = poop + 1

		if (poop >= colors):
			return 0
			break
		if (-2 > imag.num[0] or 2 < imag.num[0] or -2 > imag.num[1] or 2 < imag.num[1]):
			return poop
			break

constant = 2
xSize=int(2000/constant) #1000
ySize=int(1000/constant) #800


from graphics import *


win = GraphWin("Mandlebrot Set", xSize, ySize)


pixelSpread = 2
for x in range(0, xSize, pixelSpread):
	for y in range(0, ySize, pixelSpread):
		cmpl = imaginary()
		cmpl.num = ((x - (xSize / 2))/ xSize/0.25, (y - (ySize/2)) / ySize/0.5 )

		solve = weIn(cmpl)
		if (solve == 0):
			win.plot(x,y, 'black')
		else:
			poopoo = Color(hue=solve/colors, saturation=1, luminance=0.5)
			win.plot(x,y, poopoo.hex_l)







win.getMouse() # pause for click in windowwin.close()
win.close()











	
