"""
UINodeFactory - 节点 UI 工厂

UI 工厂负责将节点逻辑类映射到对应的 UI 类。
当框架需要在画布上显示节点时，会调用工厂函数来创建 UI 实例。

工厂模式：
- 输入：节点逻辑实例（NodeBase 的子类）
- 输出：对应的 UI 实例（UINodeBase 的子类）
- 好处：解耦逻辑和 UI，支持自定义外观

工作流程：
1. 用户在画布上创建节点
2. 框架创建节点逻辑实例（如 DemoNode）
3. 框架调用 createUINode(raw_instance)
4. 工厂检查节点类型，返回对应的 UI 类
5. UI 实例被添加到画布上显示

使用场景：
- 为自定义节点提供专用 UI
- 为不同节点类型使用不同的视觉风格
- 添加特殊的交互行为或控件
"""

from uflow.UI.Canvas.UINodeBase import UINodeBase
from ..UI.UIDemoNode import UIDemoNode


def createUINode(raw_instance):
    """
    创建节点的 UI 实例

    参数：
        raw_instance (NodeBase): 节点的逻辑实例

    返回：
        UINodeBase: 对应的 UI 实例

    作用：
        根据节点的类型，返回适当的 UI 类实例：
        - 如果是 DemoNode，返回 UIDemoNode（自定义 UI）
        - 否则，返回 UINodeBase（默认 UI）

    工作原理：
        1. 检查节点实例的类名
        2. 根据类名选择对应的 UI 类
        3. 创建并返回 UI 实例

    添加新映射：
        如果要为其他节点添加自定义 UI：
        1. 创建 UI 类（继承 UINodeBase）
        2. 导入 UI 类
        3. 添加判断分支

    示例：
        if raw_instance.__class__.__name__ == "MyCustomNode":
            return UIMyCustomNode(raw_instance)

    注意：
        - 类名比较是区分大小写的
        - 确保导入所需的 UI 类
        - 如果没有匹配项，会使用默认 UI（UINodeBase）

    效果：
        - DemoNode 使用自定义的 UIDemoNode UI
        - 其他节点使用默认 UI
    """
    # 检查节点类型并返回对应的 UI 类
    if raw_instance.__class__.__name__ == "DemoNode":
        # DemoNode 使用自定义 UI
        return UIDemoNode(raw_instance)

    # 默认情况：使用基础 UI 类
    return UINodeBase(raw_instance)
