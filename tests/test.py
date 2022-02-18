from FireCaptcha import ImageCaptcha

#initialize captcha instance, specify captcha parameters
p = ImageCaptcha(width=600,
            height=200,
            char_number=6,
            char_color='random',
            char_type=1,
            gradient='random',
            bg_color='random',
            misleading_color='random',
            misleading_lines=5,
            misleading_dots=70,)

#generate captcha, no parameters needed
captcha = p.Generate()

#assign image and answer to separate variable
image = captcha.image
answer = captcha.answer

#saves image to file
image.save('images/test.png')

#prints answer to the captcha
print(answer)
