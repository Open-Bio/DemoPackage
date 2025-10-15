"""
UIPinFactory - 引脚 UI 工厂

引脚 UI 工厂负责将引脚逻辑类映射到对应的 UI 类。
当框架需要显示引脚时，会调用工厂函数来创建引脚的 UI 实例。

工作流程：
1. 节点被创建并显示在画布上
2. 框架为每个引脚调用 createUIPin()
3. 工厂检查引脚类型，返回对应的 UI 类
4. 引脚 UI 被添加到节点 UI 上

使用场景：
- 为自定义引脚提供专用 UI
- 自定义引脚形状（方形、菱形等）
- 添加数据预览（颜色、图像缩略图等）
"""

from uflow.UI.Canvas.UIPinBase import UIPinBase
from ..UI.UIDemoPin import UIDemoPin


def createUIPin(owningNode, raw_instance):
    """
    创建引脚的 UI 实例

    参数：
        owningNode (UINodeBase): 拥有此引脚的节点 UI
        raw_instance (PinBase): 引脚的逻辑实例

    返回：
        UIPinBase: 对应的引脚 UI 实例

    作用：
        根据引脚的类型，返回适当的 UI 类实例：
        - 如果是 DemoPin，返回 UIDemoPin（自定义 UI）
        - 否则，返回 UIPinBase（默认 UI）

    效果：
        - DemoPin 使用自定义的 UIDemoPin UI
        - 其他引脚使用默认 UI（圆形）
    """
    # 检查引脚类型并返回对应的 UI 类
    if raw_instance.__class__.__name__ == "DemoPin":
        # DemoPin 使用自定义 UI
        return UIDemoPin(owningNode, raw_instance)
    else:
        # 默认情况：使用基础 UI 类
        return UIPinBase(owningNode, raw_instance)
