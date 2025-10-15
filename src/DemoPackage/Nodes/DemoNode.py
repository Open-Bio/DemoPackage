"""
DemoNode - 类节点示例

这是一个完整的类节点实现示例，展示了如何创建有状态的、复杂的节点。
本例实现了一个简单的布尔取反节点。

适用场景：
- 需要维护内部状态
- 需要动态创建/删除引脚
- 需要自定义 UI
- 需要执行流控制（ExecPin）
- 复杂的计算逻辑

不适用场景：
- 简单的纯函数转换（应使用 FunctionLibrary）
- 无状态的计算（应使用 FunctionLibrary）
"""

from uflow.Core import NodeBase
from uflow.Core.NodeBase import NodePinsSuggestionsHelper
from uflow.Core.Common import *


class DemoNode(NodeBase):
    """
    演示节点类

    功能：接收一个布尔值输入，输出其取反值（True -> False, False -> True）

    继承层次：
    NodeBase <- DemoNode

    生命周期：
    1. __init__: 创建节点实例，初始化引脚
    2. compute: 每当输入数据变化时被调用
    3. 当节点被删除时，框架自动清理资源
    """

    def __init__(self, name):
        """
        初始化节点

        参数：
            name (str): 节点的唯一名称，由框架自动生成

        作用：
        - 调用父类构造函数
        - 创建输入和输出引脚
        - 初始化节点的内部状态（如有需要）

        引脚创建说明：
        - createInputPin(name, type, defaultValue, options): 创建输入引脚
        - createOutputPin(name, type, defaultValue, options): 创建输出引脚
        - 引脚类型必须是已注册的类型（如 'BoolPin', 'IntPin', 'StringPin' 等）

        效果：
        - 节点在画布上显示时会有两个引脚：
          * 左侧：inp (红色，布尔输入)
          * 右侧：out (红色，布尔输出)
        """
        # 调用父类构造函数，传入节点名称
        super(DemoNode, self).__init__(name)

        # 创建输入引脚
        # 参数：引脚名称, 引脚类型
        # BoolPin 在 UI 中显示为红色
        self.inp = self.createInputPin("inp", "BoolPin")

        # 创建输出引脚
        # 输出引脚通常不设置默认值
        self.out = self.createOutputPin("out", "BoolPin")

    @staticmethod
    def pinTypeHints():
        """
        提供引脚类型提示（用于动态引脚创建）

        作用：
        - 当用户想要动态添加引脚时，这个方法提供可选的引脚类型
        - 在节点的右键菜单中显示 "Add input/output" 选项
        - 用于支持可变数量引脚的节点（如 MakeArray, Select 等）

        返回：
            NodePinsSuggestionsHelper: 包含引脚类型建议的辅助对象

        效果：
        - 本节点支持动态添加 BoolPin 类型的引脚
        - 新引脚只能是 Single 结构（不能是 Array）

        注意：
        - 如果节点不需要动态引脚，可以返回空的 helper 或不实现此方法
        """
        helper = NodePinsSuggestionsHelper()

        # 添加可用的输入引脚数据类型
        helper.addInputDataType("BoolPin")

        # 添加可用的输出引脚数据类型
        helper.addOutputDataType("BoolPin")

        # 添加输入引脚的结构类型
        # StructureType.Single: 单个值
        # StructureType.Array: 数组
        # StructureType.Multi: 多值（可接受多个连接）
        helper.addInputStruct(StructureType.Single)

        # 添加输出引脚的结构类型
        helper.addOutputStruct(StructureType.Single)

        return helper

    @staticmethod
    def category():
        """
        定义节点的分类

        作用：
        - 在节点浏览器中组织节点
        - 支持多级分类，用 '|' 分隔（如 'Math|Trigonometry'）
        - 用户可以通过分类快速找到相关节点

        返回：
            str: 节点的分类路径

        效果：
        - 本节点出现在节点浏览器的 "Generated from wizard" 分类下
        - 可以改为其他分类，如 'Demo', 'Logic|Boolean', 'Utils' 等
        """
        return "Generated from wizard"

    @staticmethod
    def keywords():
        """
        定义节点的搜索关键词

        作用：
        - 用于节点浏览器的搜索功能
        - 用户可以通过关键词快速找到节点
        - 支持多种语言和同义词

        返回：
            list: 关键词列表

        示例：
            return ['not', 'invert', 'negate', '取反', '否定']

        效果：
        - 本节点目前没有额外关键词（仅通过类名搜索）
        - 添加关键词可以提高可发现性
        """
        return []

    @staticmethod
    def description():
        """
        节点的描述文本

        作用：
        - 在节点浏览器中显示节点说明
        - 支持 reStructuredText (rst) 格式
        - 可以包含使用说明、示例、注意事项等

        返回：
            str: 描述文本（rst 格式）

        示例：
            return '''
            **DemoNode** - 布尔取反节点

            接收一个布尔值输入，输出其取反值。

            示例：
            - 输入 True -> 输出 False
            - 输入 False -> 输出 True

            用途：
            - 逻辑运算
            - 条件判断
            '''

        效果：
        - 鼠标悬停在节点上时可能显示此描述
        - 在文档生成时使用
        """
        return "Description in rst format."

    def compute(self, *args, **kwargs):
        """
        节点的计算逻辑（核心方法）

        触发时机：
        - 输入引脚的数据发生变化时
        - 前置节点执行完毕后
        - 手动调用 self.setDirty() 后

        作用：
        - 读取输入引脚的数据
        - 执行计算/处理逻辑
        - 将结果写入输出引脚

        参数：
            *args: 可变位置参数（通常不使用）
            **kwargs: 可变关键字参数（通常不使用）

        数据流：
        1. 通过 pin.getData() 获取输入数据
        2. 执行计算
        3. 通过 pin.setData(value) 设置输出数据
        4. 输出数据会自动传播到连接的下游节点

        效果：
        - 读取 inp 引脚的布尔值
        - 对其取反（not 操作）
        - 将结果设置到 out 引脚
        - 下游节点的 compute() 会被自动触发

        错误处理：
        - 应该捕获异常并妥善处理
        - 可以打印错误信息到控制台
        - 避免抛出未捕获的异常（会导致图执行中断）

        示例（带错误处理）：
            try:
                inputData = self.inp.getData()
                if not isinstance(inputData, bool):
                    print(f"Warning: Expected bool, got {type(inputData)}")
                    inputData = bool(inputData)
                self.out.setData(not inputData)
            except Exception as e:
                print(f"Error in DemoNode.compute: {e}")
        """
        # 获取输入引脚的数据
        inputData = self.inp.getData()

        # 执行计算：布尔取反
        # 将结果设置到输出引脚
        self.out.setData(not inputData)
