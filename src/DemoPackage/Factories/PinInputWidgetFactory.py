"""
PinInputWidgetFactory - 引脚输入控件工厂

引脚输入控件工厂负责为未连接的引脚创建编辑器控件。
当引脚未连接到其他节点时，用户可以通过输入控件直接设置引脚的值。

组成部分：
1. 输入控件类：继承自 InputWidgetSingle 或 InputWidgetRaw
2. 工厂函数：根据引脚类型返回对应的控件

输入控件的作用：
- 允许用户直接编辑引脚值（无需连接）
- 提供合适的输入方式（文本框、滑块、颜色选择器等）
- 实时更新引脚数据

常见控件类型：
- 布尔值：QCheckBox（复选框）
- 数值：QSpinBox/QDoubleSpinBox（数字框）或 QSlider（滑块）
- 字符串：QLineEdit（文本框）
- 颜色：QColorDialog（颜色选择器）
- 枚举：QComboBox（下拉框）
"""

from uflow.Core.Common import *
from qtpy import QtCore
from qtpy.QtWidgets import QCheckBox
from uflow.UI.Widgets.InputWidgets import *


class DemoInputWidget(InputWidgetSingle):
    """
    DemoPin 的输入控件

    为 DemoPin 提供复选框（QCheckBox）作为输入方式。
    当 DemoPin 未连接时，用户可以通过勾选/取消复选框来设置引脚值。

    继承层次：
    InputWidgetSingle <- DemoInputWidget

    关键方法：
    - __init__: 创建控件并连接信号
    - setWidgetValue: 设置控件的显示值
    - blockWidgetSignals: 阻止信号（避免循环更新）
    """

    def __init__(self, parent=None, **kwds):
        """
        初始化输入控件

        参数：
            parent: 父控件
            **kwds: 关键字参数，包含：
                - dataSetCallback: 数据变化时的回调函数
                - defaultValue: 默认值

        作用：
        - 创建复选框控件
        - 连接信号到回调函数
        - 设置初始状态

        效果：
        - 创建一个复选框
        - 用户勾选/取消时更新引脚数据
        """
        super(DemoInputWidget, self).__init__(parent=parent, **kwds)

        # 创建复选框控件
        self.cb = QCheckBox(self)

        # 将控件设置为输入控件（显示在节点上）
        self.setWidget(self.cb)

        # 连接复选框的状态变化信号到回调函数
        # 当用户勾选/取消复选框时，会调用 dataSetCallback
        self.cb.stateChanged.connect(lambda val: self.dataSetCallback(bool(val)))

    def blockWidgetSignals(self, bLocked):
        """
        阻止控件信号

        参数：
            bLocked (bool): True 表示阻止信号，False 表示恢复信号

        作用：
        - 在程序设置控件值时阻止信号
        - 避免触发不必要的回调（防止循环更新）

        使用场景：
        - 从外部更新控件值时（如从文件加载）
        - 避免信号循环（setValue -> signal -> setValue -> ...）
        """
        self.cb.blockSignals(bLocked)

    def setWidgetValue(self, val):
        """
        设置控件的显示值

        参数：
            val: 要显示的值（布尔值或可转换为布尔值的类型）

        作用：
        - 更新复选框的勾选状态
        - 反映引脚的当前值

        触发时机：
        - 引脚值被程序修改时
        - 从文件加载图时
        - 引脚连接断开并恢复默认值时

        效果：
        - True: 复选框被勾选
        - False: 复选框未勾选
        """
        if bool(val):
            self.cb.setCheckState(QtCore.Qt.Checked)
        else:
            self.cb.setCheckState(QtCore.Qt.Unchecked)


def getInputWidget(
    dataType, dataSetter, defaultValue, widgetVariant=DEFAULT_WIDGET_VARIANT, **kwds
):
    """
    引脚输入控件工厂函数

    参数：
        dataType (str): 引脚的数据类型名称
        dataSetter (callable): 设置引脚数据的回调函数
        defaultValue: 引脚的默认值
        widgetVariant: 控件变体（用于同一类型的不同显示方式）
        **kwds: 其他关键字参数

    返回：
        InputWidget: 对应的输入控件实例，如果不支持则返回 None

    作用：
        根据引脚类型返回合适的输入控件：
        - DemoPin: 返回 DemoInputWidget（复选框）
        - 其他类型: 返回 None（使用默认控件或无控件）

    添加新控件：
        if dataType == 'MyCustomPin':
            return MyCustomInputWidget(dataSetCallback=dataSetter, defaultValue=defaultValue, **kwds)

    效果：
        - DemoPin 引脚显示复选框输入控件
        - 用户可以直接编辑未连接的引脚值
    """
    # 为 DemoPin 类型返回复选框控件
    if dataType == "DemoPin":
        return DemoInputWidget(
            dataSetCallback=dataSetter, defaultValue=defaultValue, **kwds
        )

    # 对于其他类型，返回 None（使用默认行为）
    # return None  # 隐式返回
