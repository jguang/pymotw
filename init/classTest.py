'''
__new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供

__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例

__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值

我们可以将类比作制造商，__new__方法就是前期的原材料购买环节，__init__方法就是在有原材料的基础上，加工，初始化商品环节
'''


class TestClass(object):
    def __init__(cls, m):
        print(m)
        print('__init__执行')

    def __new__(cls, m):
        print(cls)
        print(m)
        print('__new__执行')
        return super.__new__(cls)

    def __str__(self):
        print('str')
        return '__str__执行'


if __name__ == '__main__':
    test = TestClass(222)
    print(test)
