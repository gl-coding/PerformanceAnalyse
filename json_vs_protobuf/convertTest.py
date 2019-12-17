#encoding=utf8

from example import personInfo_pb2
from example import person_pb2

from google.protobuf.json_format import MessageToJson, Parse
import json

def json_to_proto():
    f = file("./example/personInfo.json")
    json_dic = json.load(f)
    json_str = json.dumps(json_dic)
    proto_str = Parse(json_str, personInfo_pb2.PersonInfo())
    print proto_str

def proto_to_json():
    message = personInfo_pb2.PersonInfo()
    message.name = "adf"
    json_string = MessageToJson(message)
    print json_string

def serialize():
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
    print data

    # 对已经序列化的数据进行反序列化
    target = person_pb2.all_person()
    target.ParseFromString(data)
    print(target.Per[1].name)  #  打印第一个 person name 的值进行反序列化验证
    print(target.Per[1].id)

if __name__ == "__main__":
    #json_to_proto()
    #proto_to_json()
    serialize()
