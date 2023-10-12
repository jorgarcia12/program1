import pytest 
from funciones_tp5 import *

@pytest.mark.parametrize("input_dni, res",
    [("1234567",True),
    ("123456",False),
    ("12345678",True),
    ])
def test_dni(input_dni, res):
    assert dni(input_dni) == res