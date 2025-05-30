from PIL import Image

def double_negative(image_path):
    im = Image.open(image_path).convert("RGB")
    negative_pixels = [(255 - r, 255 - g, 255 - b) for (r, g, b) in im.getdata()]
    im.putdata(negative_pixels)
    return im

def apply_sunset_filter(image_path):
    im = Image.open(image_path).convert("RGB")
    sunset_pixels = [(r, int(g * 0.5), int(b * 0.5)) for (r, g, b) in im.getdata()]
    im.putdata(sunset_pixels)
    return im

def apply_grayscale_filter(image_path):
    im = Image.open(image_path).convert("RGB")
    grayscale_pixels = [(int((r + g + b) / 3),) * 3 for (r, g, b) in im.getdata()]
    im.putdata(grayscale_pixels)
    return im
