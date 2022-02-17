from FireCaptcha import Captcha

#initialize captcha instance, specify captcha parameters
p = Captcha(width=600,
            height=200,
            char_number=4,
            char_color='#13cdc7',
            char_type=1,
            gradient='#020e45',
            bg_color='#000',
            misleading_color='#13cd',
            misleading_lines=5,
            misleading_dots=70,)

#generate captcha, no parameters needed
captcha = p.Generate()

#assign image and answer to separate variable
image = captcha.image
answer = captcha.answer

#saves image to file
image.save('images/ex_3.png')

#prints answer to the captcha
print(answer)
