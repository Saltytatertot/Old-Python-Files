import image

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

def sepia(img,grayscale):
        p = grayscale_image.getPixel(col, row)
        red = p.getRed()
        blue = p.getBlue()
	if red < 63:
		red = int(red * 1.1)
		blue = int(blue * 0.9)
	elif red < 192:
		red = int(red * 1.15)
		blue = int(blue * 0.85)
	else:
		red = min(int(red * 1.08),255)
		blue = int(blue *0.93)
		
        newpixel = image.Pixel(avg, avg, avg)

        newimg.setPixel(col, row, newpixel)

        return sepia(img,grayscale)

def grayscale(img):
	for col in range(img.getWidth()):
		for row in range(img.getHeight()):
			p = img.getPixel(col, row)

			red = p.getRed()
			green = p.getGreen()
			blue = p.getBlue()
			avg = (red + green + blue)/3.0
			
			newpixel = image.Pixel(avg, avg, avg)
			newimg.setPixel(col, row, newpixel)

	return grayscale(img):
grayscale(img)            
sepia(img,grayscale)
newimg.draw(win)
win.exitonclick()
