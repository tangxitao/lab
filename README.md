# 分布式学习系统故障定位

每隔15s采集一次数据，在181,183,185上面

数据指标
cpu利用率cpu usage
gpu利用率gpu usage
gpu功率gpu power
gpu温度gpu temp
磁盘读写速率sda

normal文件夹存放着无故障时的训练数据，训练历时1m 44s

cpufullload是往185节点注入1分钟左右的cpu满载故障，训练历时2m 3s

