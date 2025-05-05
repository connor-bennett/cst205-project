from PIL import Image

def double_negative(image_path, save_path='negative_penguin.png'):
    """Create a negative of an image, then negate it again."""
    im = Image.open(image_path)
    negative_pixels = [(255 - r, 255 - g, 255 - b) for (r, g, b) in im.getdata()]
    im.putdata(negative_pixels)
    im.save(save_path)

def apply_sunset_filter(image_path, save_path=None):
    """Apply a sunset effect by reducing green and blue channels."""
    im = Image.open(image_path)
    sunset_pixels = [(r, int(g * 0.5), int(b * 0.5)) for (r, g, b) in im.getdata()]
    im.putdata(sunset_pixels)
    if save_path:
        im.save(save_path)

def apply_grayscale_filter(image_path, save_path=None):
    """Convert an image to grayscale."""
    im = Image.open(image_path)
    grayscale_pixels = [
        (int((r + g + b) / 3),) * 3 for (r, g, b) in im.getdata()
    ]
    im.putdata(grayscale_pixels)
    if save_path:
        im.save(save_path)
