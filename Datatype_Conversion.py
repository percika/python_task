Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('Hello world')
Hello world
a=10
b=9
print(a*b)
90
print(type(a))
<class 'int'>
var_flt=10.23
print(int(var_flt))
10
print(str(var_flt))
10.23
print(bool(var_flt))
True
var_int=34
print(flt(var_int))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(flt(var_int))
NameError: name 'flt' is not defined
print(float(var_int))
34.0
print(str(var_int))
34
print(bool(var_int))
True
var_str="10.23"
print(int(var_str))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(int(var_str))
ValueError: invalid literal for int() with base 10: '10.23'
print(float(var_str))
10.23
print(bool(var_str))
True
#Create boolean and convert into different datatype
#Create boolean and convert into different datatype
var_bool=false
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    var_bool=false
NameError: name 'false' is not defined. Did you mean: 'False'?
var_bool=False
print(float(var_bool))
0.0
print(str(var_bool))
False
print(int(var_bool))
0
