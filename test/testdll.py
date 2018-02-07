# -*- coding:utf-8 -*-

from ctypes import *

# dll = CDLL("MathFuncsDll.dll")
# dll = cdll.LoadLibrary("MathFuncsDll.dll")
# dll = windll.LoadLibrary("MathFuncsDll.dll")
dll = WinDLL("MathFuncsDll.dll")
szPara = create_string_buffer('/0' * 5)
print "szpara:", szPara, szPara.value
a = c_double(2.09)
b = c_double(21.3)
print type(a), type(b), a.value, b.value
subtract_double = dll.Subtract_d
subtract_double.restype = c_double
print "subtract:", subtract_double(a, b)

e1 = c_double(2.019)
e2 = c_double(43.43)
add_double = dll.Add_d
add_double.restype = c_double
print "test double:", add_double(e1, e2)

input_c = c_char_p("ssdfasdfsdfs")
print "input_c:", type(input_c), input_c, input_c.value
input_c.value = "90sdfsdfa111111111"
print input_c.value
deivied_str = dll.Divide_s
deivied_str.restype = c_char_p

print "str:", type(deivied_str(input_c)), deivied_str(input_c)

print type(c_char), c_char * 2


class keywords(Structure):
    _fields_ = [("words", c_char * 20), ]


class outStruct(Structure):
    _fields_ = [("kws", POINTER(keywords)),
                ("len", c_int)]


o = outStruct()
dll.test(byref(o))

print o.kws[0].words, "test1"
print o.kws[1].words, "test2"
# print o.kws[3].words, "test2"
print o.len


class MyStruct(Structure):
    _fields_ = [("numA", c_int), ("numB", c_int), ("sum", c_int), ("numStr", c_char * 256)]

sumnum = dll.sumnum
sumnum.restype = c_int
sumnum.argtype = [POINTER(MyStruct)]

newStruct = MyStruct()
newStruct.numA = 1
newStruct.numB = 5

ret = sumnum(byref(newStruct))

print "ret:", ret
print "num:", newStruct.sum
print "str:", len(newStruct.numStr), newStruct.numStr


dll = WinDLL("guiddll.dll")
print dll.add(c_int(1), c_int(290))

i = c_int()
f = c_float()
s = create_string_buffer('\000' * 32)
print "sizeof:", sizeof(i), sizeof(f), sizeof(s)
print i.value, f.value, repr(s.value)


def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for x in fibon(100):
    print x

gen = fibon(100)
print next(gen)
print next(gen)
print next(gen)

def generator_function():
    for item in range(3):
        yield item


gen = generator_function()

print next(gen)
print next(gen)
print next(gen)
# print next(gen)


my_str = "Yasoob"
# next(my_str)
my_iter = iter(my_str)
print type(my_iter), my_str
print next(my_iter)
print next(my_iter)
print next(my_iter)

items = [1, 2, 3, 4, 5]
res_items = squared = list(map(lambda x: x**2, items))
print res_items


def multiply(x):
    return (x * x)


def add(x):
    return (x + x)


funcs = [multiply, add]
for i in range(5):
    value = map(lambda x: x(i), funcs)
    print(list(value))


number_list = range(-5, 5)
print number_list
less_than_zero = filter(lambda x: x < 0, number_list)
print(list(less_than_zero))

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

is_fat = True
state = "fat" if is_fat else "not fat"
print state

fat = False
fitness = ("skinny", "fat")[fat]
print("Ali is", fitness)

from collections import defaultdict

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)

from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)
print(favs)

from collections import deque

# d = deque()
# d.append(1)
# d.append(2)
# d.append(3)
#
# print len(d)

d = deque(range(5))
print d.popleft()
print d.pop()
print d

d2 = deque(maxlen=30)
d2 = deque(range(5))
d2.extendleft([-1])
d2.extend([7, 8, 9])
print d2

from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print perry
print perry._asdict()

my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 2):
    print(c, value)

my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
print id(counter_list)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
