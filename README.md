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
            gradient_color='#13c',
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

## Examples
