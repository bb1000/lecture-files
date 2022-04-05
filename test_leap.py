import pytest
from leap import is_leap_year


@pytest.mark.parametrize('year,result',
    [
        (2000, True),
        (1999, False),
        (1998, False),
        (1996, True),
        (1900, False),
        (1800, False),
        (1600, True),
    ]
)
def test_leap_year(year, result):
    assert is_leap_year(year) == result

