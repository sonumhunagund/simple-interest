from simple_interest import simple_interest

def test_simple_interest():
    assert simple_interest(1000, 5, 2) == 100

def test_zero_rate():
    assert simple_interest(1000, 0, 2) == 0

def test_zero_time():
    assert simple_interest(1000, 5, 0) == 0

def test_another_value():
    assert simple_interest(2000, 10, 3) == 600