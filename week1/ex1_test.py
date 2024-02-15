import code_to_edit as student_code



def test_hi_my_name_is():
    assert len(student_code.hi_my_name_is())  > 1 

def test_length_of_string_test1():
    assert student_code.length_of_string("Hi") ==2

def test_length_of_string_test2():
    assert student_code.length_of_string("") ==0
    
def test_length_of_string_test3():
    assert student_code.length_of_string("Hello this is a large string") ==28

def test_two_numbers_equal_test1():
    assert student_code.two_numbers_equal(2,2)

def test_two_numbers_equal_test2():
    assert student_code.two_numbers_equal(-2,2)==False

def test_two_numbers_equal_test3():
    assert student_code.two_numbers_equal(3,3)==True
