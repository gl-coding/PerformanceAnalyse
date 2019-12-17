centos

两台机器,一个作为qperf的服务器端，通过访问服务端判断网络延时及带宽 (服务器ip地址是192.168.11.1)
服务器端:
    [root@localhost ~]# qperf
客户端:
    [root@localhost ~]# qperf -t 60 --use_bits_per_sec 192.168.11.1 tcp_bw tcp_lat
    tcp_bw:
     bw = 1.58 Gb/sec--------->>>这就是网络带宽
    tcp_lat:
     latency = 186 us--------->>>这就是网络延迟
    [root@localhost ~]#

    网络性能测试工具qperf使用
作者: yanyun 时间: July 23, 2017 分类: Performance Benchmark
前言

网络在性能方面的角色越来越重要，特别在现在云计算环境中，系统越来越分布化。任何一个网络性能问题，都有可能导致业务响应迟缓。
我们在知道网卡、交换机型号，以及物理距离后，理论上是可以知道带宽和延迟的。但是实际环境中由于使用不同的网卡驱动，交换机跳数，网络配置导致会有不同的性能表现。那么就需要进行测试验证，我们通常使用的网络性能测试工具有netperf/iperf，这次介绍的是qperf工具，相对netperf和iperf来说是个新工具, 而且合入到了红帽系统中

qperf介绍

网络性能主要有两个指标是带宽和延时。延迟决定最大的QPS(Query Per Second)，而带宽决定了可支撑的最大负荷。
qperf和iperf/netperf一样可以评测两个节点之间的带宽和延时。可以在测试tcp/ip协议和RDMA传输。不过相比netperf和iperf，支持RDMA是qperf工具的独有特性。
接下去开始动手使用qperf。

qperf安装

可以直接通过yum源安装。#yun install qperf
同时会安装两个依赖包(libibverbs, librdmacm),是直接和rdma功能相关的，不然无法启动rdma功能。也可以通过，https://pkgs.org/download/qperf 官方网页下载安装。

使用

qperf是测试两个节点之间的带宽和延时的，为此需要一个当作服务端，一个当作客户端。其中服务端直接运行qperf, 无需任何参数。

服务端节点

直接运行如下，无需任何参数
#qperf
默认开启端口号：19765
通过netstat查看，如下:
#netstat –tunlup
tcp 0 0 0.0.0.0:19765 0.0.0.0:* LISTEN 53755/qperf

客户端

客户端运行获取带宽、延时情况，运行过程中不需要指定端口号，只要指定主机名或者ip地址即可。文章中后续命令都是在客户端中进行执行。

TCP带宽测试

最简单的格式是客户端使用两个参数：一个是服务端的名字，另一个是本次测试的命名（例如tcp_bw TCP带宽测试）。
#qperf 11.165.67.18 tcp_bw
这个是输出tcp带宽。

TCP延时测试

测试tcp延时，如下：
#qperf 11.165.67.18 tcp_lat
结果输出如下：
tcp_bw:
bw = 1.17 GB/sec
tcp_lat:
latency = 61.3 us
可以同时测试tcp带宽和tcp延时，如下：
#qperf 11.165.67.18 tcp_bw tcp_lat
tcp_bw:
bw = 1.17 GB/sec
tcp_lat:
latency = 61.3 us
UDP协议测试同TCP协议测试类似，只需命令参数中将tcp_bw和tcp_lat改成udp_bw和udp_lat即可。

指定测试时间

有些场景下我们需要进行带负载的长时间稳定性测试，可以通过指定测试运行时间（使用-t参数）来实现。例如测试10秒tcp带宽,可以使用-t参数，如下：
#qperf 11.165.67.18 -t 10 tcp_bw

循环loop遍历测试

在做网卡性能摸底测试的时候，很多时候需要得到网卡的带宽和延时性能曲线。通过qperf提供的循环loop测试，可以一个命令得到所有数据。循环多次测试，每次改变消息大小，例如从16K增加到64K，每次大小翻倍直到64K。
#qperf 11.165.67.18 -oo msg_size:1:64K:*2 -vu tcp_bw tcp_lat
tcp_bw:
bw = 3.06 MB/sec
msg_size = 1 bytes
tcp_bw:
bw = 6.15 MB/sec
msg_size = 2 bytes
tcp_bw:
bw = 12 MB/sec
msg_size = 4 bytes
tcp_bw:
bw = 24 MB/sec
msg_size = 8 bytes
tcp_bw:
bw = 48.6 MB/sec
msg_size = 16 bytes
tcp_bw:
bw = 93.5 MB/sec
msg_size = 32 bytes
tcp_bw:
bw = 176 MB/sec
msg_size = 64 bytes
tcp_bw:
bw = 343 MB/sec
msg_size = 128 bytes
tcp_bw:
bw = 612 MB/sec
msg_size = 256 bytes
tcp_bw:
bw = 904 MB/sec
msg_size = 512 bytes
tcp_bw:
bw = 1.18 GB/sec
msg_size = 1 KiB (1,024)
tcp_bw:
bw = 1.17 GB/sec
msg_size = 2 KiB (2,048)
tcp_bw:
bw = 1.15 GB/sec
msg_size = 4 KiB (4,096)
tcp_bw:
bw = 1.17 GB/sec
msg_size = 8 KiB (8,192)
tcp_bw:
bw = 1.17 GB/sec
msg_size = 16 KiB (16,384)
tcp_bw:
bw = 1.17 GB/sec
msg_size = 32 KiB (32,768)
tcp_bw:
bw = 1.17 GB/sec
msg_size = 64 KiB (65,536)
tcp_lat:
latency = 61.5 us
msg_size = 1 bytes
tcp_lat:
latency = 61.8 us
msg_size = 2 bytes
tcp_lat:
latency = 61.9 us
msg_size = 4 bytes
tcp_lat:
latency = 29.8 us
msg_size = 8 bytes
tcp_lat:
latency = 61.5 us
msg_size = 16 bytes
tcp_lat:
latency = 62.2 us
msg_size = 32 bytes
tcp_lat:
latency = 61.6 us
msg_size = 64 bytes
tcp_lat:
latency = 61.5 us
msg_size = 128 bytes
tcp_lat:
latency = 61.9 us
msg_size = 256 bytes
tcp_lat:
latency = 61.9 us
msg_size = 512 bytes
tcp_lat:
latency = 61.7 us
msg_size = 1 KiB (1,024)
tcp_lat:
latency = 62.7 us
msg_size = 2 KiB (2,048)
tcp_lat:
latency = 62.6 us
msg_size = 4 KiB (4,096)
tcp_lat:
latency = 70.4 us
msg_size = 8 KiB (8,192)
tcp_lat:
latency = 141 us
msg_size = 16 KiB (16,384)
tcp_lat:
latency = 152 us
msg_size = 32 KiB (32,768)
tcp_lat:
latency = 186 us
msg_size = 64 KiB (65,536)
可以最后将测试数据图形化。得到msg_size从1到64K变化的过程中，带宽,延时增长趋势和临界点。这个临界点对于服务器性能评估是很有帮助的。

RDMA测试

如果网卡支持RDMA功能，例如IB卡，那么可以进行RDMA性能测试：
#qperf  11.165.67.18 ud_bw
qperf使用小结
qperf工具使用本身和netperf／iperf非常类似，但是除了支持tcp/udp/sctp外， qperf值得提的亮点是：第一可以支持RDMA测量，第二可进行循环遍历测试。这两点也是推荐该工具的主要原因。
