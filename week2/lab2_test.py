import lab2Task as student_code
def test_total_price_test1():
    assert round(student_code.total_price(10,0.13),2)==round(11.3,2)

def test_total_price_test2():
    assert round(student_code.total_price(10,1.0),2)==round(20.0,2)

def test_divisible_by_test1():
    assert student_code.divisible_by(10,3)==False

def test_divisible_by_test2():
    assert student_code.divisible_by(21,3)==True

def test_basic_calculator_test1():
    assert student_code.basic_calculator(20,3,"+")==23

def test_basic_calculator_test2():
    assert student_code.basic_calculator(20,3,"-")==17

def test_basic_calculator_test3():
    assert student_code.basic_calculator(20,3,"*")==60

def test_sum_of_even_test1():
    assert student_code.sum_of_even([0,10,22,21,13,31,43,53,2])==34

def test_sum_of_even_test2():
    assert student_code.sum_of_even([10,23,"Hi",44])=="invalid"

def test_reverse_string_test1():
    assert student_code.reverse_string("hello")=="olleh"

def test_reverse_string_test2():
    assert student_code.reverse_string(123)=="321"

def test_diamond_string_test1():
    assert student_code.diamond_string(5) in ["  *\n ***\n*****\n ***\n  *","  *\n ***\n*****\n ***\n  *\n",
            "  *  \n *** \n*****\n *** \n  *  \n","  *  \n *** \n*****\n *** \n  *  "]

def test_diamond_string_test2():
    assert student_code.diamond_string(9) in ["    *    \n   ***   \n  *****  \n ******* \n*********\n ******* \n  *****  \n   ***   \n    *    \n" ,
             "    *\n   ***\n  *****\n *******\n*********\n *******\n  *****\n   ***\n    *\n",
             "    *    \n   ***   \n  *****  \n ******* \n*********\n ******* \n  *****  \n   ***   \n    *    " ,
             "    *\n   ***\n  *****\n *******\n*********\n *******\n  *****\n   ***\n    *"]

def test_diamond_string_test3():
    assert student_code.diamond_string(6) ==""

def test_diamond_string_test4():
    assert student_code.diamond_string(8)==""

def test_diamond_string_test5():
    assert student_code.diamond_string(0)==""
    
def test_longest_consecutive_subarray_test1():
    assert student_code.longest_consecutive_subarray([100, 4, 200, 1, 3, 2])==4

def test_longest_consecutive_subarray_test2():
    assert student_code.longest_consecutive_subarray([])==0

def test_longest_consecutive_subarray_test3():
    assert student_code.longest_consecutive_subarray([5])==1

def test_longest_consecutive_subarray_test4():
    assert student_code.longest_consecutive_subarray([9,8,4,5,7,6,2,3])==8

