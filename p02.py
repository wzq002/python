# -*- encoding: utf-8 -*-
''' 演示正则表达式
'''

# python apps
import re


def main_v1():
    ''' 演示 ?P<o_id> 的作用 '''
    msg = '''/book/1234/'''
    s_re = r'(?P<o_id>\d+)'
    pattern = re.compile(s_re)
    obj = pattern.search(msg)
    print('obj.group(): {}'.format(obj.group()))
    print('obj.groups(): {}'.format(obj.groups()))
    info = obj.groupdict()
    print('obj.groupdict(): {}'.format(info))

    s_re_2 = r'(\d+)'
    pattern_2 = re.compile(s_re_2)
    obj_2 = pattern_2.search(msg)
    print('obj_2.group(): {}'.format(obj_2.group()))
    print('obj_2.groups(): {}'.format(obj_2.groups()))
    info_2 = obj_2.groupdict()
    print('obj_2.groupdict(): {}'.format(info_2))


if __name__ == '__main__':
    main_v1()
