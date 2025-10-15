"""
DemoLib - 函数库示例

函数库（FunctionLibrary）提供了一种快速创建简单节点的方式，
无需编写完整的节点类。适合实现纯函数、数学运算、简单 I/O 等。

函数库 vs 类节点：
- 函数库：简单、快速、适合纯函数
- 类节点：复杂、灵活、适合有状态的操作

适用场景：
- 数学运算（加减乘除、三角函数等）
- 数据转换（类型转换、格式化等）
- 简单 I/O（读写文件、打印等）
- 工具函数（字符串处理、列表操作等）

不适用场景：
- 需要维护状态的操作
- 需要动态创建引脚
- 需要复杂的生命周期管理
- 需要自定义 UI
"""

from uflow.Core.Common import *
from uflow.Core import FunctionLibraryBase
from uflow.Core import IMPLEMENT_NODE


class DemoLib(FunctionLibraryBase):
    """
    演示函数库类

    包含一组相关的函数节点。
    每个函数库通常对应一个功能领域（如数学、字符串处理、文件 I/O 等）。

    继承层次：
    FunctionLibraryBase <- DemoLib

    工作原理：
    1. 定义继承自 FunctionLibraryBase 的类
    2. 添加 @staticmethod 装饰的方法
    3. 用 @IMPLEMENT_NODE 装饰器标记要导出为节点的方法
    4. 框架自动将方法转换为节点

    注意：
    - 所有节点方法必须是静态方法（@staticmethod）
    - 必须使用 @IMPLEMENT_NODE 装饰器
    - 参数和返回值通过特殊格式定义
    """

    def __init__(self, packageName):
        """
        初始化函数库

        参数：
            packageName (str): 所属包的名称

        作用：
        - 调用父类构造函数
        - 注册函数库到包中

        注意：
        - 不要在这里添加其他初始化代码
        - 函数库的方法都是静态的，不依赖实例状态
        """
        super(DemoLib, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(
        returns=None,  # 返回值类型（None 表示无返回值或使用 REF 参数）
        nodeType=NodeTypes.Callable,  # 节点类型（Callable 表示有执行引脚）
        meta={
            NodeMeta.CATEGORY: "DemoLib",  # 节点分类
            NodeMeta.KEYWORDS: [],  # 搜索关键词
        },
    )
    def demoLibGreet(word=("StringPin", "Greet!")):
        """Print greeting message to console.

        This demo node prints the input word to the console when executed.

        **Parameters:**

        - word: String message to print (default: "Greet!")

        **Usage:**

        Connect execution flow to this node and it will print the word parameter.

        .. note::
           Function docstrings must use valid reStructuredText (rst) format.
           Keep formatting simple to avoid parsing errors.
        """
        # 函数体：实际的节点逻辑
        print(word)

        # ====================================================================
        # 开发者注释（不会出现在节点描述中）：
        #
        # 参数定义格式：
        # - 输入参数: param=('PinType', default_value)
        # - 输出参数: output=(REF, ('PinType', default_value))
        #
        # 装饰器说明：
        # - returns: 返回值类型（None 表示无返回值或使用 REF 参数）
        # - nodeType: NodeTypes.Pure（纯函数，自动执行）或 NodeTypes.Callable（有执行引脚）
        # - meta: {NodeMeta.CATEGORY: '分类', NodeMeta.KEYWORDS: ['关键词']}
        # ====================================================================


# ============================================================================
# 下面是更多函数节点的示例，展示不同的参数和返回值模式
# ============================================================================

# 示例 1：纯函数节点（无执行引脚）
# @staticmethod
# @IMPLEMENT_NODE(
#     returns='IntPin',              # 返回整数
#     nodeType=NodeTypes.Pure,       # 纯函数，自动执行
#     meta={
#         NodeMeta.CATEGORY: 'DemoLib|Math',
#         NodeMeta.KEYWORDS: ['add', 'plus', '加法']
#     }
# )
# def add(a=('IntPin', 0), b=('IntPin', 0)):
#     """两数相加"""
#     return a + b

# 示例 2：多个输出参数（使用 REF）
# @staticmethod
# @IMPLEMENT_NODE(
#     returns=None,                  # 使用 REF 参数，所以 returns=None
#     nodeType=NodeTypes.Pure,
#     meta={NodeMeta.CATEGORY: 'DemoLib|Math'}
# )
# def divmod_demo(
#     dividend=('IntPin', 10),       # 被除数
#     divisor=('IntPin', 3),         # 除数
#     quotient=(REF, ('IntPin', 0)), # 商（输出参数）
#     remainder=(REF, ('IntPin', 0)) # 余数（输出参数）
# ):
#     """整数除法，返回商和余数
#
#     REF 参数说明：
#     - REF 表示这是输出参数（引用参数）
#     - 格式：param=(REF, ('PinType', default_value))
#     - 在 UI 中显示为输出引脚
#     - 函数需要显式设置这些参数的值
#     """
#     q, r = divmod(dividend, divisor)
#     quotient.setData(q)   # 设置输出参数的值
#     remainder.setData(r)

# 示例 3：带错误处理的节点
# @staticmethod
# @IMPLEMENT_NODE(
#     returns='StringPin',
#     nodeType=NodeTypes.Callable,
#     meta={NodeMeta.CATEGORY: 'DemoLib|IO'}
# )
# def readFile(path=('StringPin', '')):
#     """读取文件内容
#
#     错误处理：
#     - 捕获异常
#     - 返回错误信息
#     - 避免节点执行中断
#     """
#     try:
#         with open(path, 'r') as f:
#             return f.read()
#     except Exception as e:
#         print(f"Error reading file: {e}")
#         return ""

# 示例 4：接受列表参数
# @staticmethod
# @IMPLEMENT_NODE(
#     returns='IntPin',
#     nodeType=NodeTypes.Pure,
#     meta={NodeMeta.CATEGORY: 'DemoLib|Array'}
# )
# def arraySum(arr=('AnyPin', [], {PinSpecifires.STRUCTURE: StructureType.Array})):
#     """计算数组元素之和
#
#     数组参数：
#     - 使用 PinSpecifires.STRUCTURE: StructureType.Array
#     - 输入引脚可以接受数组数据
#     - 默认值为空列表 []
#     """
#     return sum(arr) if arr else 0
