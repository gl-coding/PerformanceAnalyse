json与protobuf的速度之争

json是这些年慢慢兴起的轻量级数据交换格式。比起老大哥XML。因其更快的解析速度和更小的体积，可谓是用过的都说好。一般情况下json足够满足你的大多数需求，但是在计算机领域，没有最快，只有更快。
当你的传输数据大到一定程度的时候，json的速度也不能满足你需求的时候，你就需要更快的protobuf。
protocolbuffer(以下简称PB)是google 的一种数据交换的格式，它独立于语言，独立于平台。(百度百科)。
因为其使用二进制存储，所以会比json更快。但是缺点也是显而易见，二进制存储易读性很差。
我曾遇到要解析40M json的需求。在PC端，使用litjson需要解析10秒钟。但是将相同的内容通过protobuf再导出成bytes。只要17M。缩小了2.5倍左右。但是读取速度只要0.8秒，还包括了数据解析后的处理。
0.1秒和0.008秒可能给人差别不大，但是10秒和0.8秒的差别真的是天壤地别。

如果需要传输的数据量比较大时，protobuf是你的不二选择。

安装

brew install protobuf

生成和使用
新建 protobufExample

在protobufExample下面新建一个proto文件，取名person。

syntax = "proto3";
package protobufExample;

message person {
    int32 id = 1;
    string name = 2;
}

message all_person {
    repeated person Per = 1;
}

使用protoc编译生成proto文件如图：

$ protoc --python_out=. person.proto
就会生成 person.pb2.py 文件


main.py中编写序列化与反序列化的测试代码：

#! /usr/bin/env python
# -*- coding: utf-8 -*-
from protobufExample import person_pb2

# 为 all_person 填充数据
pers = person_pb2.all_person()
p1 = pers.Per.add()
p1.id = 1
p1.name = 'xieyanke'
p2 = pers.Per.add()
p2.id = 2
p2.name = 'pythoner'

# 对数据进行序列化
data = pers.SerializeToString()

# 对已经序列化的数据进行反序列化
target = person_pb2.all_person()
target.ParseFromString(data)
print(target.Per[1].name)  #  打印第一个 person name 的值进行反序列化验证
print(target.Per[1].id)
如此大功告成了

protobuf2语法介绍
Protobuf的语法
*.proto文件中数据类型可以分为两大类:
复合数据类型包括：枚举和message类型
标准数据类型包含：整型，浮点，字符串等

数据类型前面修饰词：
①required: 必须赋值，不能为空，否则该条message会被认为是“uninitialized”。除此之外，“required”字段跟“optional”字段并无差别。

②optional:字段可以赋值，也可以不赋值。假如没有赋值的话，会被赋上默认值。

③repeated: 该字段可以重复任意次数，包括0次。重复数据的顺序将会保存在protocol buffer中，将这个字段想象成一个可以自动设置size的数组就可以了。

每个字段要给数字
该Number是用来标记该字段在序列化后的二进制数据中所在的field，每个字段的Number在message内部都是独一无二的。也不能进行改变，否则数据就不能正确的解包

protobuf3语法介绍
1.字段前取消了required和optional两个关键字，目前可用的只有repeated关键字。
2.不可以现设置默认值了。
　　a.string默认为空串
　　b.枚举默认为第一个枚举定义的第一个值。并且必须是0,必须有有一个0值，我们可以用这个0值作为默认值。
这个零值必须为第一个元素，为了兼容proto2语义，枚举类的第一个值总是默认值。
　　c.bytes默认为空bytes
　　d.bool默认为false
　　e.数字类型默认为0
3.protoType类型如下：
double、float、int32、int64、uint32、uint64、sint32、sint64、fixed32、fixed64、sfixed32、sfixed64、bool、string、bytes

4、分配标识号
正如你所见，在消息定义中，每个字段都有唯一的一个数字标识符。这些标识符是用来在消息的二进制格式中识别各个字段的，一旦开始使用就不能够再改变。注：[1,15]之内的标识号在编码的时候会占用一个字节。[16,2047]之内的标识号则占用2个字节。所以应该为那些频繁出现的消息元素保留 [1,15]之内的标识号。切记：要为将来有可能添加的、频繁出现的标识号预留一些标识号。

最小的标识号可以从1开始，最大到2^29 - 1, or 536,870,911。不可以使用其中的[19000－19999]（ (从FieldDescriptor::kFirstReservedNumber 到 FieldDescriptor::kLastReservedNumber)）的标识号， Protobuf协议实现中对这些进行了预留。如果非要在.proto文件中使用这些预留标识号，编译时就会报警。同样你也不能使用早期保留的标识号。

指定字段规则
所指定的消息字段修饰符必须是如下之一：
singular：一个格式良好的消息应该有0个或者1个这种字段（但是不能超过1个）。
repeated：在一个格式良好的消息中，这种字段可以重复任意多次（包括0次）。重复的值的顺序会被保留。
在proto3中，repeated的标量域默认情况虾使用packed。


安装完成，验证Linux命令
protoc –version

验证Python模块是否被正确安装
python

import google.protobuf
如果没有报错，说明安装正常。

文件的第一行指定了你正在使用proto3语法：如果你没有指定这个，编译器会使用proto2。这个指定语法行必须是文件的非空非注释的第一个行。

外部引用：
我们将addressbook.proto中的repeated MyMessage maps = 7;进行了外部引用，

编译顺序：
然后首先对emu.proto进行编译，
protoc ./emu.proto --python_out=./

然后会addressbook.proto进行编译
protoc ./addressbook.proto --python_out=./
然后会默认生成上述截图中的emu_pb2.py、addressbook_pb2.py文件
