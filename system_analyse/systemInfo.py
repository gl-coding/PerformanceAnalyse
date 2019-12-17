#encoding=utf8
import psutil

print psutil.cpu_times(percpu=False)

print psutil.cpu_times(percpu=True)

#与上次调用经过时间内的cpu的使用率
print psutil.cpu_percent()

#当前1s内cpu的使用率
print psutil.cpu_percent(interval=1)

## 4个逻辑cpu的使用率
print psutil.cpu_percent(interval=1 ,percpu=True)

#提供每个特定CPU时间的利用率百分比
print psutil.cpu_times_percent(interval=1)

#逻辑cpu个数
print psutil.cpu_count()

### 物理cpu个数
print psutil.cpu_count(logical=False)

### 当前可用cpu个数
#print len(psutil.Process().cpu_affinity())

#ctx_switches	    启动后的上下文切换次数
#interrupts	    自引导以来的中断数
#soft_interrupts    自引导以来的软件中断次数
#syscalls	    自引导以来的系统调用次数
print psutil.cpu_stats()

#total	总物理内存
#available	在没有系统进入SWAP下立即提供的内存。
#percent	使用内存占比
#used	使用的物理内存
#free	没有使用的物理内存
#active	当前正在使用或最近使用的物理内存
#inactive	标记未使用的内存
#buffers	buffers使用的缓存
#cached	ccached使用的缓存
#shared	显示被共享使用的物理内存大小
#slab	内核数据结构缓存
print psutil.virtual_memory()

print psutil.swap_memory()

import datetime,psutil
print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

#网络

#获取网卡的信息
print psutil.net_if_addrs()

#获取网络接口的状态
print psutil.net_if_stats()

#所有磁盘信息
print psutil.disk_partitions()

print psutil.disk_usage("/dev/disk1s1")

#获取网口的流量
print psutil.net_io_counters()

#获取当前用户
psutil.users()

#获取PID
print psutil.pids()

#获取进程信息
#for x in  psutil.process_iter():
#    print(x)

