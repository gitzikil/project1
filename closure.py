def outer_func():
    message = 'hi'
    def inner_func():
        print(message)
    return inner_func()

outer_func #outer_func 자체
outer_func() #outer_func 수행 결과 (inner_func 수행 결과 ('hi')를 return)



def outer_funcx():
    message = 'hi hi'
    def inner_funcx():
        print(message)
    return inner_funcx
print(outer_funcx.__name__)
outer_funcx   #outer_funcx 자체 (function object)
outer_funcx() #outer_funcx 수행 결과 (inner_funcx 자체를 return)
call_f = outer_funcx() #call_f 에 inner_funcx 가 할당됨
call_f() #inner_funcx 을 수행한 결과('hi hi')를 return

print(call_f)
print(dir(call_f))
print(call_f.__closure__)
print(call_f.__closure__[0])
print(dir(call_f.__closure__[0]))
print(call_f.__closure__[0].cell_contents)
print()
print(outer_funcx)
print(dir(outer_funcx))
print(outer_funcx().__closure__[0])
print(outer_funcx().__closure__[0].cell_contents)
print('-'*30)
def outer_func1(tag):
    txt1 = 'some title'
    txt2 = 'some text'
    tg = tag

    def inner_function1():
        if tg == 'h1':
            print('<{0}>{1}<{0}>'.format(tg, txt1))
        else:
            print('<{0}>{1}<{0}>'.format(tg, txt2))

    return inner_function1

call1_func = outer_func1('h1')
call2_func = outer_func1('p')

call1_func()
call2_func()






