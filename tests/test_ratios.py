import pytest

from models.company import Ratio


class QuarterValidationTestCase:
    @pytest.mark.parametrize(
        'ratio',
        (
            {'title': 'P/E', 'quarter': '1999Q1', 'value': 0},
            {'title': 'P/E', 'quarter': '1999Q2', 'value': 0},
            {'title': 'P/E', 'quarter': '1999Q3', 'value': 0},
            {'title': 'P/E', 'quarter': '1999Q4', 'value': 0},
        ),
    )
    def test_success(self, ratio):
        assert Ratio(**ratio)

    @pytest.mark.parametrize(
        'ratio',
        (
            {'title': 'P/E', 'quarter': '', 'value': 0},
            {'title': 'P/E', 'quarter': '1999', 'value': 0},
            {'title': 'P/E', 'quarter': '1999Q0', 'value': 0},
            {'title': 'P/E', 'quarter': '1999Q5', 'value': 0},
            {'title': 'P/E', 'quarter': '19992Q1', 'value': 0},
            {'title': 'P/E', 'quarter': '1999Q1 1999Q1', 'value': 0},
        ),
    )
    def test_failed(self, ratio):
        with pytest.raises(ValueError):
            Ratio(**ratio)
