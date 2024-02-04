import cv2
import pytesseract
import os

# 设置TESSDATA_PREFIX环境变量，指向tessdata文件夹所在的路径
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'

# 接下来进行图像识别的代码

# 设置Tesseract OCR的路径，确保你已经安装了Tesseract并配置好路径C:\Program Files\Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 读取身份证图片
image_path = r'E:\360MoveData\Users\crab\Desktop\图片\正面.jpg'
# image_path = r'E:\360MoveData\Users\crab\Desktop\图片\testIDCard.jpg'
img = cv2.imread(image_path)

# 将图片转换为灰度
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 进行图像预处理，例如去噪、二值化等
# 你可能需要根据实际情况调整参数
# _, binary_img = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# 使用Tesseract进行OCR识别
# custom_config = r'--oem 3 --psm 6 outputbase digits'
# text = pytesseract.image_to_string(binary_img, lang='chi_sim+eng', config=custom_config)

text = pytesseract.image_to_string(gray, lang='chi_sim+eng')

# 打印识别结果
print("身份证信息：")
print(text)
