# 分布式学习系统故障定位

每隔15s采集一次数据，在181,183,185上面

### 数据指标
1. cpu利用率cpu usage
2. gpu利用率gpu usage
3. gpu功率gpu power
4. gpu温度gpu temp
5. 磁盘读写速率sda


### 文件夹存放 
normal文件夹存放着无故障时的训练数据，训练历时1m 44s

cpufullload是往185节点注入75s的cpu满载故障，训练历时2m 3s

gpu_burn是对185节点进行1分钟的GPU_burn，训练历时2m 14s。


diskburn文件夹对185进行磁盘高负载故障90s，训练历时1m 46s，可视为无影响。

netloss文件夹对185进行50%的丢包处理，训练历时1m42s，可视为无影响（在终端输出的信息中，一个节点丢包网络不好，ray会把任务分给网络好的节点，总时长基本不变）