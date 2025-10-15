"""
DemoPin - 自定义引脚（数据类型）示例

这是一个完整的自定义引脚实现示例，展示了如何在 uflow 中定义新的数据类型。
自定义引脚允许节点之间传递任意类型的数据。

引脚系统组成：
1. 数据类：实际存储的数据结构（如 FakeTypeATWXP）
2. 引脚类：定义引脚的行为、外观和序列化（如 DemoPin）
3. 输入控件：用于编辑引脚值的 UI 控件（在 PinInputWidgetFactory.py 中定义）

适用场景：
- 需要传递自定义数据结构（如自定义对象、复杂数据类型）
- 需要特殊的数据处理或转换逻辑
- 需要自定义引脚的视觉表现（颜色、形状）

示例：
- DataFramePin: 传递 pandas DataFrame
- ImagePin: 传递 OpenCV 图像（numpy 数组）
- ObjectPin: 传递任意 Python 对象
"""

from uflow.Core import PinBase
from uflow.Core.Common import *


class FakeTypeATWXP(object):
    """
    自定义数据类型示例

    这是引脚内部实际存储的数据结构。
    可以是任意 Python 类，用于封装要传递的数据。

    作用：
    - 封装引脚要传递的数据
    - 提供数据操作的方法（如果需要）
    - 作为类型标识（用于类型检查）

    示例用途：
    - 简单值包装：存储单个值（如本例）
    - 复杂数据结构：存储多个字段的对象
    - 数据容器：包装第三方库的数据类型（DataFrame、图像等）

    注意：
    - 类名可以任意命名，不影响引脚类型名称
    - 引脚类型名称由 DemoPin.supportedDataTypes() 定义
    """

    def __init__(self, value=None):
        """
        初始化数据对象

        参数：
            value: 要存储的值（任意类型）

        效果：
        - 创建一个数据容器，存储传入的值
        """
        super(FakeTypeATWXP, self).__init__()
        # 存储实际的数据值
        self.value = value


class DemoPin(PinBase):
    """
    自定义引脚类

    定义引脚的所有行为特性：
    - 数据类型和结构
    - UI 外观（颜色）
    - 数据处理逻辑
    - 序列化方式

    继承层次：
    PinBase <- DemoPin

    关键概念：
    - 引脚类型名称：'DemoPin'（由 supportedDataTypes() 定义）
    - 内部数据类型：FakeTypeATWXP（由 internalDataStructure() 定义）
    - 这两者可以不同，允许灵活的数据封装
    """

    def __init__(self, name, parent, direction, **kwargs):
        """
        初始化引脚实例

        参数：
            name (str): 引脚名称（如 'input', 'output'）
            parent (NodeBase): 拥有此引脚的节点
            direction (PinDirection): 引脚方向（Input 或 Output）
            **kwargs: 其他选项（如 defaultValue, options 等）

        作用：
        - 调用父类构造函数初始化基础功能
        - 设置引脚的默认值
        - 可以配置引脚选项（如是否可序列化、是否允许多连接等）

        效果：
        - 创建一个 DemoPin 类型的引脚实例
        - 默认值为 False
        """
        # 调用父类构造函数
        super(DemoPin, self).__init__(name, parent, direction, **kwargs)

        # 设置引脚的默认值
        # 当引脚未连接且未手动设置值时，使用此默认值
        self.setDefaultValue(False)

        # 可选：配置引脚选项
        # 示例：对于不可序列化的数据类型（如 OpenCV 图像、DataFrame）
        # self.disableOptions(PinOptions.Storable)  # 禁用序列化
        # self.enableOptions(PinOptions.AllowMultipleConnections)  # 允许多个连接

    @staticmethod
    def IsValuePin():
        """
        标识这是否是值引脚（相对于执行引脚）

        返回：
            bool: True 表示是数据引脚，False 表示是执行引脚

        说明：
        - 数据引脚（Value Pin）：传递数据值
        - 执行引脚（Exec Pin）：控制执行流程
        - 大多数自定义引脚都是数据引脚

        效果：
        - 本引脚是数据引脚，可以存储和传递数据
        """
        return True

    @staticmethod
    def supportedDataTypes():
        """
        定义引脚支持的数据类型名称

        返回：
            tuple: 数据类型名称的元组

        重要：
        - 这是引脚的类型标识，用于：
          * 类型匹配：判断两个引脚能否连接
          * 节点创建：在 createInputPin/createOutputPin 中使用此名称
          * UI 显示：在节点浏览器中显示
        - 通常只包含一个类型名称（与类名相同）
        - 可以支持多个类型（用于类型兼容性）

        效果：
        - 引脚类型名称为 'DemoPin'
        - 只有类型为 'DemoPin' 的引脚才能相互连接
        - 在代码中使用：self.createInputPin('name', 'DemoPin')
        """
        return ("DemoPin",)

    @staticmethod
    def pinDataTypeHint():
        """
        提供引脚数据类型提示

        返回：
            tuple: (类型名称, 是否是列表)

        说明：
        - 第一个元素：数据类型名称
        - 第二个元素：是否是列表类型（True/False）

        用途：
        - UI 提示
        - 类型检查
        - 代码补全

        效果：
        - 提示此引脚的类型是 'DemoPin'
        - 不是列表类型（单个值）
        """
        return "DemoPin", False

    @staticmethod
    def color():
        """
        定义引脚在 UI 中的颜色

        返回：
            tuple: RGBA 颜色值 (R, G, B, A)，每个分量范围 0-255

        作用：
        - 在节点画布上区分不同类型的引脚
        - 相同颜色的引脚通常表示相同或兼容的类型
        - 帮助用户快速识别可以连接的引脚

        常见颜色约定（uflowBase）：
        - 白色 (255, 255, 255)：执行引脚
        - 红色 (255, 0, 0)：布尔
        - 绿色 (0, 255, 0)：整数
        - 青色 (0, 255, 255)：浮点
        - 粉色 (255, 0, 255)：字符串
        - 黄色 (255, 255, 0)：列表/数组

        效果：
        - 本引脚显示为黄绿色 (200, 200, 50)
        - 完全不透明 (alpha = 255)
        - 在画布上容易与其他类型区分
        """
        return (200, 200, 50, 255)

    @staticmethod
    def internalDataStructure():
        """
        返回引脚的内部数据结构类

        返回：
            type: 用于存储数据的 Python 类

        作用：
        - 定义引脚实际存储的数据类型
        - 用于数据的包装和解包
        - 提供类型信息给框架

        说明：
        - 可以返回任意 Python 类
        - 对于简单类型，可以返回内置类型（int, str, bool, list 等）
        - 对于复杂类型，返回自定义类（如本例的 FakeTypeATWXP）
        - 对于第三方库类型，直接返回该类型（如 pd.DataFrame）

        效果：
        - 引脚内部使用 FakeTypeATWXP 类来存储数据
        - getData() 返回 FakeTypeATWXP 实例
        """
        return FakeTypeATWXP

    @staticmethod
    def processData(data):
        """
        处理和转换输入数据

        参数：
            data: 要处理的原始数据（任意类型）

        返回：
            处理后的数据（通常是 internalDataStructure() 的实例）

        作用：
        - 将外部数据转换为引脚的内部数据格式
        - 在 setData() 时被调用
        - 提供数据验证和类型转换的机会

        典型用途：
        1. 类型包装：将原始值包装到数据类中
        2. 类型转换：将不同类型转换为统一格式
        3. 数据验证：检查数据是否有效
        4. 数据清洗：规范化输入数据

        示例：
            # 简单包装
            return FakeTypeATWXP(data)

            # 带类型转换
            if isinstance(data, FakeTypeATWXP):
                return data
            else:
                return FakeTypeATWXP(data)

            # 带验证
            if not isinstance(data, (int, bool)):
                raise ValueError("Invalid data type")
            return FakeTypeATWXP(data)

        效果：
        - 将输入的数据包装成 FakeTypeATWXP 实例
        - 确保引脚内部始终存储标准格式的数据
        """
        # 使用内部数据结构包装数据
        return DemoPin.internalDataStructure()(data)
