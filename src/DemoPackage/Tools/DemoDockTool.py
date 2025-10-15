"""
DemoDockTool - 可停靠面板工具示例

DockTool（停靠工具）是可以停靠在 uflow 主窗口周围的面板工具。
提供持续的交互界面，适合需要复杂 UI 或持续监控的功能。

DockTool 的作用：
- 提供可停靠的工具面板
- 显示持续更新的信息（如历史记录、属性、日志）
- 提供复杂的交互界面（表格、树形视图、图表等）
- 监控和调试功能

典型用途：
- 节点浏览器（查看和搜索节点）
- 属性编辑器（编辑选中节点的属性）
- 历史记录（撤销/重做历史）
- 日志查看器（显示运行日志）
- 数据查看器（显示表格、图表等）
- 调试工具（变量监视、性能分析）

DockTool vs ShelfTool：
- DockTool：可停靠面板，提供持续的交互界面
- ShelfTool：工具栏按钮，点击执行一次性操作
"""

from qtpy import QtGui
from uflow.UI.Tool.Tool import DockTool


class DemoDockTool(DockTool):
    """
    演示停靠工具

    提供一个可停靠的面板示例，可以从菜单打开并停靠在主窗口周围。

    继承层次：
    QWidget <- DockTool <- DemoDockTool

    关键方法：
    - name(): 工具的唯一标识
    - toolTip(): 工具提示
    - getIcon(): 工具图标
    - isSingleton(): 是否单例（通常为 True）
    - onShow(): 显示时调用（可选）

    注意：
    - DockTool 本质上是 QWidget，可以添加任意 Qt 控件
    - 在 __init__ 中构建 UI 界面
    """

    def __init__(self):
        """
        初始化停靠工具

        作用：
        - 调用父类构造函数
        - 构建工具的 UI 界面
        - 初始化数据和状态

        UI 构建：
        - 创建布局（QVBoxLayout, QHBoxLayout 等）
        - 添加控件（按钮、列表、表格等）
        - 连接信号和槽
        - 设置样式

        效果：
        - 创建一个空白的停靠面板
        - 可以添加自定义 UI（见下方示例）
        """
        super(DemoDockTool, self).__init__()

        # ====================================================================
        # 以下是 UI 构建示例（已注释）
        # ====================================================================

        # 示例 1：添加简单的标签和按钮
        # from qtpy.QtWidgets import QVBoxLayout, QLabel, QPushButton
        #
        # layout = QVBoxLayout(self)
        # self.setLayout(layout)
        #
        # # 添加标签
        # label = QLabel("This is DemoDockTool")
        # layout.addWidget(label)
        #
        # # 添加按钮
        # btn = QPushButton("Click Me")
        # btn.clicked.connect(self.onButtonClick)
        # layout.addWidget(btn)

        # 示例 2：添加列表控件
        # from qtpy.QtWidgets import QListWidget
        #
        # self.listWidget = QListWidget()
        # layout.addWidget(self.listWidget)
        #
        # # 添加一些项目
        # self.listWidget.addItems(['Item 1', 'Item 2', 'Item 3'])

        # 示例 3：添加表格
        # from qtpy.QtWidgets import QTableWidget
        #
        # self.tableWidget = QTableWidget(5, 3)  # 5 行 3 列
        # self.tableWidget.setHorizontalHeaderLabels(['Name', 'Type', 'Value'])
        # layout.addWidget(self.tableWidget)

    # def onButtonClick(self):
    #     """按钮点击处理示例"""
    #     print("Button clicked in DemoDockTool!")
    #     # 可以访问 uflow 实例
    #     # uflowInstance = self._wrapper.uflowInstance

    # def onShow(self):
    #     """
    #     工具显示时调用（可选）
    #
    #     作用：
    #     - 初始化或刷新数据
    #     - 连接信号
    #     - 启动定时器
    #
    #     示例：每次显示时更新内容
    #     """
    #     super(DemoDockTool, self).onShow()
    #     # 更新数据
    #     # self.refreshData()

    @staticmethod
    def getIcon():
        """
        工具的图标

        返回：
            QIcon: Qt 图标对象

        作用：
        - 显示在工具面板的标题栏
        - 显示在菜单中

        效果：
        - 使用砖块图标
        """
        return QtGui.QIcon(":brick.png")

    @staticmethod
    def toolTip():
        """
        工具的提示文本

        返回：
            str: 工具提示

        作用：
        - 在菜单中显示工具说明
        - 鼠标悬停时的提示

        效果：
        - 显示 "My awesome dock tool!"
        """
        return "My awesome dock tool!"

    @staticmethod
    def name():
        """
        工具的唯一名称

        返回：
            str: 工具标识符

        作用：
        - 唯一标识此工具
        - 用于工具的注册和查找
        - 在代码中引用工具时使用

        重要：
        - 名称在包内必须唯一
        - 建议使用描述性名称

        效果：
        - 工具注册为 "DemoDockTool"
        - 可以通过 invokeDockToolByName("DemoPackage", "DemoDockTool") 打开
        """
        return "DemoDockTool"

    # @staticmethod
    # def isSingleton():
    #     """
    #     是否为单例工具（可选）
    #
    #     返回：
    #         bool: True 表示只能打开一个实例，False 表示可以打开多个
    #
    #     作用：
    #     - 控制工具的实例数量
    #     - 大多数工具都是单例
    #
    #     默认值：True
    #     """
    #     return True
