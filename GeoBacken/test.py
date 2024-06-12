from PIL import Image, ImageFilter

# Load the image
image_path = "test.png"
image = Image.open(image_path)

# Apply edge enhancement filter
sharpened_image = image.filter(ImageFilter.EDGE_ENHANCE)

# Save the sharpened image
sharpened_image_path = "testout.png"
sharpened_image.save(sharpened_image_path)

sharpened_image_path