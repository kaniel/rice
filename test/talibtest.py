# -*- coding:utf-8 -*-

print "sss"

import talib
import numpy
import time
import pandas

close = numpy.random.random(3)
print close
output = talib.SMA(close)
print "output:", output

start = time.clock()
mc = talib.SMA(close, timeperiod=2)
end = time.clock()
print "time:", end - start, type(mc[-1]), mc
start = time.clock()
df = pandas.DataFrame(close, columns=["close"])
# print df
# print "-------------------"
# print df.head()
# print "-------------------"
ds = df.rolling(2).mean()
end = time.clock()
print "\ntime:1", end - start, ds


a = numpy.array([1, -1, 1, -1, 1, -1], dtype='float')
rsi = talib.RSI(a, timeperiod=2)
print rsi
