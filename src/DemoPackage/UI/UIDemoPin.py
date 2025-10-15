"""
UIDemoPin - 自定义引脚 UI 示例

这是引脚的 UI 层实现，负责引脚在画布上的视觉呈现和交互。
继承自 UIPinBase，可以自定义引脚的外观、形状、连接行为等。

引脚 UI 的作用：
- 定义引脚的视觉外观（形状、大小、图标）
- 自定义引脚的绘制（特殊形状、装饰）
- 处理连接交互（拖拽、高亮、验证）
- 显示数据预览或状态

何时需要自定义引脚 UI：
- 需要特殊的引脚形状（如矩形、菱形、自定义图标）
- 需要显示数据预览（如颜色预览、图像缩略图）
- 需要特殊的连接逻辑或验证
- 需要视觉反馈（如数据流动动画）

何时使用默认 UI：
- 标准的圆形引脚即可满足需求
- 不需要额外的视觉反馈
- 引脚行为简单，遵循默认规则
"""

from uflow.UI.Canvas.UIPinBase import UIPinBase


class UIDemoPin(UIPinBase):
    """
    DemoPin 的 UI 类

    负责 DemoPin 在画布上的视觉呈现。
    目前使用默认实现，可以根据需要添加自定义功能。

    继承层次：
    QGraphicsItem <- UIPinBase <- UIDemoPin

    可自定义的方法（示例）：
    - paint(): 自定义引脚的绘制
    - hoverEnterEvent()/hoverLeaveEvent(): 鼠标悬停效果
    - contextMenuBuilder(): 右键菜单
    - canConnectTo(): 连接验证逻辑
    """

    def __init__(self, owningNode, raw_pin):
        """
        初始化引脚 UI

        参数：
            owningNode (UINodeBase): 拥有此引脚的节点 UI
            raw_pin (DemoPin): 底层的引脚逻辑实例

        作用：
        - 调用父类构造函数，初始化基础 UI
        - 连接引脚逻辑和 UI 层
        - 可以在此添加自定义初始化代码

        UI-逻辑分离：
        - raw_pin: 底层引脚逻辑（在 Pins/ 中定义）
        - self: UI 层（当前类）
        - owningNode: 父节点的 UI
        - UI 负责显示，逻辑负责数据

        效果：
        - 创建引脚的图形表示
        - 使用 DemoPin 定义的颜色（黄绿色）
        - 使用默认的圆形形状
        """
        # 调用父类构造函数，初始化基础 UI
        super(UIDemoPin, self).__init__(owningNode, raw_pin)

        # ====================================================================
        # 以下是可选的自定义代码示例（已注释）
        # ====================================================================

        # 示例 1：自定义引脚大小
        # self._pinSize = 10  # 引脚的大小（像素）

    # 示例方法 1：自定义绘制
    # def paint(self, painter, option, widget):
    #     """
    #     自定义引脚的绘制
    #
    #     参数：
    #         painter (QPainter): Qt 绘制器
    #         option: 样式选项
    #         widget: 窗口部件
    #
    #     作用：
    #     - 完全自定义引脚的外观
    #     - 绘制特殊形状（矩形、菱形、星形等）
    #     - 添加装饰（边框、图标、文字等）
    #     - 显示数据预览（如颜色、数值等）
    #
    #     示例：绘制方形引脚
    #     """
    #     from qtpy import QtCore, QtGui
    #
    #     # 获取引脚颜色
    #     color = self.color()
    #
    #     # 设置画笔和画刷
    #     painter.setPen(QtGui.QPen(QtCore.Qt.black, 2))
    #     painter.setBrush(QtGui.QBrush(color))
    #
    #     # 绘制方形引脚
    #     rect = self.boundingRect()
    #     painter.drawRect(rect)
    #
    #     # 如果有连接，绘制边框高亮
    #     if self.hasConnections():
    #         painter.setPen(QtGui.QPen(QtCore.Qt.white, 3))
    #         painter.drawRect(rect)

    # 示例方法 2：自定义形状（用于碰撞检测）
    # def shape(self):
    #     """
    #     定义引脚的碰撞形状
    #
    #     返回：
    #         QPainterPath: 引脚的形状路径
    #
    #     作用：
    #     - 用于鼠标点击检测
    #     - 用于连线碰撞检测
    #     - 应该与 paint() 中绘制的形状匹配
    #
    #     示例：方形形状
    #     """
    #     from qtpy import QtGui
    #     path = QtGui.QPainterPath()
    #     path.addRect(self.boundingRect())
    #     return path

    # 示例方法 3：连接验证
    # def canConnectTo(self, other):
    #     """
    #     验证是否可以连接到另一个引脚
    #
    #     参数：
    #         other (UIPinBase): 目标引脚
    #
    #     返回：
    #         bool: 是否允许连接
    #
    #     作用：
    #     - 自定义连接规则
    #     - 添加额外的类型检查
    #     - 实现特殊的连接逻辑
    #
    #     示例：只允许连接到相同类型的引脚
    #     """
    #     # 先调用父类的验证
    #     if not super(UIDemoPin, self).canConnectTo(other):
    #         return False
    #
    #     # 添加自定义验证逻辑
    #     # 例如：检查数据范围、节点类型等
    #     return True

    # 示例方法 4：鼠标悬停效果
    # def hoverEnterEvent(self, event):
    #     """
    #     鼠标进入引脚区域
    #
    #     参数：
    #         event: 悬停事件
    #
    #     作用：
    #     - 显示工具提示
    #     - 改变引脚外观（高亮、放大等）
    #     - 显示数据预览
    #
    #     示例：显示引脚数据
    #     """
    #     super(UIDemoPin, self).hoverEnterEvent(event)
    #
    #     # 显示当前引脚的数据值
    #     data = self.getData()
    #     if data is not None:
    #         self.setToolTip(f"Value: {data}")
    #
    # def hoverLeaveEvent(self, event):
    #     """鼠标离开引脚区域"""
    #     super(UIDemoPin, self).hoverLeaveEvent(event)
    #     self.setToolTip("")  # 清除提示

    # 示例方法 5：数据变化时的视觉反馈
    # def onPinDataChanged(self, *args, **kwargs):
    #     """
    #     引脚数据变化时调用
    #
    #     作用：
    #     - 更新引脚的视觉表示
    #     - 显示数据预览
    #     - 触发动画效果
    #
    #     示例：数据变化时闪烁
    #     """
    #     super(UIDemoPin, self).onPinDataChanged(*args, **kwargs)
    #
    #     # 可以在这里添加动画、更新预览等
    #     # 例如：颜色闪烁效果
    #     # self.startFlashAnimation()

    # 示例方法 6：显示数据预览（如颜色预览）
    # def updatePreview(self):
    #     """
    #     更新引脚的数据预览
    #
    #     适用于：
    #     - 颜色引脚：显示颜色块
    #     - 图像引脚：显示缩略图
    #     - 数值引脚：显示当前值
    #
    #     示例：假设 DemoPin 存储颜色值
    #     """
    #     data = self.getData()
    #     if isinstance(data, tuple) and len(data) == 3:
    #         # 假设数据是 RGB 颜色
    #         from qtpy import QtGui
    #         color = QtGui.QColor(*data)
    #         self._previewColor = color
    #         self.update()  # 触发重绘
