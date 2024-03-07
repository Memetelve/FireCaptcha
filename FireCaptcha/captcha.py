import os
import random
import math

from PIL import Image, ImageDraw, ImageFont


FONTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "fonts")
DEFAULT_FONT = os.path.join(FONTS_DIR, "Monaco.ttf")


class FinishedCaptcha:
    def __init__(self, image, answer):
        self.image = image
        self.answer = answer


class ImageCaptcha:
    @staticmethod
    def generate_gradient(colour1: str, colour2: str, width: int, height: int) -> Image:
        """Generate a vertical gradient."""
        base = Image.new("RGB", (width, height), colour1)
        top = Image.new("RGB", (width, height), colour2)
        mask = Image.new("L", (width, height))
        mask_data = []
        for y in range(height):
            mask_data.extend([int(255 * (y / height))] * width)
        mask.putdata(mask_data)
        base.paste(top, (0, 0), mask)
        return base

    @staticmethod
    def generate_position(i, font_size, image_width, image_height, char_number):
        offset_x = int(image_width / char_number * 0.4)
        offset_y = font_size

        space_for_char = image_width / char_number

        x_min = space_for_char * i + offset_x
        x_max = space_for_char * (i + 1) - offset_x

        y_min = 0
        y_max = image_height - offset_y * 1.2

        x = random.randint(int(x_min), int(x_max))
        y = random.randint(y_min, int(y_max))

        return x, y

    @staticmethod
    def draw_chars(chars, char_number, char_color, image):

        height = image.height
        width = image.width

        answer = ""
        for i in range(char_number):
            char = random.choice(chars)

            answer += char

            font_size = random.randint(
                math.floor(height * 0.3), math.floor(height * 0.4)
            )

            x, y = ImageCaptcha.generate_position(
                i, font_size, width, height, char_number
            )

            font = ImageFont.truetype("arial", font_size)
            # draw char
            draw = ImageDraw.Draw(image)

            if char_color.lower() == "random":
                # generate random hex color
                color = "#" + "".join(
                    [random.choice("0123456789ABCDEF") for _ in range(6)]
                )

                draw.text((x, y), char, color, font)
            else:
                draw.text((x, y), char, char_color, font)

        return answer, image

    @staticmethod
    def draw_misleading_lines(image, misleading_color, misleading_lines):

        height = image.height
        width = image.width

        if misleading_lines <= 0:
            return image
        draw = ImageDraw.Draw(image)
        for _ in range(misleading_lines):
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = random.randint(0, width)
            y2 = random.randint(0, height)

            if misleading_color.lower() == "random":
                color = "#" + "".join(
                    [random.choice("0123456789ABCDEF") for _ in range(6)]
                )
                draw.line((x1, y1, x2, y2), fill=color, width=4)
            else:
                draw.line((x1, y1, x2, y2), fill=misleading_color, width=4)

        return image

    @staticmethod
    def draw_misleading_dots(image, misleading_color, misleading_dots):

        height = image.height
        width = image.width

        if misleading_dots <= 0:
            return image
        draw = ImageDraw.Draw(image)
        for _ in range(misleading_dots):
            x = random.randint(0, width)
            y = random.randint(0, height)
            radius = random.randint(0, width // 30)

            if misleading_color.lower() == "random":
                color = "#" + "".join(
                    [random.choice("0123456789ABCDEF") for _ in range(6)]
                )
                draw.ellipse((x, y, x + radius, y + radius), fill=color)
            else:
                draw.ellipse((x, y, x + radius, y + radius), fill=misleading_color)

        return image

    @staticmethod
    def Generate(
        width: int = 300,
        height: int = 100,
        char_number: int = 4,
        char_color: str = "#3ee6f9",
        char_type: int = 1,
        bg_color: str = "#343232",
        bg_color_2: str = "",
        misleading_lines: int = 0,
        misleading_dots: int = 0,
        misleading_color: str = "#e6cd79",
    ) -> FinishedCaptcha:

        if bg_color.lower() == "random":
            bg_color = "#" + "".join(
                [random.choice("0123456789ABCDEF") for _ in range(6)]
            )
        if bg_color_2.lower() == "random":
            bg_color_2 = "#" + "".join(
                [random.choice("0123456789ABCDEF") for _ in range(6)]
            )

        if bg_color_2:
            image = ImageCaptcha.generate_gradient(bg_color_2, bg_color, width, height)
        else:
            image = Image.new("RGB", (width, height), bg_color)

        if char_type == 1:
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        elif char_type == 2:
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXY"
        elif char_type == 3:
            chars = "abcdefghijklmnopqrstuvwxyz"
        elif char_type == 4:
            chars = "0123456789"

        answer, image = ImageCaptcha.draw_chars(chars, char_number, char_color, image)

        image_with_lines = ImageCaptcha.draw_misleading_lines(
            image, misleading_color, misleading_lines
        )

        image_with_dots = ImageCaptcha.draw_misleading_dots(
            image_with_lines, misleading_color, misleading_dots
        )

        return FinishedCaptcha(image_with_dots, answer)
