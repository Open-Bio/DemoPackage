"""
DemoShelfTool - 工具栏按钮示例

ShelfTool（架子工具）是显示在 uflow 主窗口工具栏上的快速操作按钮。
用户点击按钮时执行特定的操作，适合频繁使用的功能。

ShelfTool 的作用：
- 提供快速访问的功能按钮
- 执行一次性操作（创建节点、运行脚本、打开工具等）
- 触发某些动作（保存、导出、执行等）
- 打开 DockTool 或对话框

典型用途：
- 创建特定类型的节点
- 执行图的验证或优化
- 快速导入/导出
- 运行自定义脚本
- 打开设置或帮助

ShelfTool vs DockTool：
- ShelfTool：工具栏按钮，点击执行操作
- DockTool：可停靠面板，提供持续的交互界面
"""

from uflow.UI.Tool.Tool import ShelfTool
from uflow.Core.Common import Direction

from qtpy import QtGui


class DemoShelfTool(ShelfTool):
    """
    演示工具栏按钮

    提供一个简单的工具栏按钮示例，点击时在控制台打印 "Greet!"。

    继承层次：
    ShelfTool <- DemoShelfTool

    关键方法：
    - name(): 工具的唯一标识
    - toolTip(): 鼠标悬停提示
    - getIcon(): 工具图标
    - do(): 点击时执行的操作
    """

    def __init__(self):
        """
        初始化工具栏按钮

        作用：
        - 调用父类构造函数
        - 可以初始化工具的状态（如果需要）

        注意：
        - 工具通常是无状态的
        - 大部分逻辑应在 do() 方法中实现
        """
        super(DemoShelfTool, self).__init__()

    @staticmethod
    def toolTip():
        """
        工具的提示文本

        返回：
            str: 鼠标悬停时显示的提示文本

        作用：
        - 告诉用户此工具的功能
        - 显示在工具栏按钮的 tooltip 中
        - 帮助用户理解工具的用途

        效果：
        - 鼠标悬停在按钮上时显示此文本
        """
        return "This is my new awesome shelf button"

    @staticmethod
    def getIcon():
        """
        工具的图标

        返回：
            QIcon: Qt 图标对象

        作用：
        - 定义工具栏按钮的图标
        - 使用 uflow 内置图标资源或自定义图标
        - 提供视觉识别

        图标资源：
        - 内置图标：使用 ":" 前缀（如 ":brick.png"）
        - 自定义图标：提供文件路径
        - 图标文件通常放在包的 resources 目录中

        效果：
        - 在工具栏上显示砖块图标
        """
        return QtGui.QIcon(":brick.png")

    @staticmethod
    def name():
        """
        工具的唯一名称

        返回：
            str: 工具的标识符

        作用：
        - 唯一标识此工具
        - 用于工具的注册和查找
        - 在代码中引用工具时使用

        重要：
        - 名称在包内必须唯一
        - 建议使用描述性名称
        - 通常与类名相同

        效果：
        - 工具注册为 "DemoShelfTool"
        - 可以通过此名称调用工具
        """
        return "DemoShelfTool"

    def do(self):
        """
        执行工具的操作（点击时调用）

        作用：
        - 实现工具的核心功能
        - 点击工具栏按钮时被调用
        - 可以访问 uflow 实例和画布

        可用的操作：
        1. 访问 uflow 实例
        2. 创建节点
        3. 操作图
        4. 打开对话框或工具
        5. 执行脚本

        效果：
        - 点击按钮时在控制台打印 "Greet!"

        示例用法（已注释）见下方
        """
        # 当前功能：简单打印
        print("Greet!")

        # ====================================================================
        # 以下是更多操作示例（已注释）
        # ====================================================================

        # 示例 1：访问 uflow 实例
        # uflowInstance = self.uflowInstance
        # if uflowInstance:
        #     print(f"Current app: {uflowInstance}")

        # 示例 2：在画布上创建节点
        # canvas = uflowInstance.getCanvas()
        # graph = uflowInstance.graphManager.activeGraph()
        # if graph:
        #     # 创建一个 DemoNode
        #     node = graph.createNode('DemoNode', name='MyDemo')
        #     print(f"Created node: {node.getName()}")

        # 示例 3：打开 DockTool
        # uflowInstance.invokeDockToolByName("DemoPackage", "DemoDockTool")

        # 示例 4：显示消息对话框
        # from qtpy.QtWidgets import QMessageBox
        # QMessageBox.information(None, "Demo Tool", "Hello from DemoShelfTool!")

        # 示例 5：执行图
        # graph = uflowInstance.graphManager.activeGraph()
        # if graph:
        #     graph.evaluate()
        #     print("Graph evaluated!")

        # 示例 6：保存当前图
        # uflowInstance.currentSoftware.saveGraph()

        # 示例 7：创建多个节点并连接它们
        # graph = uflowInstance.graphManager.activeGraph()
        # if graph:
        #     # 创建两个节点
        #     node1 = graph.createNode('DemoNode', name='Node1')
        #     node2 = graph.createNode('DemoNode', name='Node2')
        #
        #     # 连接节点
        #     out_pin = node1.getPin('out')
        #     in_pin = node2.getPin('inp')
        #     if out_pin and in_pin:
        #         out_pin.connectTo(in_pin)
        #         print("Nodes connected!")

        # 示例 8：遍历所有节点
        # graph = uflowInstance.graphManager.activeGraph()
        # if graph:
        #     for node in graph.nodes.values():
        #         print(f"Node: {node.getName()}, Type: {node.__class__.__name__}")

        # 示例 9：获取选中的节点
        # canvas = uflowInstance.getCanvas()
        # selected_nodes = canvas.getSelectedNodes()
        # print(f"Selected {len(selected_nodes)} nodes")
        # for ui_node in selected_nodes:
        #     print(f"  - {ui_node.getName()}")
