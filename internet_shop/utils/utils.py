from PIL import Image


def resize_photo(photo, max_photo_size: int):
    if photo:
        filepath = photo.path
        width = photo.width
        height = photo.height

        max_size = max(width, height)

        if max_size > max_photo_size:
            image = Image.open(filepath)
            image = image.resize(
                (round(width / max_size * max_photo_size),  # Сохраняем пропорции
                 round(height / max_size * max_photo_size)),
                Image.ANTIALIAS)
            image.save(filepath)
