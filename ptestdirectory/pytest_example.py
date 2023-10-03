import pytest

#
# def func(x):
#     return x+5
# def test_method1():
#     assert func(3)==8
#
# def test_method2():
#     assert func(3)==9
#
# def test_method3():
#     assert func(3)==9


#USING MARKER  --command-- pytest pytest_example.py -m "focus" (m is for marker and for self created marker write inside ""


# def func(x):
#     return x+5
#
# def test_method1():
#     assert func(3)==8
#
# @pytest.mark.xfail
# def test_method2():
#     assert func(3) == 9
#
# @pytest.mark.skip
# def test_method3():
#     assert func(3) == 8
#
# @pytest.mark.focus --called as decorator selects one and deselects every other--
# def test_method4():
#     assert func(3) == 8


#fixture --command-- pytest pytest_example.py
#fixture function runs at first

# @pytest.fixture()
# def func():
#     x=10
#     y=20
#     return [x,y]
#
# def test_method1(func):
#     assert func[0]==10
#
# def test_method2(func):
#     assert func[1]==10




#PARAMETERIZED MARKER --command-- pytest pytest_example.py

#
# @pytest.mark.parametrize("a,b,c",[(10,20,200),(10,20,400)])
#
# def test_method(a,b,c):
#     assert a*b==c

