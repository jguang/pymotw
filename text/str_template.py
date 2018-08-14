import string

"""
字符替换:
%s变量，对应元组字符串替换如, print('%sDDD' % ('aa'))元组长度为一可省略其变为字符串

%(var)s, 对应字典, print('%(var)sDDDDD' % {'var':'CCCCCC'})

"""

values = {'var': 'foo'}

t = string.Template("""
Variable        : $var
Escape          : $$AAA
Variable in text: ${var}iable
""")

print('TEMPLATE:', t.substitute(values))

s = """
Variable        : %(var)s
Escape          : %%AAA
Variable in text: %(var)siable
"""

print('INTERPOLATION:', s % values)

s = """
Variable        : {var}
Escape          : {{}}AAA
Variable in text: {var}iable
"""

print('FORMAT:', s.format(**values))


s = """
Baidu: %(baid)s-DDD
Google: %(goog)s-ADDD
"""

bg = {'baid': 'aaa', 'goog': 'bbbbb'}

print('test %', s % bg)

print('%sAAA%sAA' % ('ddd', 'RRRR'))
