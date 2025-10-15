# DemoPackage - uflow 包开发模板

DemoPackage 是 uflow 框架提供的完整包开发模板，展示了如何创建一个功能完整的 uflow 插件包。本模板包含了所有可能的组件类型，是学习 uflow 包开发的最佳起点。

## 目录结构

```
DemoPackage/
├── __init__.py                          # 包入口：继承 PackageBase，自动注册所有组件
├── Nodes/                               # 类节点目录：复杂、有状态的节点
│   ├── __init__.py
│   └── DemoNode.py                      # 示例类节点：布尔取反节点
├── Pins/                                # 自定义引脚（数据类型）目录
│   ├── __init__.py
│   └── DemoPin.py                       # 示例引脚：自定义数据类型
├── FunctionLibraries/                   # 函数库目录：简单的纯函数节点
│   ├── __init__.py
│   └── DemoLib.py                       # 示例函数库：包含一个打印问候的节点
├── UI/                                  # 自定义 UI 组件目录
│   ├── UIDemoNode.py                    # 节点的自定义 UI（如需自定义外观/交互）
│   └── UIDemoPin.py                     # 引脚的自定义 UI（如需自定义渲染）
├── Factories/                           # 工厂目录：负责创建 UI 组件
│   ├── __init__.py
│   ├── UINodeFactory.py                 # 节点 UI 工厂：将节点类映射到 UI 类
│   ├── UIPinFactory.py                  # 引脚 UI 工厂：将引脚类映射到 UI 类
│   └── PinInputWidgetFactory.py         # 引脚输入控件工厂：为引脚创建编辑器控件
├── Tools/                               # 工具目录：用户交互工具
│   ├── __init__.py
│   ├── DemoShelfTool.py                 # 工具栏按钮：快速操作按钮
│   └── DemoDockTool.py                  # 停靠面板：可停靠的工具窗口
├── Exporters/                           # 导入导出器目录
│   ├── __init__.py
│   └── DemoExporter.py                  # 示例导出器：自定义文件格式支持
├── PrefsWidgets/                        # 首选项面板目录
│   └── DemoPrefs.py                     # 示例首选项：包的设置界面
└── README.md                            # 本文件
```

## 组件说明

### 1. 包入口 (__init__.py)

__作用__: 定义包的基本信息，自动扫描并注册所有组件。

__关键点__:

- 包类名必须与目录名匹配（`DemoPackage`）
- 调用 `self.analyzePackage()` 自动发现并注册所有组件
- 框架会自动加载所有正确命名的子目录

__效果__:

- 包被 uflow 识别并加载
- 所有节点、引脚、工具等自动可用

### 2. 类节点 (Nodes/DemoNode.py)

__作用__: 实现复杂的、有状态的节点逻辑。

__适用场景__:

- 需要维护内部状态
- 需要动态创建/删除引脚
- 需要自定义 UI
- 需要执行流控制（ExecPin）
- 复杂的计算逻辑

__关键方法__:

- `__init__`: 初始化节点，创建引脚
- `compute()`: 执行节点计算
- `category()`: 节点分类（用于节点浏览器）
- `keywords()`: 搜索关键词
- `pinTypeHints()`: 引脚类型提示（用于动态引脚创建）

__效果__:

- 节点出现在节点浏览器的 "Generated from wizard" 分类下
- 可以在画布上创建和使用
- 接收布尔输入，输出其取反值

### 3. 自定义引脚 (Pins/DemoPin.py)

__作用__: 定义新的数据类型，用于节点之间传递自定义数据。

__包含两部分__:

1. __数据类__ (`FakeTypeATWXP`): 实际存储的数据结构
2. __引脚类__ (`DemoPin`): 引脚的行为定义

__关键静态方法__:

- `supportedDataTypes()`: 返回引脚类型名称
- `color()`: 引脚在 UI 中的颜色（RGBA）
- `internalDataStructure()`: 返回内部数据类型
- `processData()`: 数据处理/转换

__效果__:

- 新数据类型可在所有节点中使用
- 引脚在画布上显示为黄色（200, 200, 50）
- 可以连接相同类型的引脚

### 4. 函数库 (FunctionLibraries/DemoLib.py)

__作用__: 快速创建简单的纯函数节点，无需完整的类定义。

__适用场景__:

- 简单的数据转换
- 数学运算
- I/O 操作
- 无状态的纯函数

__关键装饰器__: `@IMPLEMENT_NODE`

- `returns`: 返回值类型（None 表示使用 REF 参数返回）
- `nodeType`: 节点类型（`NodeTypes.Callable` 表示有执行引脚）
- `meta`: 元数据（分类、关键词等）

__参数定义__:

- 输入参数: `param=('PinType', default_value)`
- 输出参数: `output=(REF, ('PinType', default_value))`

__效果__:

- 创建名为 "demoLibGreet" 的节点
- 节点出现在 "DemoLib" 分类下
- 有执行引脚（因为 `nodeType=NodeTypes.Callable`）
- 执行时打印输入的字符串

### 5. UI 组件

#### 5.1 UIDemoNode (UI/UIDemoNode.py)

__作用__: 为节点提供自定义的 UI 外观和交互。

__适用场景__:

- 自定义节点外观（颜色、形状）
- 添加自定义控件（按钮、滑块等）
- 特殊的交互行为
- 自定义绘制逻辑

__效果__:

- 目前使用默认 UI（未自定义）
- 可以添加自定义绘制、事件处理等

#### 5.2 UIDemoPin (UI/UIDemoPin.py)

__作用__: 为引脚提供自定义的 UI 渲染。

__适用场景__:

- 自定义引脚形状
- 特殊的连接行为
- 自定义绘制

__效果__:

- 目前使用默认 UI
- 可以自定义引脚的视觉表现

### 6. 工厂 (Factories/)

#### 6.1 UINodeFactory (Factories/UINodeFactory.py)

__作用__: 将节点类映射到对应的 UI 类。

__工作流程__:

1. uflow 创建节点时调用此工厂
2. 检查节点类名
3. 返回对应的 UI 类实例

__效果__:

- DemoNode 使用 UIDemoNode 作为 UI
- 其他节点使用默认 UI

#### 6.2 UIPinFactory (Factories/UIPinFactory.py)

__作用__: 将引脚类映射到对应的 UI 类。

__效果__:

- DemoPin 使用 UIDemoPin 作为 UI
- 其他引脚使用默认 UI

#### 6.3 PinInputWidgetFactory (Factories/PinInputWidgetFactory.py)

__作用__: 为引脚创建输入编辑器控件（当引脚未连接时显示）。

__包含__:

1. __控件类__ (`DemoInputWidget`): 实际的 Qt 控件
2. __工厂函数__ (`getInputWidget`): 根据引脚类型创建控件

__效果__:

- DemoPin 使用复选框作为输入控件
- 可以在未连接时直接设置引脚值

### 7. 工具 (Tools/)

#### 7.1 ShelfTool (Tools/DemoShelfTool.py)

__作用__: 在工具栏添加快速操作按钮。

__关键方法__:

- `name()`: 工具名称（唯一标识）
- `toolTip()`: 鼠标悬停提示
- `getIcon()`: 工具图标
- `do()`: 点击时执行的操作

__效果__:

- 工具栏出现一个砖块图标按钮
- 点击时在控制台打印 "Greet!"

#### 7.2 DockTool (Tools/DemoDockTool.py)

__作用__: 创建可停靠的工具面板。

__关键方法__:

- `name()`: 工具名称
- `toolTip()`: 提示文本
- `getIcon()`: 工具图标
- `isSingleton()`: 是否单例（通常为 True）

__效果__:

- 可以从菜单打开的停靠面板
- 可以停靠在主窗口的任意位置
- 目前是空白面板，可以添加任意 Qt 控件

### 8. 导出器 (Exporters/DemoExporter.py)

__作用__: 提供自定义的文件格式导入/导出功能。

__关键方法__:

- `displayName()`: 在菜单中显示的名称
- `toolTip()`: 提示文本
- `version()`: 导出器版本
- `doExport()`: 导出逻辑
- `doImport()`: 导入逻辑
- `createImporterMenu()`: 是否在导入菜单显示

__效果__:

- 在文件菜单的导入/导出子菜单中出现 "Demo exporter"
- 选择时打印消息（实际应实现文件读写）

### 9. 首选项面板 (PrefsWidgets/DemoPrefs.py)

__作用__: 为包提供设置界面，保存用户首选项。

__关键方法__:

- `__init__`: 创建 UI 控件
- `initDefaults()`: 初始化默认值
- `serialize()`: 保存设置
- `onShow()`: 显示时加载设置

__效果__:

- 在首选项对话框中出现 "Demo section" 折叠面板
- 包含一个可编辑的文本框 "Example property"
- 设置自动保存和加载

## 开发新包的步骤

### 1. 复制模板

```bash
cd uflow/Packages/
cp -r DemoPackage MyNewPackage
```

### 2. 重命名包类

编辑 `MyNewPackage/__init__.py`:

```python
class MyNewPackage(PackageBase):  # 类名必须与目录名相同
    def __init__(self):
        super(MyNewPackage, self).__init__()
        self.analyzePackage(os.path.dirname(__file__))
```

### 3. 根据需要保留组件

删除不需要的目录：

- 不需要自定义数据类型？删除 `Pins/`
- 只需要函数节点？删除 `Nodes/`
- 不需要工具？删除 `Tools/`
- 不需要设置？删除 `PrefsWidgets/`

### 4. 实现你的节点/功能

根据实际需求修改保留的组件。

### 5. 测试

```bash
# 运行 uflow
uv run python uflow.py

# 在节点浏览器中查找你的节点
# 测试功能是否正常
```

## 节点类型选择指南

### 使用类节点 (Nodes/) 当你需要

- 维护内部状态
- 动态创建引脚
- 自定义 UI
- 执行流控制
- 复杂生命周期管理

__示例__: ViewerNode, DataViewerNode, LoopNode

### 使用函数节点 (FunctionLibraries/) 当你需要

- 简单的数据转换
- 纯函数计算
- 数学运算
- 简单 I/O
- 无状态操作

__示例__: ReadCSV, WriteCSV, Add, Multiply

## 引脚系统说明

### 引脚颜色约定

- 执行流: 白色
- 布尔: 红色
- 整数: 绿色
- 浮点: 青色
- 字符串: 粉色
- 自定义类型: 自定义颜色（如 DemoPin 的黄色）

### 引脚结构类型

- `StructureType.Single`: 单个值
- `StructureType.Array`: 数组/列表
- `StructureType.Multi`: 多值（可以接受任意数量的连接）

## 常见问题

### Q: 为什么我的节点不显示？

A: 检查：

1. 包类名是否与目录名匹配
2. 是否调用了 `analyzePackage()`
3. 节点类是否继承了 `NodeBase` 或使用了 `@IMPLEMENT_NODE`
4. 所有 `__init__.py` 是否存在

### Q: 如何添加执行引脚？

A: 在类节点中：

```python
self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, PinOptions.AllowAny)
self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')
```

### Q: 自定义数据类型如何序列化？

A: 对于复杂对象（DataFrame, OpenCV 图像等）：

```python
# 在引脚类中
@staticmethod
def jsonEncoderClass():
    return NoneEncoder

@staticmethod
def jsonDecoderClass():
    return NoneDecoder

# 并在 __init__ 中移除 Storable 选项
self.disableOptions(PinOptions.Storable)
```

### Q: 如何访问 uflow 实例？

A: 在工具中：

```python
uflowInstance = self._wrapper.canvasRef().uflowInstance
```

在节点中：

```python
uflowInstance = self.getGraph().graphManager.get()
```

## 参考资源

- __uflow 核心__: `uflow/Core/`
- __其他包示例__:
  - `uflowBase`: 基础节点（数学、逻辑、变量）
  - `uflowDataAnalysis`: DataFrame 处理示例
  - `uflowOpenCv`: 图像处理示例
- __开发指南__: `notes/` 目录（中文详细指南）
- __测试示例__: `uflow/Tests/`

## 总结

DemoPackage 展示了 uflow 包的完整结构。实际开发时：

1. 根据需求选择合适的组件类型
2. 删除不需要的部分以保持简洁
3. 参考其他包的实现方式
4. 充分测试功能

祝开发顺利！
