import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
# https://doc.qt.io/qtforpython-6/quickstart.html#quick-start
# 这两个示例是使用 PySide6 创建简单 Qt 应用的不同实现方式：
#
# 1. **QML 版本：**
# - 这个版本使用 QML（Qt Meta-Object Language），这是一种描述 Qt 应用结构和行为的标记语言。
# - 应用窗口的结构在 QML 语法中定义，包括 `Window`、`ColumnLayout`、`Text` 和 `Button` 等组件。
# - 在 QML 中定义了 `setText` 函数，用于随机设置 `Text` 元素的文本为预定义的字符串之一。
# - QML 文件加载到 `QQmlApplicationEngine` 中，并启动应用的主循环。
#
# 2. **QWidget 版本：**
# - 这个版本使用基于 QWidget 的传统方法。
# - 通过子类化 `QtWidgets.QWidget` 创建了一个自定义小部件（`MyWidget`）。
# - 小部件包含一个 `QPushButton` 和一个使用垂直布局（`QVBoxLayout`）排列的 `QLabel`。
# - `magic` 方法连接到按钮的 `clicked` 信号，它随机设置标签的文本为预定义的字符串之一。
# - 创建了 QApplication，实例化了自定义小部件，显示了它，并启动了应用的主循环。
#
# **区别:**
# - QML 版本使用一种声明性语言描述 UI，而 QWidget 版本使用 Python 进行命令式编程来创建和控制 UI。
# - QML 通常用于更复杂的 UI，特别是在 QtQuick 应用中很常见，而基于 QWidget 的应用程序采用更传统的方式。
# - QML 版本可能更灵活，允许在 UI 和逻辑之间进行分离，而 QWidget 版本提供了创建桌面应用程序的更 Pythonic 和熟悉的方式。

QML = """
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 200
    visible: true
    title: "Hello World"

    readonly property list<string> texts: ["Hallo Welt", "Hei maailma",
                                           "Hola Mundo", "Привет мир"]

    function setText() {
        var i = Math.round(Math.random() * 3)
        text.text = texts[i]
    }

    ColumnLayout {
        anchors.fill:  parent

        Text {
            id: text
            text: "Hello World"
            Layout.alignment: Qt.AlignHCenter
        }
        Button {
            text: "Click me"
            Layout.alignment: Qt.AlignHCenter
            onClicked:  setText()
        }
    }
}
"""

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.loadData(QML.encode('utf-8'))
    if not engine.rootObjects():
        sys.exit(-1)
    exit_code = app.exec()
    del engine
    sys.exit(exit_code)