from FireCaptcha import Captcha

#initialize captcha instance, specify captcha parameters
p = Captcha(width=600,
            height=200,
            char_number=10,
            char_color='random',
            char_type=1,
            gradient='random',
            bg_color='random',
            misleading_color='random',
            misleading_lines=20,
            misleading_dots=200,)

#generate captcha, no parameters needed
captcha = p.Generate()

#assign image and answer to separate variable
image = captcha.image
answer = captcha.answer

#saves image to file
image.save('images/test.png')

#prints answer to the captcha
print(answer)
