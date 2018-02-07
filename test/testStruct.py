# -*- coding:utf-8 -*-

import struct

str_code = struct.pack("ii", 20, 400)
print str_code
print len(str_code)

a1, a2 = struct.unpack("ii", str_code)

print "a1: %s     a2:%s" % (str(a1), str(a2))
print 'struct.calcsize:', struct.calcsize("ii")

string = 'test astring'
format_code = '5s 4x 3s'
print struct.unpack(format_code, string)

string = 'he is not very happy'
format_code = '2s 1x 2s 5x 4s 1x 5s'
print struct.unpack(format_code, string)

a = 20
b = 400
str_code = struct.pack("ii", a, b)
print "length:", len(str_code)
print str_code
print repr(str_code)

str_code = struct.pack("QH14sHI", 51213234232342412, 78, "sdffsd1111", 89, 3000)
print len(str_code), str_code
print repr(str_code)
a, b, c, d, h = struct.unpack("QH14sHI", str_code)
print a, b
print len(c), c, c[-1]
print d, h
