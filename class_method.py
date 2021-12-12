class Employee:
    raise_amount = 1.1  # 연봉 인상율 클래스 변수

    def __init__(self, first, last, pay):
        self.fst = first
        self.lst = last
        self.pay = pay

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def full_name(slf):
        return '{} {}'.format(slf.fst, slf.lst)

    def get_pay(sgp):
        return '현재 "{}"의 연봉은 "{}"입니다.'.format(sgp.full_name(), sgp.pay)

    # 1 클래스 메소드 데코레이터를 사용하여 클래스 메소드 정의
    @classmethod
    def change_raise_amount(cls, amount):
         # 인상율이 "1" 보다 작으면 재입력 요청
        while amount < 1:
            print('[경고] 인상율은 "1"보다 작을 수 없습니다.')
            amount = input('[입력] 인상율을 다시 입력하여 주십시오.\n=> ')
            amount = float(amount)
        cls.raise_amount = amount
        print('인상율 "{}"가 적용 되었습니다.'.format(amount))


emp_1 = Employee('Sanghee', 'Lee', 50000)
emp_2 = Employee('Minjung', 'Kim', 60000)

# 연봉 인상 전
print(emp_1.get_pay())
print(emp_2.get_pay())

# 연봉 인상율 변경
Employee.change_raise_amount(1.5)

# 연봉 인상
emp_1.apply_raise()
emp_2.apply_raise()

# 연봉 인상 후
print(emp_1.get_pay())
print(emp_2.get_pay())

class person:
    def __init__(self, first, last, pay):
        self.fst = first
        self.lst = last
        self.pay = pay
        #self.rate = rate
    def student(self, b):
        print(b + ' is string')
        print(self.fst)

    @classmethod
    def change_raise_amount(cra, amount):
        print(str(amount) + ' is input')
        print(amount * 2)
        cra.rate = amount
    def new_rate(self):
        return self.rate * self.rate

    def __str__(self):
        return 'str method'
    def __repr__(self):
        return 'repr method'


p = person('james', 'lee', 1000)
p.student('j')
#print(p.rate)
p.change_raise_amount(2.8)
#print(p.rate)
p.new_rate()
print(p.new_rate())
print(p.__str__())
print(str(p))
print(p)

class oper:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __sub__(self, oth):
        return self.a - oth.a, self.b - oth.b

    def __add__(self, oth):
        return self.a + oth.a, self.b + oth.b

o = oper
o1 = o(1,2)
o2 = o(10,20)
print(o2 + o1)
print(o1.a - o2.a)
print('---------------')



def decorator_function(original_function):
    def wrapper_function():
        print('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
        return original_function()

    return wrapper_function

def display_2():
    print('display_2 함수가 실행됐습니다.')

display_2 = decorator_function(display_2)  # 2
print(type(display_2))
display_2()
print('*************')


def decorator_function(original_function):

    print('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
    return original_function()

def display_1():
    print('display_1 함수가 실행됐습니다.')

display_1 = decorator_function(display_1)  # 1
print(type(display_1))
#display_1()
print('****************************')
def outer_function():
    #global a
    a = 20
    def inner_function():
        global a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)

a = 10
outer_function()
print('a =', a)
print('****************************')
print('--------')

class Employee:
    raise_amount = 1.1  # 연봉 인상율 클래스 변수

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def get_pay(self):
        return '현재 "{}"의 연봉은 "{}"입니다.'.format(self.full_name(), self.pay)

    # 1 클래스 메소드 데코레이터를 사용하여 클래스 메소드 정의
    @classmethod
    def change_raise_amount(self, amount):
        # 2 인상율이 "1" 보다 작으면 재입력 요청
        #while amount < 1:
        #   print('[경고] 인상율은 "1"보다 작을 수 없습니다.')
        #    amount = input('[입력] 인상율을 다시 입력하여 주십시오.\n=> ')
        #   amount = float(amount)
        self.raise_amount = amount
        print('인상율 "{}"가 적용 되었습니다.'.format(amount))


emp_1 = Employee('Sanghee', 'Lee', 10000)
emp_2 = Employee('Minjung', 'Kim', 100000)

# 연봉 인상 전
print(emp_1.get_pay())
print(emp_2.get_pay())

# 연봉 인상율 변경
Employee.change_raise_amount(2)

# 연봉 인상
emp_1.apply_raise()
emp_2.apply_raise()

# 연봉 인상 후
print(emp_1.get_pay())
print(emp_2.get_pay())


'''
class Person:
    def __init__(self, year, month, day, sex):
        self.year = year
        self.month = month
        self.day = day
        self.sex = sex

    def __str__(self):
        return '{}년 {}월 {}일생 {}입니다.'.format(self.year, self.month, self.day, self.sex)

ssn_1 = '900829-1034356'
ssn_2 = '051224-4061569'

def ssn_parser(ssn):
    front, back = ssn.split('-')
    sex = back[0]

    if sex == '1' or sex == '2':
        year = '19' + front[:2]
    else:
        year = '20' + front[:2]

    if (int(sex) % 2) == 0:
        sex = '여성'
    else:
        sex = '남성'

    month = front[2:4]
    day = front[4:6]

    return year, month, day, sex

print(ssn_parser(ssn_1))
print(*ssn_parser(ssn_1))

p1 = Person(*ssn_parser(ssn_1))
print(p1)
print('--------------------------')
print()

class Person:
    def __init__(self, year, month, day, sex):
        self.year = year
        self.month = month
        self.day = day
        self.sex = sex

    def __str__(self):
        return '{}년 {}월 {}일생 {}입니다.'.format(self.year, self.month, self.day, self.sex)

    def p_f(self):
        return self.a

    @classmethod
    def g(cls, ssn, age):
        front, back = ssn.split('-')
        sex = back[0]

        if sex == '1' or sex == '2':
            year = '19' + front[:2]
        else:
            year = '20' + front[:2]
        if (int(sex) % 2) == 0:
            sex = '여성'
        else:
            sex = '남성'

        month = front[2:4]
        day = front[4:6]

        cls.a = age

        return cls(year, month, day, sex)

ssn_1 = '900829-1034356'
p1 = Person.g(ssn_1, 10)
print(p1)
print(p1.p_f())

print('++++++++++++++++++++++')
print()
import datetime
class St:
    @staticmethod
    def is_work_day(day):
        # weekday() 함수의 리턴값은
        # 월: 0, 화: 1, 수: 2, 목: 3, 금: 4, 토: 5, 일: 6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

d = St
my_date = datetime.date(2016, 10, 9)
d.is_work_day(my_date)'''















