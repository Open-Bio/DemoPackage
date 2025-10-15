"""
DemoPrefs - 首选项面板示例

首选项面板（PrefsWidget）为包提供设置界面，允许用户配置包的行为和选项。
设置会自动保存到 QSettings，并在 uflow 启动时加载。

首选项面板的作用：
- 为用户提供配置界面
- 保存和加载用户设置
- 提供包级别的全局选项
- 自定义包的行为

典型用途：
- 默认值配置（节点的默认参数）
- 路径设置（资源目录、输出目录等）
- 行为选项（自动保存、性能优化等）
- 外观设置（颜色主题、字体等）
- API 密钥和认证信息

继承：CategoryWidgetBase
"""

from qtpy.QtWidgets import *

from uflow.UI.Widgets.PropertiesFramework import CollapsibleFormWidget
from uflow.UI.Widgets.PreferencesWindow import CategoryWidgetBase


class DemoPrefs(CategoryWidgetBase):
    """
    演示首选项面板

    为 DemoPackage 提供设置界面示例。
    展示如何创建可折叠的设置区域和保存/加载设置。

    继承层次：
    QWidget <- CategoryWidgetBase <- DemoPrefs

    关键方法：
    - __init__: 构建 UI 界面
    - initDefaults: 初始化默认值
    - serialize: 保存设置
    - onShow: 显示时加载设置

    设置存储：
    - 使用 QSettings 自动保存
    - 设置路径：包名/设置键
    - 持久化存储，跨会话保持
    """

    def __init__(self, parent=None):
        """
        初始化首选项面板

        参数：
            parent: 父控件

        作用：
        - 创建设置界面的 UI 布局
        - 添加设置控件（文本框、复选框、滑块等）
        - 组织设置为可折叠的区域

        UI 组件：
        - CollapsibleFormWidget: 可折叠的设置区域
        - QLineEdit, QCheckBox 等：具体的设置控件
        - QSpacerItem: 占位符，保持布局美观

        效果：
        - 创建一个包含 "Demo section" 的设置面板
        - 包含一个 "Example property" 文本框
        """
        super(DemoPrefs, self).__init__(parent)

        # 创建垂直布局
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(1, 1, 1, 1)  # 设置边距
        self.layout.setSpacing(2)  # 设置控件间距

        # 创建可折叠的设置区域
        # headName 参数指定区域的标题
        demoSection = CollapsibleFormWidget(headName="Demo section")

        # 创建示例属性控件（文本框）
        self.exampleProperty = QLineEdit("Property value")

        # 将控件添加到设置区域
        # 第一个参数是标签文本，第二个参数是控件
        demoSection.addWidget("Example property", self.exampleProperty)

        # 将设置区域添加到主布局
        self.layout.addWidget(demoSection)

        # 添加弹性空间，使设置区域靠上对齐
        spacerItem = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacerItem)

        # ====================================================================
        # 可以添加更多设置区域和控件（示例）
        # ====================================================================

        # 示例：添加更多设置
        # anotherSection = CollapsibleFormWidget(headName="Advanced Settings")
        #
        # # 添加复选框
        # self.enableFeature = QCheckBox()
        # self.enableFeature.setChecked(True)
        # anotherSection.addWidget("Enable Feature", self.enableFeature)
        #
        # # 添加数字输入
        # self.maxValue = QSpinBox()
        # self.maxValue.setRange(0, 100)
        # self.maxValue.setValue(50)
        # anotherSection.addWidget("Max Value", self.maxValue)
        #
        # # 添加下拉框
        # self.colorScheme = QComboBox()
        # self.colorScheme.addItems(['Light', 'Dark', 'Auto'])
        # anotherSection.addWidget("Color Scheme", self.colorScheme)
        #
        # self.layout.addWidget(anotherSection)

    def initDefaults(self, settings):
        """
        初始化默认设置值

        参数：
            settings (QSettings): 设置对象

        作用：
        - 在首次运行时设置默认值
        - 确保所有设置都有初始值
        - 仅在设置不存在时调用

        调用时机：
        - uflow 首次启动时
        - 设置文件被删除或损坏时

        注意：
        - 设置键应该清晰描述用途
        - 使用统一的命名规范
        - 考虑向后兼容性

        效果：
        - 设置 "ExampleProperty" 的默认值为 "property value"
        """
        settings.setValue("ExampleProperty", "property value")

        # 示例：设置更多默认值
        # settings.setValue("EnableFeature", True)
        # settings.setValue("MaxValue", 50)
        # settings.setValue("ColorScheme", "Light")

    def serialize(self, settings):
        """
        序列化（保存）设置

        参数：
            settings (QSettings): 设置对象

        作用：
        - 将 UI 控件的当前值保存到设置
        - 用户点击 "应用" 或 "确定" 时调用
        - 持久化用户的配置

        调用时机：
        - 用户点击首选项对话框的 "应用" 按钮
        - 用户点击 "确定" 按钮关闭对话框
        - uflow 关闭时（如果设置了自动保存）

        注意：
        - 设置键必须与 initDefaults 中的一致
        - 保存正确的数据类型
        - 考虑数据验证

        效果：
        - 将 exampleProperty 文本框的值保存到 "ExampleProperty" 设置
        """
        settings.setValue("ExampleProperty", self.exampleProperty.text())

        # 示例：保存更多设置
        # settings.setValue("EnableFeature", self.enableFeature.isChecked())
        # settings.setValue("MaxValue", self.maxValue.value())
        # settings.setValue("ColorScheme", self.colorScheme.currentText())

    def onShow(self, settings):
        """
        显示面板时调用（加载设置）

        参数：
            settings (QSettings): 设置对象

        作用：
        - 从设置加载值到 UI 控件
        - 每次打开首选项对话框时调用
        - 显示当前保存的设置

        调用时机：
        - 用户打开首选项对话框时
        - 切换到此设置类别时

        注意：
        - 使用 settings.value() 读取设置
        - 提供默认值以防设置不存在
        - 更新所有 UI 控件的状态

        效果：
        - 将保存的 "ExampleProperty" 值加载到文本框
        """
        # 读取设置并更新 UI 控件
        # settings.value() 返回保存的值，如果不存在则返回 None
        self.exampleProperty.setText(settings.value("ExampleProperty"))

        # 示例：加载更多设置
        # enableFeature = settings.value("EnableFeature", True, type=bool)
        # self.enableFeature.setChecked(enableFeature)
        #
        # maxValue = settings.value("MaxValue", 50, type=int)
        # self.maxValue.setValue(maxValue)
        #
        # colorScheme = settings.value("ColorScheme", "Light")
        # index = self.colorScheme.findText(colorScheme)
        # if index >= 0:
        #     self.colorScheme.setCurrentIndex(index)

    # 可选方法示例
    # def onApply(self):
    #     """
    #     应用设置（可选）
    #
    #     作用：
    #     - 在保存设置后执行额外操作
    #     - 触发设置变更的副作用
    #     - 刷新依赖设置的组件
    #
    #     示例：
    #     - 重新加载资源
    #     - 更新 UI 主题
    #     - 重启服务
    #     """
    #     print("Settings applied!")
    #     # 执行应用设置后的操作
    #     # 例如：通知其他组件设置已更改
