# coding=utf-8
import addressbook_pb2

address_book = addressbook_pb2.AdressBook()

#### person1 ###
p1 = address_book.people
#p1 = p1.append()
p1.name = "Jack"
p1.id = 20
p1.email = "jack@qq.com"

phone_num1 = p1.phones.add()
phone_num1.number = "123"
phone_num1.type = 2  # 与默认类型不同

phone_num2 = p1.phones.add()
phone_num2.number = "456"
print(p1)

### person2 ###
p2 = address_book.people#.add()
p2.name = "Chen"
p2.id = 21

# 遍历，输出repeated类型的成员
for phone in p1.phones:
    print(phone.type)

# 保存到二进制文件
f = open("address.pb", "wb")
f.write(address_book.SerializeToString()) # 调用串行化接口
f.close()

