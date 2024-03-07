import pytesseract
from PIL import Image

# 读取图片
pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\Tesseract-OCR\tesseract.exe'
image = Image.open('baidu.png')
# 列出支持的语言
print(pytesseract.get_languages(config=''))
text = pytesseract.image_to_string(image, lang='chi_sim')
print(text)

