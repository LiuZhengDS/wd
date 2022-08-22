
# wd
Django dashboard
>96c92e8832c1dc534f5b70f139bd03eef4557407

Currently used as TODO list & development log for WD dashboard project.

# 0.1 前后台打通，可以成功显示文字，基础框架布局，总结ML函数
### 0.1.1 搭建基础框架，hello Django!
### 0.1.2 Machine Learning package collection

# 0.2 数据处理
### 0.2.1 前后台打通，读取数据(csv)
- 以dataframe格式进行处理
### 0.2.2 其他部门常用数据格式(例:sas)转csv函数
- sas2csv, csv2sas, ...
### 0.2.3 基础数据(预)处理函数
- ref Mia's summary of DataProcessing.md list
### (0.2.4) Brainstorm for *other possible* data pre-process/cleaning functions
- DA teammates, Baosu, Haibo等同事提意见和建议

# 0.3 数据可视化 （在正确的位置出现，数据显示正确）
### 0.3.1 Django 前端位置预留设计，打印空图
### 0.3.2 读取、处理csv文件并将结果展示
### 0.3.3 figure type summary
- scatter
- plot
- bar
- pie
- ...

# 0.4 接口（数据选择，预处理，ML，可视化）

## 二维数据
### 分析维度 n选2 (二维绘图)
### 辅助维度 交互 (例: 鼠标悬停时展示的信息)
### 2个维度都为数值型数据 散点图
### 1个维度为时间 1个维度为数值型 折线图 柱状图
该情况涉及基于时间的统计，后端生成新的数据表后append(适合大数据集)，或者即时计算(适合小数据集)
### 0.4.1 勾选框
### 0.4.2 滑动框
### 0.4.3 


# 0.5 测试 demo inside DA

### 0.5.1 后端输入输出检查
- 路径与数据处理接口(输入:识别路径, 输出:处理过的数据)
- 数据处理与机器学习函数的接口(输入:处理过的数据, 输出:计算过的数据)
- 数据与可视化的接口(输入:处理/计算过的数据, 输出:~)

### 0.5.2 toy数据集测试

### 0.5.3 大数据集测试 & 统计运行时间与硬件型号(CPU)

- x0: 硬件型号
- x1: 数据集大小
- x2: 数据处理类别
- y: 运行时间

## 0.5.4 demo

# 0.6 封装sklearn（将来处理其他代码）
### 0.6.1 基于0.1.2收集package, from _ import _ 
### 0.6.2 封装(预留接口)

# 0.7 用户权限（IT同事一起管理？），使用白皮书
# 0.8 丰富ML算法，完善用户界面（设计，美观？）
# 0.9 动画效果，鼠标悬浮数据展示
# 1.0 神经网络DIY








## 数据改动的自动化，选项？

## 时间敏感度