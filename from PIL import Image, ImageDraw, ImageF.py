from PIL import Image, ImageDraw, ImageFont

def create_profile_image(output_filename="hayalimdi_profile.png", width=500, height=500):
    # Pastel tonlarda renkler (soluk mor, hafif mavi, pembe)
    pastel_purple = (210, 180, 235)  # Soluk mor
    pastel_blue   = (173, 216, 230)  # Hafif mavi
    pastel_pink   = (255, 182, 193)  # Pembe

    # RGBA modunda yeni bir resim oluşturuyoruz
    img = Image.new("RGBA", (width, height))
    draw = ImageDraw.Draw(img)

    # Üst yarıda soluk mor'dan hafif mavi'ya, alt yarıda hafif mavi'den pembe'ye geçiş yapan dikey degrade oluşturuyoruz.
    for y in range(height):
        if y < height // 2:
            t = y / (height // 2)  # 0'dan 1'e kadar
            r = int(pastel_purple[0] * (1 - t) + pastel_blue[0] * t)
            g = int(pastel_purple[1] * (1 - t) + pastel_blue[1] * t)
            b = int(pastel_purple[2] * (1 - t) + pastel_blue[2] * t)
        else:
            t = (y - height // 2) / (height // 2)
            r = int(pastel_blue[0] * (1 - t) + pastel_pink[0] * t)
            g = int(pastel_blue[1] * (1 - t) + pastel_pink[1] * t)
            b = int(pastel_blue[2] * (1 - t) + pastel_pink[2] * t)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Ortada hafif şeffaf bir daire çiziyoruz
    circle_radius = 100
    circle_bbox = [
        width // 2 - circle_radius,
        height // 2 - circle_radius,
        width // 2 + circle_radius,
        height // 2 + circle_radius,
    ]
    circle_color = (255, 255, 255, 180)  # Beyaz, biraz şeffaf
    draw.ellipse(circle_bbox, fill=circle_color)

    # Dairenin hemen altına "hayalimdi" metnini ekliyoruz.
    text = "hayalimdi"
    try:
        # Sisteminizde arial.ttf varsa kullanılır. Yoksa default font kullanılır.
        font = ImageFont.truetype("arial.ttf", size=30)
    except IOError:
        font = ImageFont.load_default()

    text_width, text_height = draw.textsize(text, font=font)
    text_position = (width // 2 - text_width // 2, height // 2 + circle_radius + 10)
    draw.text(text_position, text, font=font, fill=(255, 255, 255))

    # Görseli kaydediyoruz
    img.save(output_filename)
    print(f"Profil resmi '{output_filename}' olarak kaydedildi.")

if __name__ == "__main__":
    create_profile_image()
