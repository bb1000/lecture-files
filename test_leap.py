from leap import is_leap_year


def test_leap_year():
    assert is_leap_year(2000) == True
    assert is_leap_year(1999) == False
    assert is_leap_year(1998) == False
    assert is_leap_year(1996) == True
    assert is_leap_year(1900) == False
    assert is_leap_year(1800) == False
    assert is_leap_year(1600) == True
