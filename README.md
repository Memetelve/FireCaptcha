# FireCaptcha

Python random captcha package, which is very customizable

## Instalation

- FireCaptcha uses Pillow to generate images, on linux distros you have to install Pillow dependencies alone

```bash
sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk
```

- then / 1st step on windows

```bash
pip install FireCaptcha
```

## Usage

```python
from FireCaptcha import Captcha

#initialize captcha instance, specify captcha parameters
p = Captcha(width=600,
            height=200,
            char_number=5,
            char_color='#13cdc7',
            char_type=3,
            bg_color='#000',
            gradient='#13c',
            misleading_lines=3,
            misleading_dots=20,
            misleading_color='#444444')

#generate captcha, no parameters needed
captcha = p.Generate()

#assign image and answer to separate variable
image = captcha.image
answer = captcha.answer

#saves image to file
image.save('images/test.png')

#prints answer to the captcha
print(answer)
```

## Parameters

```
width: int - width of captcha in px
height: int - height of captcha in px
char_number: int - how many characters should be on captcha
char_color: str - color of characters in hex (with #) e.g: #ff0000
char_type: int<1,4> - type of characters:
    1 - 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    2 - 'ABCDEFGHIJKLMNOPQRSTUVWXY'
    3 - 'abcdefghijklmnopqrstuvwxyz'
    4 - '0123456789'
bg_color: str - color of background in hex (with #) e.g: #ff0000
gradient: str - color of gradient in hex (with #) e.g: #ff0000 (this color on top, bg_color on botton)
    (if not specified no   gradient)
misleading_lines: int - amount of misleading lines
misleading_dots: int - amount of misleading dots/circles
misleading_color: str - color of misleading components in hex (with #) e.g: #ff0000
```

## Examples

![example 1](https://raw.githubusercontent.com/Memetelve/FireCaptcha/master/images/ex_1.png)
![example 1](https://raw.githubusercontent.com/Memetelve/FireCaptcha/master/images/ex_2.png)
![example 1](https://raw.githubusercontent.com/Memetelve/FireCaptcha/master/images/ex_3.png)