#proto2
protoc --python_out=. ./proto2/addressbook.proto

#proto3
protoc --python_out=. ./example/person.proto
protoc --python_out=. ./example/personInfo.proto
protoc --python_out=. ./example/addressbook.proto

protoc --python_out=. ./tutorial/emu.proto
protoc --python_out=. ./tutorial/addressbook.proto
