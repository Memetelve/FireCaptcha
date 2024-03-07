from captcha import ImageCaptcha

image = ImageCaptcha.Generate(
    width=300,
    height=100,
    char_number=4,
    char_color="#ffffff",
    char_type=1,
    bg_color="#000000",
    bg_color_2="",
    misleading_lines=0,
    misleading_dots=0,
    misleading_color="random",
)


print(image.answer)
image.image.save("test.png")
