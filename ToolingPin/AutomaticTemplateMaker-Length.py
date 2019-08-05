from PIL import Image

count = 1
img = Image.open("./Templates/WithPaper-Right-Length/3834x2536.png")
interval = 100
w, l = img.size

while l - interval*count > 0:
    to_crop = count*interval/2
    img.crop((0, to_crop, w, l-to_crop)
             ).save("./Templates/WithPaper-Right-Length/3834x" + str(l-interval*count) + ".png")
    count += 1

print("done")
