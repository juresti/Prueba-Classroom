import pytest
import prueba
def test_impares():
    assert prueba.impares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5
    assert prueba.impares([2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
