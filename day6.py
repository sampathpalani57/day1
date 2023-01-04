print('this is starting exception')
try:
    print(5/0)
    print('no exception')
except ZeroDivisionError:
    print('this is except')
finally:
    print('this is finally')
print('this is ending exception')