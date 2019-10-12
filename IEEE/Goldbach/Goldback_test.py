import pytest
from Goldbach import find_goldbach, find_primes

test_data = [
    65,
    101,
    501,
    907,
    853,
    971,
    25937,
    705
]


@pytest.mark.parametrize('number', test_data)
def test_find_goldbach(number):
    primes = find_primes(number)
    sol = find_goldbach(number, primes)
    assert sum(map(int, sol.split())) == number
