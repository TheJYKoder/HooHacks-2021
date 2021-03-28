from PIL import Image, ImageDraw
import urllib.request
def createGif(gif1,gif2):
	urllib.request.urlretrieve(gif1,'first.gif')
	urllib.request.urlretrieve(gif2,'second.gif')
	firstgif = Image.open('first.gif')
	secondgif = Image.open('second.gif')
	#print(firstgif.n_frames)
	#print(secondgif.n_frames)
	totalframes = firstgif.n_frames+secondgif.n_frames
	for frame in range(0,firstgif.n_frames):
		firstgif.seek(frame)
		firstgif.save("frame"+str(frame)+".png")
	for frame in range(firstgif.n_frames,totalframes):
		secondgif.seek(frame-firstgif.n_frames)
		secondgif.save("frame"+str(frame)+".png")
	allframes = []
	for frame in range(0,totalframes):
		allframes.append("frame"+str(frame)+".png")
	print(allframes)
	imgify = lambda a : Image.open(a)
	allimages = list(map(imgify,allframes))
	print(len(allimages))
	allimages[0].save('out.gif',save_all=True, append_images= allimages[1:])

#gif = Image.open("")
#nextgif = Image.open("gif.gif")
createGif('https://raw.githubusercontent.com/garfix/movemegif/master/images/horse.gif','https://steamusercontent-a.akamaihd.net/ugc/82595628823614964/59CA60267C9EF097829F8B6CFDED0CD489F0ECCE/')