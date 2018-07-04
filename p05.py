# -*- encoding: utf-8 -*-

# python apps
import pdb


class TraceBlock:
    def message(self, arg):
        print('running {}'.format(arg))

    def __enter__(self):
        print('TraceBlock.__enter__(): ...')
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('exc_type, exc_value, exc_tb: {}'.format( (exc_type, exc_value, exc_tb) ))
        # pdb.set_trace()

        if exc_type:
            print('raise an exception! {}'.format(exc_type))
            return False
        else:
            print('ok.')


# action = None
# print('action: {}'.format(action))
# with TraceBlock() as action:
#     print('action: {}'.format(action))
#     action.message('test 1')
#     print('..............')
# print('action: {}'.format(action))


i = 1
with TraceBlock() as action:
    action.message('test 2')
    # raise TypeError('类型错误')
    assert 0 < i, ValueError('值错误')
    print('--------------')

