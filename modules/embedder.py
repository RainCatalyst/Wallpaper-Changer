from PIL import Image, ImageFont, ImageDraw, ImageFilter
import config

font = ImageFont.truetype(config.FONT_PATH, config.FONT_SIZE)

def embed_text(in_path, text, out_path):
    image = Image.open(in_path)
    draw = ImageDraw.Draw(image)

    width, height = image.size
    text_width, text_height = draw.textsize(text, font)
    center_x, center_y = (width - text_width - config.PAD, int(height * 0.94) - text_height - config.PAD)
    
    box = tuple(map(int, (center_x - config.PAD, center_y - config.PAD, center_x + text_width + config.PAD, center_y + text_height + config.PAD)))
    cropped = image.crop(box)
    for i in range(10):
        cropped = cropped.filter(ImageFilter.BLUR)
    image.paste(cropped, box)
    draw.text((center_x, center_y), text, (255, 255, 255), font = font)
    

    image.save(out_path)