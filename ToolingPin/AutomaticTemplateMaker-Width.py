from PIL import Image

count = 1
img = Image.open("./Templates/WithPaper-Right-Width/3834x1336.png")
interval = 100
w, l = img.size

while w - interval*count > 0:
    to_crop = count*interval/2
    img.crop((to_crop, 0, w-to_crop, l)
             ).save("./Templates/WithPaper-Right-Width/" + str(w-interval*count) + "x1336" + ".png")
    count += 1

print("done")
