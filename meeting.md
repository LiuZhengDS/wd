# Sep. 15 mornitoring system


# 0. 使用之前
- 默认传入(读取)的数据已经清洗过了，没有缺失值等情况。

- 依据个人习惯使用SAS/JMP做数据清洗，或提供DataProcess.py的Python脚本可以一步到位执行数据预处理(需做培训学习)

- 当前版本展示

# 1. 界面
## - 界面逻辑
除部分预留接口外，界面前后顺序是否符合实际使用需求，是否有整、删、改的需求？

返回是一步一步返回还是回到数据选择 (第一步)？
## - 界面布局
各选择框，按钮位置布局是否符合使用习惯？

# 2. 画图

## 维度

- 画布平面内X,Y轴可使用2个feature (2维数据)

这种情况多适合画scatter(散点图)

- 若考虑双Y轴，则可以使用3个feature (3维数据)

这种情况X轴适合作为时间轴，(双)Y轴作为数值型变量的刻度尺

## 增加辅助信息

- 更多维度的数据是否会需要同时被画在同一张图里 (4维，5维，。。。)？

某些feature单位(量纲)相同的情况probably可以额外添加数据，“共享同一个Y轴”

- 辅助信息在导出图例时是否要同时导出？

关键数据也导出吗？如何定义关键数据？有了定义，可以把该定义的逻辑通过if判断加入代码

例如判断为outlier的数据点的信息会被导出，或者如图所示

## legend

- 画图的“分析维度”是提供数值型数据的
- “辅助维度”选择字符型数据（category）来作为legend

# 3. 运行时间

- 两种读取方案

a. 数据文件以python变量的形式全部load进内存里，每次根据前端选择调用所选python变量

b. 不提前load，每次前端选择后，load文件为python变量并调用

- tradeoff 

时间（等待时间，用户体验）vs 空间（硬件，钱 经费）



## 图片存在S3上 而不是box
## 哪些type 已经在用了 哪些还没有涉及

# Sep 28 Monitoring 会议

- monitor里面不修改数据类型（数据类型修改？都在预处理阶段完成），preprocess代码（自动化）
- 主维度1，主维度2，辅助维度 变更为 主维度（单选），辅助维度（多选），legend（多选）
- 要求主维度，辅助维度必须为numerical，legend为category
- 页面设计成一页多图，一主多辅
- fig1 volume和sigma能否通过添加箱图同时存在（pros）,但是legend多时，箱图会比较乱（cons）
- filter 画图类型选择这个功能去掉，添加legend和辅助维度选择
- export 图片 or 数据表格（预处理后的summary好了的）