"""
DemoPackage - uflow 包开发模板

这是 uflow 框架的完整包示例，展示了如何创建一个功能完整的插件包。
本包包含了所有可能的组件类型，可作为开发新包的参考模板。

包的组件会被自动发现和注册，无需手动导入。
"""

import os
from uflow.Core.PackageBase import PackageBase


class DemoPackage(PackageBase):
    """
    DemoPackage 包定义类

    重要规则：
    1. 类名必须与包目录名完全一致（本例中都是 "DemoPackage"）
    2. 必须继承自 PackageBase
    3. 必须调用 analyzePackage() 来自动扫描和注册组件

    工作原理：
    - uflow 启动时会扫描 Packages 目录下的所有包
    - 加载每个包的 __init__.py 并实例化包类
    - analyzePackage() 会自动发现以下组件：
      * Nodes/       - 类节点（复杂节点）
      * Pins/        - 自定义数据类型
      * FunctionLibraries/ - 函数节点（简单节点）
      * Tools/       - 工具（ShelfTool 和 DockTool）
      * UI/          - 自定义 UI 组件
      * Factories/   - UI 工厂
      * Exporters/   - 导入导出器
      * PrefsWidgets/ - 首选项面板
    """

    def __init__(self):
        """
        初始化包

        步骤：
        1. 调用父类构造函数
        2. 调用 analyzePackage() 自动扫描并注册所有组件

        注意：
        - analyzePackage() 会递归扫描包目录下的所有子目录
        - 每个子目录必须有 __init__.py 文件
        - 组件类必须遵循命名和继承约定才能被识别
        """
        super().__init__()

        # 自动分析并注册包中的所有组件
        # __file__ 是当前 Python 文件的路径
        # os.path.dirname(__file__) 返回包的目录路径
        self.analyzePackage(os.path.dirname(__file__))
