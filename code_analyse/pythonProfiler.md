Python性能优化的20条建议
优化算法时间复杂度
算法的时间复杂度对程序的执行效率影响最大，在Python中可以通过选择合适的数据结构来优化时间复杂度，如list和set查找某一个元素的时间复杂度分别是O(n)和O(1)。不同的场景有不同的优化方式，总得来说，一般有分治，分支界限，贪心，动态规划等思想。

减少冗余数据
如用上三角或下三角的方式去保存一个大的对称矩阵。在0元素占大多数的矩阵里使用稀疏矩阵表示。

合理使用copy与deepcopy
对于dict和list等数据结构的对象，直接赋值使用的是引用的方式。而有些情况下需要复制整个对象，这时可以使用copy包里的copy和deepcopy，这两个函数的不同之处在于后者是递归复制的。效率也不一样：（以下程序在ipython中运行）

import copy
a = range(100000)
%timeit -n 10 copy.copy(a) # 运行10次 copy.copy(a)
%timeit -n 10 copy.deepcopy(a)
10 loops, best of 3: 1.55 ms per loop
10 loops, best of 3: 151 ms per loop
timeit后面的-n表示运行的次数，后两行对应的是两个timeit的输出，下同。由此可见后者慢一个数量级。

使用dict或set查找元素
python dict和set都是使用hash表来实现(类似c++11标准库中unordered_map)，查找元素的时间复杂度是O(1)

a = range(1000)
s = set(a)
d = dict((i,1) for i in a)
%timeit -n 10000 100 in d
%timeit -n 10000 100 in s
10000 loops, best of 3: 43.5 ns per loop
10000 loops, best of 3: 49.6 ns per loop
dict的效率略高(占用的空间也多一些)。

合理使用生成器（generator）和yield
%timeit -n 100 a = (i for i in range(100000))
%timeit -n 100 b = [i for i in range(100000)]
100 loops, best of 3: 1.54 ms per loop
100 loops, best of 3: 4.56 ms per loop
使用()得到的是一个generator对象，所需要的内存空间与列表的大小无关，所以效率会高一些。在具体应用上，比如set(i for i in range(100000))会比set([i for i in range(100000)])快。

但是对于需要循环遍历的情况：

%timeit -n 10 for x in (i for i in range(100000)): pass
%timeit -n 10 for x in [i for i in range(100000)]: pass
10 loops, best of 3: 6.51 ms per loop
10 loops, best of 3: 5.54 ms per loop
后者的效率反而更高，但是如果循环里有break,用generator的好处是显而易见的。yield也是用于创建generator：

def yield_func(ls):
    for i in ls:
        yield i+1
 
def not_yield_func(ls):
    return [i+1 for i in ls]
ls = range(1000000)
%timeit -n 10 for i in yield_func(ls):pass
%timeit -n 10 for i in not_yield_func(ls):pass
10 loops, best of 3: 63.8 ms per loop
10 loops, best of 3: 62.9 ms per loop
对于内存不是非常大的list，可以直接返回一个list，但是可读性yield更佳(人个喜好)。

python2.x内置generator功能的有xrange函数、itertools包等。

优化循环
循环之外能做的事不要放在循环内，比如下面的优化可以快一倍：

a = range(10000)
size_a = len(a)
%timeit -n 1000 for i in a: k = len(a)
%timeit -n 1000 for i in a: k = size_a
1000 loops, best of 3: 569 µs per loop
1000 loops, best of 3: 256 µs per loop
优化包含多个判断表达式的顺序
对于and，应该把满足条件少的放在前面，对于or，把满足条件多的放在前面。如：

a = range(2000)  
%timeit -n 100 [i for i in a if 10 < i < 20 or 1000 < i < 2000]
%timeit -n 100 [i for i in a if 1000 < i < 2000 or 100 < i < 20]     
%timeit -n 100 [i for i in a if i % 2 == 0 and i > 1900]
%timeit -n 100 [i for i in a if i > 1900 and i % 2 == 0]
100 loops, best of 3: 287 µs per loop
100 loops, best of 3: 214 µs per loop
100 loops, best of 3: 128 µs per loop
100 loops, best of 3: 56.1 µs per loop
使用join合并迭代器中的字符串
In [1]: %%timeit
   ...: s = ''
   ...: for i in a:
   ...:         s += i
   ...:
10000 loops, best of 3: 59.8 µs per loop
In [2]: %%timeit
s = ''.join(a)
   ...:
100000 loops, best of 3: 11.8 µs per loop
join对于累加的方式，有大约5倍的提升。

选择合适的格式化字符方式
s1, s2 = 'ax', 'bx'
%timeit -n 100000 'abc%s%s' % (s1, s2)
%timeit -n 100000 'abc{0}{1}'.format(s1, s2)
%timeit -n 100000 'abc' + s1 + s2
100000 loops, best of 3: 183 ns per loop
100000 loops, best of 3: 169 ns per loop
100000 loops, best of 3: 103 ns per loop
三种情况中，%的方式是最慢的，但是三者的差距并不大（都非常快）。(个人觉得%的可读性最好)

不借助中间变量交换两个变量的值
In [3]: %%timeit -n 10000
    a,b=1,2
   ....: c=a;a=b;b=c;
   ....:
10000 loops, best of 3: 172 ns per loop
In [4]: %%timeit -n 10000
a,b=1,2
a,b=b,a
   ....:
10000 loops, best of 3: 86 ns per loop
使用a,b=b,a而不是c=a;a=b;b=c;来交换a,b的值，可以快1倍以上。

使用if is
a = range(10000)
%timeit -n 100 [i for i in a if i == True]
%timeit -n 100 [i for i in a if i is True]
100 loops, best of 3: 531 µs per loop
100 loops, best of 3: 362 µs per loop
使用 if is True 比 if == True 将近快一倍。

使用级联比较x < y < z
x, y, z = 1,2,3
%timeit -n 1000000 if x < y < z:pass
%timeit -n 1000000 if x < y and y < z:pass
1000000 loops, best of 3: 101 ns per loop
1000000 loops, best of 3: 121 ns per loop
x < y < z效率略高，而且可读性更好。

while 1 比 while True 更快
def while_1():
    n = 100000
    while 1:
        n -= 1
        if n <= 0: break
def while_true():
    n = 100000
    while True:
        n -= 1
        if n <= 0: break    
m, n = 1000000, 1000000 
%timeit -n 100 while_1()
%timeit -n 100 while_true()
100 loops, best of 3: 3.69 ms per loop
100 loops, best of 3: 5.61 ms per loop
while 1 比 while true快很多，原因是在python2.x中，True是一个全局变量，而非关键字。

使用**而不是pow
%timeit -n 10000 c = pow(2,20)
%timeit -n 10000 c = 2**20
10000 loops, best of 3: 284 ns per loop
10000 loops, best of 3: 16.9 ns per loop
**就是快10倍以上！

使用 cProfile, cStringIO 和 cPickle等用c实现相同功能（分别对应profile, StringIO, pickle）的包
import cPickle
import pickle
a = range(10000)
%timeit -n 100 x = cPickle.dumps(a)
%timeit -n 100 x = pickle.dumps(a)
100 loops, best of 3: 1.58 ms per loop
100 loops, best of 3: 17 ms per loop
由c实现的包，速度快10倍以上！

使用最佳的反序列化方式
下面比较了eval, cPickle, json方式三种对相应字符串反序列化的效率：

import json
import cPickle
a = range(10000)
s1 = str(a)
s2 = cPickle.dumps(a)
s3 = json.dumps(a)
%timeit -n 100 x = eval(s1)
%timeit -n 100 x = cPickle.loads(s2)
%timeit -n 100 x = json.loads(s3)
100 loops, best of 3: 16.8 ms per loop
100 loops, best of 3: 2.02 ms per loop
100 loops, best of 3: 798 µs per loop
可见json比cPickle快近3倍，比eval快20多倍。

使用C扩展(Extension)
目前主要有CPython(python最常见的实现的方式)原生API, ctypes,Cython，cffi三种方式，它们的作用是使得Python程序可以调用由C编译成的动态链接库，其特点分别是：

CPython原生API: 通过引入Python.h头文件，对应的C程序中可以直接使用Python的数据结构。实现过程相对繁琐，但是有比较大的适用范围。

ctypes: 通常用于封装(wrap)C程序，让纯Python程序调用动态链接库（Windows中的dll或Unix中的so文件）中的函数。如果想要在python中使用已经有C类库，使用ctypes是很好的选择，有一些基准测试下，python2+ctypes是性能最好的方式。

Cython: Cython是CPython的超集，用于简化编写C扩展的过程。Cython的优点是语法简洁，可以很好地兼容numpy等包含大量C扩展的库。Cython的使得场景一般是针对项目中某个算法或过程的优化。在某些测试中，可以有几百倍的性能提升。

cffi: cffi的就是ctypes在pypy（详见下文）中的实现，同进也兼容CPython。cffi提供了在python使用C类库的方式，可以直接在python代码中编写C代码，同时支持链接到已有的C类库。

使用这些优化方式一般是针对已有项目性能瓶颈模块的优化，可以在少量改动原有项目的情况下大幅度地提高整个程序的运行效率。

并行编程
因为GIL的存在，Python很难充分利用多核CPU的优势。但是，可以通过内置的模块multiprocessing实现下面几种并行模式：

多进程：对于CPU密集型的程序，可以使用multiprocessing的Process,Pool等封装好的类，通过多进程的方式实现并行计算。但是因为进程中的通信成本比较大，对于进程之间需要大量数据交互的程序效率未必有大的提高。

多线程：对于IO密集型的程序，multiprocessing.dummy模块使用multiprocessing的接口封装threading，使得多线程编程也变得非常轻松(比如可以使用Pool的map接口，简洁高效)。

分布式：multiprocessing中的Managers类提供了可以在不同进程之共享数据的方式，可以在此基础上开发出分布式的程序。

不同的业务场景可以选择其中的一种或几种的组合实现程序性能的优化。

终级大杀器：PyPy
PyPy是用RPython(CPython的子集)实现的Python，根据官网的基准测试数据，它比CPython实现的Python要快6倍以上。快的原因是使用了Just-in-Time(JIT)编译器，即动态编译器，与静态编译器(如gcc,javac等)不同，它是利用程序运行的过程的数据进行优化。由于历史原因，目前pypy中还保留着GIL，不过正在进行的STM项目试图将PyPy变成没有GIL的Python。

如果python程序中含有C扩展(非cffi的方式)，JIT的优化效果会大打折扣，甚至比CPython慢（比Numpy）。所以在PyPy中最好用纯Python或使用cffi扩展。

随着STM，Numpy等项目的完善，相信PyPy将会替代CPython。

使用性能分析工具
除了上面在ipython使用到的timeit模块，还有cProfile。cProfile的使用方式也非常简单： python -m cProfile filename.py，filename.py 是要运行程序的文件名，可以在标准输出中看到每一个函数被调用的次数和运行的时间，从而找到程序的性能瓶颈，然后可以有针对性地优化。

参考
[1] http://www.ibm.com/developerworks/cn/linux/l-cn-python-optim/

[2] http://maxburstein.com/blog/speeding-up-your-python-code/

=========================

 

http://code.oneapm.com/python/2015/05/18/python-performance-tips/

原文地址：https://blog.newrelic.com/2015/01/21/python-performance-tips/

Python是一门优秀的语言，它能让你在短时间内通过极少量代码就能完成许多操作。不仅如此，它还轻松支持多任务处理，比如多进程。

不喜欢Python的人经常会吐嘈Python运行太慢。但是，事实并非如此。尝试以下六个窍门，来为你的Python应用提速。

窍门一：关键代码使用外部功能包
Python简化了许多编程任务，但是对于一些时间敏感的任务，它的表现经常不尽人意。使用C/C++或机器语言的外部功能包处理时间敏感任务，可以有效提高应用的运行效率。这些功能包往往依附于特定的平台，因此你要根据自己所用的平台选择合适的功能包。简而言之，这个窍门要你牺牲应用的可移植性以换取只有通过对底层主机的直接编程才能获得的运行效率。以下是一些你可以选择用来提升效率的功能包：

Cython
Pylnlne
PyPy
Pyrex
这些功能包的用处各有不同。比如说，使用C语言的数据类型，可以使涉及内存操作的任务更高效或者更直观。Pyrex就能帮助Python延展出这样的功能。Pylnline能使你在Python应用中直接使用C代码。内联代码是独立编译的，但是它把所有编译文件都保存在某处，并能充分利用C语言提供的高效率。

窍门二：在排序时使用键
Python含有许多古老的排序规则，这些规则在你创建定制的排序方法时会占用很多时间，而这些排序方法运行时也会拖延程序实际的运行速度。最佳的排序方法其实是尽可能多地使用键和内置的sort()方法。譬如，拿下面的代码来说：

    import operator
    somelist = [(1, 5, 8), (6, 2, 4), (9, 7, 5)]
    somelist.sort(key=operator.itemgetter(0))
    somelist
    #Output = [(1, 5, 8), (6, 2, 4), (9, 7, 5)]
    somelist.sort(key=operator.itemgetter(1))
    somelist
    #Output = [(6, 2, 4), (1, 5, 8), (9, 7, 5)]
    somelist.sort(key=operator.itemgetter(2))
    somelist
    #Output = [(6, 2, 4), (9, 7, 5), (1, 5, 8)],
在每段例子里，list都是根据你选择的用作关键参数的索引进行排序的。这个方法不仅对数值类型有效，还同样适用于字符串类型。

窍门三：针对循环的优化
每一种编程语言都强调最优化的循环方案。当使用Python时，你可以借助丰富的技巧让循环程序跑得更快。然而，开发者们经常遗忘的一个技巧是：尽量避免在循环中访问变量的属性。譬如，拿下面的代码来说：

    lowerlist = ['this', 'is', 'lowercase']
    upper = str.upper
    upperlist = []
    append = upperlist.append
    for word in lowerlist:
        append(upper(word))
        print(upperlist)
        #Output = ['THIS', 'IS', 'LOWERCASE']
每次你调用str.upper, Python都会计算这个式子的值。然而，如果你把这个求值赋值给一个变量，那么求值的结果就能提前知道，Python程序就能运行得更快。因此，关键就是尽可能减小Python在循环中的工作量。因为Python解释执行的特性，在上面的例子中会大大减慢它的速度。

（注意：优化循环的方法还有很多，这只是其中之一。比如，很多程序员会认为，列表推导式是提高循环速度的最佳方法。关键在于，优化循环方案是提高应用程序运行速度的上佳选择。）

窍门四：使用较新的Python版本
如果你在网上搜索Python，你会发现数不尽的信息都是关于如何升级Python版本。通常，每个版本的Python都会包含优化内容，使其运行速度优于之前的版本。但是，限制因素在于，你最喜欢的函数库有没有同步更新支持新的Python版本。与其争论函数库是否应该更新，关键在于新的Python版本是否足够高效来支持这一更新。

你要保证自己的代码在新版本里还能运行。你需要使用新的函数库才能体验新的Python版本，然后你需要在做出关键性的改动时检查自己的应用。只有当你完成必要的修正之后，你才能体会新版本的不同。

然而，如果你只是确保自己的应用在新版本中可以运行，你很可能会错过新版本提供的新特性。一旦你决定更新，请分析你的应用在新版本下的表现，并检查可能出问题的部分，然后优先针对这些部分应用新版本的特性。只有这样，用户才能在更新之初就觉察到应用性能的改观。

窍门五：尝试多种编码方法
每次创建应用时都使用同一种编码方法几乎无一例外会导致应用的运行效率不尽人意。可以在程序分析时尝试一些试验性的办法。譬如说，在处理字典中的数据项时，你既可以使用安全的方法，先确保数据项已经存在再进行更新，也可以直接对数据项进行更新，把不存在的数据项作为特例分开处理。请看下面第一段代码：

    n = 16
    myDict = {}
    for i in range(0, n):
        char = 'abcd'[i%4]
        if char not in myDict:
            myDict[char] = 0
            myDict[char] += 1
            print(myDict)
当一开始myDict为空时，这段代码会跑得比较快。然而，通常情况下，myDict填满了数据，至少填有大部分数据，这时换另一种方法会更有效率。

    n = 16
    myDict = {}
    for i in range(0, n):
        char = 'abcd'[i%4]
        try:
            myDict[char] += 1
        except KeyError:
            myDict[char] = 1
        print(myDict)
在两种方法中输出结果都是一样的。区别在于输出是如何获得的。跳出常规的思维模式，创建新的编程技巧能使你的应用更有效率。

窍门六：交叉编译你的应用
开发者有时会忘记计算机其实并不理解用来创建现代应用程序的编程语言。计算机理解的是机器语言。为了运行你的应用，你借助一个应用将你所编的人类可读的代码转换成机器可读的代码。有时，你用一种诸如Python这样的语言编写应用，再以C++这样的语言运行你的应用，这在运行的角度来说，是可行的。关键在于，你想你的应用完成什么事情，而你的主机系统能提供什么样的资源。

Nuitka是一款有趣的交叉编译器，能将你的Python代码转化成C++代码。这样，你就可以在native模式下执行自己的应用，而无需依赖于解释器程序。你会发现自己的应用运行效率有了较大的提高，但是这会因平台和任务的差异而有所不同。

（注意：Nuitka现在还处在测试阶段，所以在实际应用中请多加注意。实际上，当下最好还是把它用于实验。此外，关于交叉编译是否为提高运行效率的最佳方法还存在讨论的空间。开发者已经使用交叉编译多年，用来提高应用的速度。记住，每一种解决办法都有利有弊，在把它用于生产环境之前请仔细权衡。）

在使用交叉编译器时，记得确保它支持你所用的Python版本。Nuitka支持Python2.6, 2.7, 3.2和3.3。为了让解决方案生效，你需要一个Python解释器和一个C++编译器。Nuitka支持许多C++编译器，其中包括Microsoft Visual Studio,MinGW 和 Clang/LLVM。

交叉编译可能造成一些严重问题。比如，在使用Nuitka时，你会发现即便是一个小程序也会消耗巨大的驱动空间。因为Nuitka借助一系列的动态链接库（DDLs）来执行Python的功能。因此，如果你用的是一个资源很有限的系统，这种方法或许不太可行。

结论
前文所述的六个窍门都能帮助你创建运行更有效率的Python应用。但是银弹是不存在的。上述的这些窍门不一定每次都能奏效。在特定的Python的版本下，有的窍门或许比其他的表现更好，但这有时候甚至取决于平台的差异。你需要总结分析你的应用，找到它效率低下的部分，然后尝试这些窍门，找到解决问题的最佳方法。



首页 > Python > 几个提升Python运行效率的方法之间的对比
几个提升Python运行效率的方法之间的对比
这篇文章主要介绍了几个提升Python运行效率的方法之间的对比,包括使用Cython和PyPy等这些热门方法,需要的朋友可以参考下

在我看来，python社区分为了三个流派，分别是python 2.x组织，3.x组织和PyPy组织。这个分类基本上可以归根于类库的兼容性和速度。这篇文章将聚焦于一些通用代码的优化技巧以及编译成C后性能的显著提升，当然我也会给出三大主要python流派运行时间。我的目的不是为了证明一个比另一个强，只是为了让你知道如何在不同的环境下使用这些具体例子作比较。

使用生成器

一个普遍被忽略的内存优化是生成器的使用。生成器让我们创建一个函数一次只返回一条记录，而不是一次返回所有的记录，如果你正在使用python2.x，这就是你为啥使用xrange替代range或者使用ifilter替代filter的原因。一个很好地例子就是创建一个很大的列表并将它们拼合在一起。

import timeit
import random
 
def generate(num):
while num:
yield random.randrange(10)
num -= 1
 
def create_list(num):
numbers = []
while num:
numbers.append(random.randrange(10))
num -= 1
return numbers
print(timeit.timeit("sum(generate(999))", setup="from __main__ import generate", number=1000))
>>> 0.88098192215 #Python 2.7
>>> 1.416813850402832 #Python 3.2
print(timeit.timeit("sum(create_list(999))", setup="from __main__ import create_list", number=1000))
>>> 0.924163103104 #Python 2.7
>>> 1.5026731491088867 #Python 3.2
这不仅是快了一点，也避免了你在内存中存储全部的列表!

Ctypes的介绍

对于关键性的性能代码python本身也提供给我们一个API来调用C方法，主要通过 ctypes来实现，你可以不写任何C代码来利用ctypes。默认情况下python提供了预编译的标准c库，我们再回到生成器的例子，看看使用ctypes实现花费多少时间。

import timeit
from ctypes import cdll
 
def generate_c(num):
#Load standard C library
libc = cdll.LoadLibrary("libc.so.6") #Linux
#libc = cdll.msvcrt #Windows
while num:
yield libc.rand() % 10
num -= 1
 
print(timeit.timeit("sum(generate_c(999))", setup="from __main__ import generate_c", number=1000))
>>> 0.434374809265 #Python 2.7
>>> 0.7084300518035889 #Python 3.2
仅仅换成了c的随机函数，运行时间减了大半！现在如果我告诉你我们还能做得更好，你信吗?

Cython的介绍

Cython 是python的一个超集，允许我们调用C函数以及声明变量来提高性能。尝试使用之前我们需要先安装Cython.

sudo pip install cython
Cython 本质上是另一个不再开发的类似类库Pyrex的分支，它将我们的类Python代码编译成C库，我们可以在一个python文件中调用。对于你的python文件使用.pyx后缀替代.py后缀，让我们看一下使用Cython如何来运行我们的生成器代码。

#cython_generator.pyx
import random
 
def generate(num):
while num:
yield random.randrange(10)
num -= 1
我们需要创建个setup.py以便我们能获取到Cython来编译我们的函数。

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
 
setup(
cmdclass = {'build_ext': build_ext},
ext_modules = [Extension("generator", ["cython_generator.pyx"])]
)
编译使用:

python setup.py build_ext --inplace
你应该可以看到两个文件cython_generator.c 文件 和 generator.so文件，我们使用下面方法测试我们的程序:

import timeit
print(timeit.timeit("sum(generator.generate(999))", setup="import generator", number=1000))
>>> 0.835658073425
还不赖，让我们看看是否还有可以改进的地方。我们可以先声明“num”为整形，接着我们可以导入标准的C库来负责我们的随机函数。

#cython_generator.pyx
cdef extern from "stdlib.h":
int c_libc_rand "rand"()
 
def generate(int num):
while num:
yield c_libc_rand() % 10
num -= 1
如果我们再次编译运行我们会看到这一串惊人的数字。

>>> 0.033586025238
仅仅的几个改变带来了不赖的结果。然而，有时这个改变很乏味，因此让我们来看看如何使用规则的python来实现吧。
PyPy的介绍

PyPy 是一个Python2.7.3的即时编译器，通俗地说这意味着让你的代码运行的更快。Quora在生产环境中使用了PyPy。PyPy在它们的下载页面有一些安装说明，但是如果你使用的Ubuntu系统，你可以通过apt-get来安装。它的运行方式是立即可用的，因此没有疯狂的bash或者运行脚本，只需下载然后运行即可。让我们看看我们原始的生成器代码在PyPy下的性能如何。

import timeit
import random
 
def generate(num):
while num:
yield random.randrange(10)
num -= 1
 
def create_list(num):
numbers = []
while num:
numbers.append(random.randrange(10))
num -= 1
return numbers
print(timeit.timeit("sum(generate(999))", setup="from __main__ import generate", number=1000))
>>> 0.115154981613 #PyPy 1.9
>>> 0.118431091309 #PyPy 2.0b1
print(timeit.timeit("sum(create_list(999))", setup="from __main__ import create_list", number=1000))
>>> 0.140175104141 #PyPy 1.9
>>> 0.140514850616 #PyPy 2.0b1
哇！没有修改一行代码运行速度是纯python实现的8倍。

进一步测试为什么还要进一步研究？PyPy是冠军！并不全对。虽然大多数程序可以运行在PyPy上，但是还是有一些库没有被完全支持。而且，为你的项目写C的扩展相比换一个编译器更加容易。让我们更加深入一些，看看ctypes如何让我们使用C来写库。我们来测试一下归并排序和计算斐波那契数列的速度。下面是我们要用到的C代码（functions.c）：

/* functions.c */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
/* http://rosettacode.org/wiki/Sorting_algorithms/Merge_sort#C */
inline void
merge (int *left, int l_len, int *right, int r_len, int *out)
{
int i, j, k;
for (i = j = k = 0; i < l_len && j < r_len;)
out[k++] = left[i] < right[j] ? left[i++] : right[j++];
while (i < l_len)
out[k++] = left[i++];
while (j < r_len)
out[k++] = right[j++];
}
 
/* inner recursion of merge sort */
void
recur (int *buf, int *tmp, int len)
{
int l = len / 2;
if (len <= 1)
return;
/* note that buf and tmp are swapped */
recur (tmp, buf, l);
recur (tmp + l, buf + l, len - l);
merge (tmp, l, tmp + l, len - l, buf);
}
 
/* preparation work before recursion */
void
merge_sort (int *buf, int len)
{
/* call alloc, copy and free only once */
int *tmp = malloc (sizeof (int) * len);
memcpy (tmp, buf, sizeof (int) * len);
recur (buf, tmp, len);
free (tmp);
}
 
int
fibRec (int n)
{
if (n < 2)
return n;
else
return fibRec (n - 1) + fibRec (n - 2);
}
在Linux平台，我们可以用下面的方法把它编译成一个共享库：

gcc -Wall -fPIC -c functions.c
gcc -shared -o libfunctions.so functions.o
使用ctypes， 通过加载”libfunctions.so”这个共享库，就像我们前边对标准C库所作的那样，就可以使用这个库了。这里我们将要比较Python实现和C实现。现在我们开始计算斐波那契数列：

# functions.py
 
from ctypes import *
import time
 
libfunctions = cdll.LoadLibrary("./libfunctions.so")
 
def fibRec(n):
if n < 2:
return n
else:
return fibRec(n-1) + fibRec(n-2)
 
start = time.time()
fibRec(32)
finish = time.time()
print("Python: " + str(finish - start))
 
# C Fibonacci
start = time.time()
x = libfunctions.fibRec(32)
finish = time.time()
print("C: " + str(finish - start))
正如我们预料的那样，C比Python和PyPy更快。我们也可以用同样的方式比较归并排序。

我们还没有深挖Cypes库，所以这些例子并没有反映python强大的一面，Cypes库只有少量的标准类型限制，比如int型，char数组，float型，字节（bytes）等等。默认情况下，没有整形数组，然而通过与c_int相乘（ctype为int类型）我们可以间接获得这样的数组。这也是代码第7行所要呈现的。我们创建了一个c_int数组，有关我们数字的数组并分解打包到c_int数组中

主要的是c语言不能这样做，而且你也不想。我们用指针来修改函数体。为了通过我们的c_numbers的数列，我们必须通过引用传递merge_sort功能。运行merge_sort后，我们利用c_numbers数组进行排序，我已经把下面的代码加到我的functions.py文件中了。

#Python Merge Sort
from random import shuffle, sample
#Generate 9999 random numbers between 0 and 100000
numbers = sample(range(100000), 9999)
shuffle(numbers)
c_numbers = (c_int * len(numbers))(*numbers)
from heapq import merge
def merge_sort(m):
if len(m) <= 1:
return m
middle = len(m) // 2
left = m[:middle]
right = m[middle:]
left = merge_sort(left)
right = merge_sort(right)
return list(merge(left, right))
start = time.time()
numbers = merge_sort(numbers)
finish = time.time()
print("Python: " + str(finish - start))
#C Merge Sort
start = time.time()
libfunctions.merge_sort(byref(c_numbers), len(numbers))
finish = time.time()
print("C: " + str(finish - start))
Python: 0.190635919571 #Python 2.7
Python: 0.11785483360290527 #Python 3.2
Python: 0.266992092133 #PyPy 1.9
Python: 0.265724897385 #PyPy 2.0b1
C: 0.00201296806335 #Python 2.7 + ctypes
C: 0.0019741058349609375 #Python 3.2 + ctypes
C: 0.0029308795929 #PyPy 1.9 + ctypes
C: 0.00287103652954 #PyPy 2.0b1 + ctypes
