# reStructuredText (RST) 格式指南

## 问题说明

在 uflow 中，当鼠标悬停在节点上时，如果节点的描述文本（docstring）包含格式错误的 reStructuredText (rst)，会在终端显示如下错误：

```
<string>:17: (ERROR/3) Unexpected indentation.
```

这是因为 uflow 使用 rst 解析器来渲染节点描述，格式错误会导致解析失败。

## 受影响的位置

1. **类节点的 `description()` 方法返回值**（Nodes/）

   ```python
   @staticmethod
   def description():
       return "Your description in rst format"  # 这里必须是有效的 rst
   ```

2. **函数节点的 docstring**（FunctionLibraries/）

   ```python
   @IMPLEMENT_NODE(...)
   def myFunction(param=('StringPin', '')):
       """This docstring is used as node description."""  # 必须是有效的 rst
       pass
   ```

## 常见错误

### ❌ 错误示例 1：缩进不一致

```python
def description():
    return """
    参数定义格式：
    - param: 说明
      - 嵌套项：缩进不对
    """
```

### ❌ 错误示例 2：列表后没有空行

```python
def description():
    return """
    说明文本：
    - 列表项 1
    - 列表项 2
    继续说明  # 错误：列表后应该有空行
    """
```

### ❌ 错误示例 3：代码块缩进问题

```python
def description():
    return """
    示例：
        code line 1
       code line 2  # 错误：缩进不一致
    """
```

## 正确的 RST 格式

### ✅ 正确示例 1：简单描述

```python
@staticmethod
def description():
    return "Simple one-line description."
```

### ✅ 正确示例 2：带列表的描述

```python
@staticmethod
def description():
    return """Node description here.

    **Parameters:**

    - param1: Description of parameter 1
    - param2: Description of parameter 2

    **Usage:**

    Connect this node to other nodes to process data.
    """
```

### ✅ 正确示例 3：使用 rst 指令

```python
def myFunction(x=('IntPin', 0)):
    """Calculate result.

    This function performs calculation on the input value.

    **Parameters:**

    - x: Input number

    .. note::
       This is a note block using rst directive.

    .. warning::
       Keep formatting simple to avoid errors.
    """
    return x * 2
```

### ✅ 正确示例 4：带代码块

```python
@staticmethod
def description():
    return """Execute Python code.

    **Example:**

    ::

        # Python code example
        x = 10
        print(x)

    Note: Code blocks must be preceded by :: and properly indented.
    """
```

## RST 格式规则总结

1. **段落之间留空行**：不同段落必须用空行分隔
2. **列表格式**：
   - 使用 `-` 或 `*` 开头
   - 列表项保持相同缩进
   - 列表前后要有空行
3. **代码块**：
   - 使用 `::` 引导代码块
   - 代码块需要额外缩进（通常 4 个空格）
4. **加粗/斜体**：
   - 加粗：`**text**`
   - 斜体：`*text*`
   - 代码：`` `text` ``
5. **RST 指令**：
   - 注意：`.. note::`
   - 警告：`.. warning::`
   - 代码：`.. code-block:: python`

## 开发建议

1. **保持简洁**：描述文本尽量简单明了，避免复杂的格式
2. **使用标准结构**：参考上面的正确示例
3. **测试描述**：鼠标悬停到节点上检查是否有错误
4. **在线验证**：可以使用在线 rst 验证工具检查格式
5. **查看示例**：参考 FlowBasePackage 包中的节点描述

## 修复步骤

如果遇到 "Unexpected indentation" 错误：

1. 找到报错的节点（通过鼠标悬停测试）
2. 检查该节点的 `description()` 返回值或函数 docstring
3. 简化格式，移除复杂的缩进结构
4. 确保列表、段落格式正确
5. 重新运行 uflow 测试

## 参考资源

- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [RST Quick Reference](https://docutils.sourceforge.io/docs/user/rst/quickref.html)
- FlowBasePackage 包中的节点描述示例
