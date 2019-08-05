# This program automatically crops templates in length.
# It starts with the biggest template, and saves a series of images that
# are shorter than the given template by a given interval.
# Iria Wang, 07.23.2019

from PIL import Image

count = 1
img = Image.open("G_bottom_74x110.png")  # The largest template you wish to use
interval = 4  # The interval by which the images will be cropped
w, l = img.size  # Length and width of the largest template

# Crops smaller and smaller images until there is no more image to crop
while l - interval*count > 0:
    to_crop = count*interval/2  # How many pixels to crop from the top and bottom
    img.crop((0, to_crop, w, l-to_crop)  # (right, bottom, left, top)
             ).save("./G_bottom_74x" + str(l-interval*count) + ".png")
    # Save based on naming system of largest template
    count += 1

print("done :)")
