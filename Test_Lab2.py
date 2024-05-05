import LAB2
def test_find_minmax():
    result = []
    input_arr = [2,3,4,5]
    test_arr = [2,5]
    
    result = LAB2.find_min_max(input_arr)
    assert (result == test_arr)

def test_calc_average():
    result = []
    input_arr = [2,4,6,8]
    test_arr = [5]

    result = LAB2.calc_average(input_arr)
    assert (result == test_arr)

def test_calc_median():
    result = []
    input_arr = [1,2,3,4,5]
    test_arr = [3]

    result = LAB2.calc_median_temperature(input_arr)
    assert (result == test_arr)