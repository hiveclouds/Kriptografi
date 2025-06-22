from PIL import Image, ImageDraw, ImageFont
import time
start_time = time.time()
# Load an image
image = Image.open("Watermark/1.jpg")
draw = ImageDraw.Draw(image)

# Set watermark text and font
text = "This is Visible Watermark uisng Python"
font = ImageFont.truetype("arial.ttf", 50)  # Make sure the font path is correct

# Calculate text bounding box and position
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
x = image.width - text_width - 10  # X position
y = image.height - text_height - 300  # Y position

# Add text watermark with semi-transparency
draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))

# Save the image as a new file
image.save("Watermark/watermarked_image.jpg")  # Use PNG to retain transparency if needed
end_time = time.time()
processing_time = end_time - start_time
print(f"Time taken to process the image: {processing_time:.4f} seconds")
