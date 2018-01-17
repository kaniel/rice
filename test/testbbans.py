#-*- coding:utf-8 -*-

import talib
import numpy
import time
import pandas
import json
from pandas import Series, DataFrame

# data = '''[["1516085400000","0.01379","0.01379","0.01371614","0.0137899","58.72669144"],["1516085460000","0.01367977","0.01367977","0.01352799","0.01352799","300.06164706"],["1516085520000","0.01352799","0.01366108","0.01352799","0.01366107","25.27772642"],["1516085580000","0.01366102","0.01366111","0.01366098","0.01366111","65.45389138"],["1516085640000","0.01366","0.01366111","0.01365999","0.01366111","142.35465322"],["1516085700000","0.01366111","0.01378999","0.0136002","0.01378999","115.51216144"],["1516085760000","0.01360057","0.01360057","0.01360056","0.01360056","9.8"],["1516085820000","0.01378941","0.01378941","0.01362775","0.01378909","36.7343832"],["1516085880000","0.01378901","0.01378901","0.01378901","0.01378901","0.12604112"],["1516085940000","0.01378838","0.0137884","0.01378822","0.01378822","35.72186312"],["1516086000000","0.01361447","0.01377805","0.01361447","0.01377759","12.12532466"],["1516086060000","0.01377751","0.01377751","0.01377741","0.01377741","2.90324216"],["1516086120000","0.01377686","0.01377686","0.01377686","0.01377686","3.4461989"],["1516086180000","0.01360209","0.0137765","0.01360209","0.01361005","72.8601515"],["1516086240000","0.01361009","0.01377589","0.013555","0.01361014","466.05894804"],["1516086300000","0.01377582","0.01377588","0.0136102","0.01377565","438.38483164"],["1516086360000","0.01361046","0.0137756","0.01361046","0.01377534","17.30278526"],["1516086420000","0.01377491","0.01377491","0.01377491","0.01377491","0.33416752"],["1516086480000","0.01375052","0.01375052","0.01375051","0.01375051","0.46619984"],["1516086540000","0.01375051","0.01375051","0.01375051","0.01375051","0"]]'''

data = '''[["1516174980000","0.01165431","0.01165431","0.01165431","0.01165431","0"],["1516175040000","0.01146853","0.01146853","0.01146851","0.01146851","88.22848936"],["1516175100000","0.01146851","0.01146851","0.01146851","0.01146851","0"],["1516175160000","0.01146851","0.01146851","0.01146851","0.01146851","0"],["1516175220000","0.01146851","0.01146851","0.01146851","0.01146851","0"],["1516175280000","0.01162752","0.01162752","0.01162752","0.01162752","18.44130336"],["1516175340000","0.01162752","0.01162752","0.01162752","0.01162752","0"],["1516175400000","0.01162675","0.01162675","0.01162675","0.01162675","0.85970774"],["1516175460000","0.01162675","0.01162675","0.01162675","0.01162675","0"],["1516175520000","0.01162613","0.01162616","0.01162597","0.01162598","154.7848659"],["1516175580000","0.01162598","0.01162598","0.01162598","0.01162598","0"],["1516175640000","0.01162598","0.01162598","0.01162598","0.01162598","0"],["1516175700000","0.01162731","0.01162731","0.01162731","0.01162731","0"],["1516175760000","0.01162731","0.01162731","0.01162731","0.01162731","0"],["1516175820000","0.01143939","0.01162663","0.01143939","0.01162663","33.18399838"],["1516175880000","0.01162663","0.01162663","0.01162663","0.01162663","0"],["1516175940000","0.01162663","0.01162663","0.01162663","0.01162663","0"],["1516176000000","0.01162663","0.01162663","0.01162663","0.01162663","0"],["1516176060000","0.01162552","0.01162552","0.01162552","0.01162552","0"],["1516176120000","0.01162552","0.01162552","0.01162552","0.01162552","0"]]'''


k_data = json.loads(data)
d_time = list()
high = list()
open = list()
low = list()
close_s = list()
scale = list()
for item in k_data:
    # print type(item)
    if isinstance(item, list):
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(item[0])/1000))
        print item
        # close.append(float(item[4]))
        d_time.append(float(item[0]))
        open.append(float(item[1]))
        high.append(float(item[2]))
        low.append(float(item[3]))
        close_s.append(float(item[4]))
        scale.append(float(item[5]))
        # s_data.append(float(item[4]))
    else:
        print "not list"

# data_1 = ["1516086600000", "0.01375051", "0.01375051", "0.01375051", "0.01375051", "0"]
data_1 = ["1516176180000","0.01162727","0.01162727","0.01162726","0.01162726","15.30478846"]
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(data_1[0])/1000))
# close.append(float(data_1[4]))
# s_data.append(float(data_1[4]))
d_time.append(float(data_1[0]))
open.append(float(data_1[1]))
high.append(float(data_1[2]))
low.append(float(data_1[3]))
close_s.append(float(data_1[4]))
scale.append(float(data_1[5]))

# data_2 = ["1516086600000","0.01372999","0.01372999","0.01372999","0.01372999","8.92727964"]
# print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(data_1[0])/1000))
# # close.append(float(data_1[4]))
# # s_data.append(float(data_2[4]))
# d_time.append(float(data_2[0]))
# open.append(float(data_2[1]))
# high.append(float(data_2[2]))
# low.append(float(data_2[3]))
# close_s.append(float(data_2[4]))
# scale.append(float(data_2[5]))

# data_3 = ["1516086660000","0.01372999","0.01372999","0.01372999","0.01372999","0"]
# print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(data_1[0])/1000))
# # close.append(float(data_3[4]))
# # s_data.append(float(data_3[4]))
# d_time.append(float(data_3[0]))
# open.append(float(data_3[1]))
# high.append(float(data_3[2]))
# low.append(float(data_3[3]))
# close_s.append(float(data_3[4]))
# scale.append(float(data_3[5]))

close_d = [x * 10 for x in close_s]
print close_d[0]

data_dict = dict()
data_dict["time"] = numpy.array(d_time, dtype='float')
data_dict["open"] = numpy.array(open, dtype='float')
data_dict["high"] = numpy.array(high, dtype='float')
data_dict["low"] = numpy.array(low, dtype='float')
data_dict["close"] = numpy.array(close_d, dtype='float')
data_dict["volume"] = numpy.array(scale, dtype='float')
print "data_dict:", data_dict

ds = DataFrame(data_dict, columns=["time", "open", "high", "low", "close", "volume"])
print "date_frmae:", type(ds), ds
print "close:", ds.close


input_data = numpy.array(data_dict["close"], dtype='float')
print type(input_data), type(input_data[0]), input_data[0], input_data
# upper, middle, lower = talib.BBANDS(input_data, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
upper, middle, lower = talib.BBANDS(input_data, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
# upper, middle, lower = talib.BBANDS(closed, matype=talib.MA_Type.T3)
# upper = [item for item in upper if numpy.isnan(item) else item]
upper = [item if numpy.isnan(item) else item / 10 for item in upper]
middle = [item if numpy.isnan(item) else item / 10 for item in middle]
lower = [item if numpy.isnan(item) else format(item / 10, ".6f") for item in lower]
print "1", "-" * 30
print "upper:", type(upper), upper
print "middle:", middle
print "lower:", lower
