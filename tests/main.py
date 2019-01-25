import builtins
import pytest
from unittest.mock import patch
from SavingCalc.main import get_monthly_savings, get_months, get_product_cost, get_savings

def test_get_savings():
    with patch.object(builtins, 'input', return_value="1"):
        assert get_savings() == 1.0

def test_get_savings_fail():
    with patch.object(builtins, 'input', return_value="a"):
        with pytest.raises(Exception):
            get_savings()

def test_get_monthly_savings():
    with patch.object(builtins, 'input', return_value="1"):
        assert get_monthly_savings() == 1.0

def test_get_monthly_savings_fail():
    with patch.object(builtins, 'input', return_value="a"):
        with pytest.raises(Exception):
            get_monthly_savings()

def test_get_product_cost():
    with patch.object(builtins, 'input', return_value="1"):
        assert get_product_cost() == 1.0

def test_get_product_cost_fail():
    with patch.object(builtins, 'input', return_value="a"):
        with pytest.raises(Exception):
            get_product_cost()

def test_get_months():
    assert get_months(5000, 5000, 6000) == 1.0

def test_get_months_fail():
    with pytest.raises(Exception):
        get_months("a", "b", "c")


