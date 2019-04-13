from PIL import Image

my_image = Image.open("shaq.jpg") #this code opens the image
image_pixels = my_image.load()
width, height = my_image.size
for i in range(0, width):
    for j in range(0, height):
        current_pixel = image_pixels[i,j]
        blue_component = image_pixels[i,j][0]
        red_component = image_pixels[i,j][2]
        green_component = image_pixels[i,j][1]
        gray_value = (int)(0.07 * blue_component + 0.72 * green_component + 0.21 * red_component)

        if(gray_value < 50):
            new_color = (0, 31, 59, 255)
        elif (gray_value < 100):
            new_color = (215, 30, 1, 255)
        elif (gray_value < 150):
            new_color = (230, 191, 255, 255)
        elif (gray_value < 200):
            new_color = (255, 196, 86, 255)
        elif (gray_value < 250):
            new_color = (255, 246, 0, 255)

        image_pixels[i,j] = new_color
my_image.show()
