sysbench
sysbench是一款开源的多线程性能测试工具，可以执行CPU/内存/线程/IO/数据库等方面的性能测试。

sysbench支持以下几种测试模式：
1、CPU运算性能
2、磁盘IO性能
3、调度程序性能
4、内存分配及传输速度
5、POSIX线程性能
6、数据库性能(OLTP基准测试)

install

macOs
brew install sysbench

1、CPU测试
对CPU的性能测试通常有：1.质数计算；2圆周率计算；sysbench使用的就是通过质数相加的测试。对CPU测试直接运行run即可

sysbench --threads=20 --events=10000 --debug=on --test=cpu --cpu-max-prime=20000 run
20个线程执行1万条请求，每个请求执行质数相加到20000


2、内存测试
测试8K顺序分配：
sysbench --threads=12 --events=10000 --test=memory --memory-block-size=8K --memory-total-size=100G --memory-access-mode=seq run
测试8K随机分配。
sysbench --threads=12 --events=10000 --test=memory --memory-block-size=8K --memory-total-size=100G --memory-access-mode=rnd run



3、文件io测试
IO的测试主要用于测试IO的负载性能。主要测试选项为--file-test-mode。还有可以关注的参数包括--file-block-size、--file-io-mode、--file-fsync-freq 、--file-rw-ratio，具体参数含义请见参数解释章节。
sysbench --threads=12 --events=10000 fileio --file-total-size=3G --file-test-mode=rndrw prepare
sysbench --threads=12 --events=10000 fileio --file-total-size=3G --file-test-mode=rndrw run
sysbench --threads=12 --events=10000 fileio --file-total-size=3G --file-test-mode=rndrw cleanup
对比两台服务器的io性能，需要跑相同的线程

4、锁测试
互斥锁测试模拟所有线程在同一时刻并发运行。
sysbench --threads=12 mutex --mutex-num=1024 --mutex-locks=10000 --mutex-loops=10000 run


5、线程测试
sysbench threads --num-threads=64 --thread-yields=100 --thread-locks=2 run

7、参数解释
通过命令sysbench –help可以了解各参数的具体解释
--test=tests/db/oltp.lua 表示调用 tests/db/oltp.lua 脚本进行 oltp 模式测试
--threads：客户端的并发连接数
--time：测试执行的时间，单位是秒，该值不要太短，可以选择120
--report-interval：生成报告的时间间隔，单位是秒，如10
--oltp_tables_count=10 表示会生成 10 个测试表
--oltp-table-size=100000 表示每个测试表填充数据量为 100000
--mysql-engine-trx=STRING指定不同的存储引擎测试。
--oltp-test-mode=STRING测试类型：simple(简单select测试),complex(事务测试),nontrx(非事务测试),sp(存储过程) ；默认complex
--oltp-sp-name=STRING指定存储过程进行语句测试
--oltp-table-size=N指定表的记录大小，默认[10000]
--oltp-num-tables=N指定测试表的数量，默认1
--rand-init=on 表示每个测试表都是用随机数据来填充的
--file-num=N创建测试文件的数量,默认128个
--file-block-size=N block size大小,默认16K
--file-total-size=SIZE所有文件的总大小，默认2G
--file-test-mode=STRING测试类型 {seqwr(顺序写), seqrewr(顺序读写), seqrd(顺序读), rndrd(随机读), rndwr(随机写), rndrw(随机读写)} --file-io-mode=STRING I/O模式,需要系统支持默认sync[sync(同步IO),async(异步IO),mmap()]
--file-async-backlog=N每个线程的异步操作队列数，默认128个，需要--file-io-mode=async;
--file-extra-flags=STRING additional flags to use on opening files {sync,dsync,direct} []
--file-fsync-freq=N当请求数达到多少时执行fsync()刷新,默认100,0代表过程中不执行fsync()
--file-fsync-all=[on|off] 执行每一个写操作后执行fsync()刷新操作,默认关闭off --file-fsync-end=[on|off] 测试结束执行fsync()操作,默认开启on --file-fsync-mode=STRING 同步刷新方法,默认fsync {fsync, fdatasync} --file-merged-requests=N合并指定数量的IO请求,0代表不合并,默认0 --file-rw-ratio=N 读写比例，默认1.5/1

8、建议、注意
建议：
1）、在开始测试之前，应该首先明确：应采用针对整个系统的基准测试，还是针对MySQL的基准测试，还是二者都需要。

2）、如果需要针对MySQL的基准测试，那么还需要明确精度方面的要求：是否需要使用生产环境的真实数据，还是使用工具生成也可以；前者实施起来更加繁琐。如果要使用真实数据，尽量使用全部数据，而不是部分数据。

3)、要进行多次才有意义。需要注意主从同步的状态。测试必须模拟多线程的情况，单线程情况不但无法模拟真实的效率，也无法模拟阻塞甚至死锁情况。

注意：
1）、尽量不要在MySQL服务器运行的机器上进行测试，一方面可能无法体现网络（哪怕是局域网）的影响，另一方面，sysbench的运行（尤其是设置的并发数较高时）会影响MySQL服务器的表现。

2）、可以逐步增加客户端的并发连接数（--thread参数），观察在连接数不同情况下，MySQL服务器的表现；如分别设置为10,20,50,100等。

3）、一般执行模式选择complex即可，如果需要特别测试服务器只读性能，或不使用事务时的性能，可以选择simple模式或nontrx模式。

4）、如果连续进行多次测试，注意确保之前测试的数据已经被清理干净。
