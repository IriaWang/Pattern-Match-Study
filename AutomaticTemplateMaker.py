from PIL import Image

count = 1
img = Image.open("G_bottom_74x110.png")
interval = 4
w, l = img.size

while l - interval*count > 0:
    to_crop = count*2
    img.crop((0, to_crop, w, l-to_crop)
             ).save("./G_bottom_74x" + str(l-interval*count) + ".png")
    count += 1

print("done")
