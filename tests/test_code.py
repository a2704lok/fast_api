import sys
from pathlib import Path
import pytest
codesetup_path = Path.home()/"Desktop"/"codesetup"
sys.path.append(str(codesetup_path))

from function import addition # type: ignore

def test_addition() -> None:
    assert addition(1,2) == 3

def test_addition_2() -> None:
    assert addition(3,2) == 5

@pytest.mark.parametrize("num1, num2, expected",
                          [(2, 3,5),
                            (-1, 5, 4),
                            (1.5,1.4,2.9)])
def test_addition(num1: float,
                  num2: float,
                  expected: float) -> None:
    assert addition(num1,num2) == expected
