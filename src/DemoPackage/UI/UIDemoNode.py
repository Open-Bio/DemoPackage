"""
UIDemoNode - 自定义节点 UI 示例

这是节点的 UI 层实现，负责节点在画布上的视觉呈现和交互。
继承自 UINodeBase，可以自定义节点的外观、颜色、形状、控件等。

UI 层的作用：
- 定义节点的视觉外观（颜色、形状、大小）
- 添加自定义控件（按钮、滑块、下拉框等）
- 处理用户交互（点击、拖拽、右键菜单等）
- 自定义绘制逻辑（特殊形状、装饰、动画等）

何时需要自定义节点 UI：
- 需要特殊的外观（如不同的颜色方案）
- 需要在节点上添加交互控件
- 需要自定义绘制（如进度条、预览图等）
- 需要特殊的布局或排列

何时使用默认 UI：
- 标准的节点外观即可满足需求
- 不需要额外的交互控件
- 节点逻辑简单，不需要视觉反馈
"""

from uflow.UI.Canvas.UINodeBase import UINodeBase


class UIDemoNode(UINodeBase):
    """
    DemoNode 的 UI 类

    负责 DemoNode 在画布上的视觉呈现。
    目前使用默认实现，可以根据需要添加自定义功能。

    继承层次：
    QGraphicsWidget <- UINodeBase <- UIDemoNode

    可自定义的方法（示例）：
    - postCreate(): 节点创建后的初始化（添加控件）
    - paint(): 自定义绘制逻辑
    - mousePressEvent(): 处理鼠标点击
    - createInputWidgets(): 为引脚创建输入控件
    - serialize()/deserialize(): 保存/加载 UI 状态
    """

    def __init__(self, raw_node):
        """
        初始化节点 UI

        参数：
            raw_node (DemoNode): 底层的节点逻辑实例

        作用：
        - 调用父类构造函数，初始化基础 UI
        - 连接节点逻辑和 UI 层
        - 可以在此添加自定义初始化代码

        UI-逻辑分离：
        - raw_node: 底层节点逻辑（在 Nodes/ 中定义）
        - self: UI 层（当前类）
        - 通过 self.node() 访问底层节点
        - UI 负责显示，逻辑负责计算

        效果：
        - 创建节点的图形表示
        - 自动创建引脚的 UI
        - 使用默认的节点外观
        """
        # 调用父类构造函数，初始化基础 UI
        super(UIDemoNode, self).__init__(raw_node)

        # ====================================================================
        # 以下是可选的自定义代码示例（已注释）
        # ====================================================================

        # 示例 1：自定义节点颜色
        # self.color = QtGui.QColor(100, 100, 200)  # 自定义节点颜色
        # self.headColor = QtGui.QColor(150, 150, 250)  # 标题栏颜色

        # 示例 2：添加自定义控件（在 postCreate 中实现更合适）
        # 通常在 postCreate() 方法中添加控件

    # 示例方法 1：节点创建后的初始化
    # def postCreate(self, jsonTemplate=None):
    #     """
    #     节点创建后调用，用于添加自定义控件
    #
    #     参数：
    #         jsonTemplate: 节点的序列化数据（如果是从文件加载）
    #
    #     作用：
    #     - 添加自定义 Qt 控件到节点
    #     - 连接信号和槽
    #     - 初始化 UI 状态
    #
    #     示例：添加一个按钮
    #     """
    #     super(UIDemoNode, self).postCreate(jsonTemplate)
    #
    #     # 添加一个按钮
    #     from qtpy.QtWidgets import QPushButton
    #     btn = QPushButton("Click Me")
    #     btn.clicked.connect(self.onButtonClicked)
    #     self.createInputWidget("", btn)  # 添加到节点上
    #
    # def onButtonClicked(self):
    #     """按钮点击处理"""
    #     print("Button clicked on", self.getName())

    # 示例方法 2：自定义绘制
    # def paint(self, painter, option, widget):
    #     """
    #     自定义节点的绘制
    #
    #     参数：
    #         painter (QPainter): Qt 绘制器
    #         option: 样式选项
    #         widget: 窗口部件
    #
    #     作用：
    #     - 完全自定义节点的外观
    #     - 绘制特殊形状、图标、装饰等
    #     - 添加视觉反馈（如高亮、阴影）
    #
    #     示例：绘制自定义背景
    #     """
    #     # 先调用父类绘制基础外观
    #     super(UIDemoNode, self).paint(painter, option, widget)
    #
    #     # 在节点上绘制自定义内容
    #     from qtpy import QtCore
    #     rect = self.boundingRect()
    #     painter.setPen(QtCore.Qt.yellow)
    #     painter.drawText(rect, QtCore.Qt.AlignCenter, "DEMO")

    # 示例方法 3：右键菜单自定义
    # def contextMenuBuilder(self):
    #     """
    #     自定义节点的右键菜单
    #
    #     返回：
    #         QMenu: 右键菜单对象
    #
    #     作用：
    #     - 添加自定义菜单项
    #     - 提供节点特定的操作
    #
    #     示例：添加一个菜单项
    #     """
    #     menu = super(UIDemoNode, self).contextMenuBuilder()
    #
    #     # 添加自定义菜单项
    #     action = menu.addAction("Custom Action")
    #     action.triggered.connect(self.onCustomAction)
    #
    #     return menu
    #
    # def onCustomAction(self):
    #     """自定义菜单项的处理"""
    #     print("Custom action triggered!")

    # 示例方法 4：访问底层节点
    # def updateNodeShape(self):
    #     """
    #     更新节点形状（示例）
    #
    #     演示如何访问底层节点的数据
    #     """
    #     # 通过 self 访问底层节点
    #     node = self  # self 同时是 UI 和节点的接口
    #
    #     # 或者通过 raw_node
    #     # raw_node = self.node()
    #
    #     # 访问引脚
    #     inp_pin = self.getPin("inp")
    #     if inp_pin:
    #         data = inp_pin.getData()
    #         print(f"Input pin data: {data}")
