import sys
from pathlib import Path
codesetup_path = Path.home()/"Desktop"/"codesetup"
sys.path.insert(0, str(codesetup_path))
from function import addition # type: ignore

def test_addition() -> None:
    assert addition(1,2) == 3

def test_addition_2() -> None:
    assert addition(3,2) == 5    