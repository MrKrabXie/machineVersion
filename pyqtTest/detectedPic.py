import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class DetectionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('YOLOACT Image Detection')
        self.setGeometry(100, 100, 600, 400)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setPixmap(QPixmap('placeholder_image.png'))  # 设置默认图片

        self.upload_button = QPushButton('上传图像', self)
        self.upload_button.clicked.connect(self.upload_image)

        self.result_label = QLabel('检测结果将显示在这里', self)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.upload_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def upload_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, '选择图像文件', '', 'Images (*.png *.jpg *.jpeg)')

        if file_path:
            # 在这里调用处理图像的函数，更新结果并显示
            self.process_image(file_path)

    def process_image(self, image_path):
        # 在这里调用YOLOACT模型，获取检测结果
        # detection_result = yoloact_model.detect(image)

        # 这里使用一个假的检测结果来演示
        detection_result = {'objects': ['person', 'car', 'dog'], 'confidence': [0.85, 0.92, 0.78]}

        # 更新界面显示
        self.show_detection_result(detection_result)

    def show_detection_result(self, result):
        # 在结果标签中显示检测结果
        result_text = f"检测到的对象: {', '.join(result['objects'])}\n置信度: {', '.join(map(str, result['confidence']))}"
        self.result_label.setText(result_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DetectionApp()
    window.show()
    sys.exit(app.exec())
