#这种方式每次需要执行close关闭文件
"""f=(open('datas/txtfile', 'rt'))
print(f.read())
f.close()
"""
#方法2 自动回收资源，且这种方式打开的文件是以列表的形式返回的
with open('datas/txtfile') as f:
    '''print(f.readlines())'''
    while True:
        line=f.readline()
        if line:
            print(line)
        else:
            break