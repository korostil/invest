import allure
import pytest

from schemas.company import FinancialStatement

pytestmark = [pytest.mark.asyncio]


@allure.feature('Data model')
@allure.story('Financial statement validation')
@allure.label('layer', 'unit')
class QuarterValidationTestCase:
    @allure.title('Statement is valid')
    @pytest.mark.parametrize(
        'statement',
        (
            {'code': '1', 'quarter': '1999Q1', 'value': 0},
            {'code': '1', 'quarter': '1999Q2', 'value': 0},
            {'code': '1', 'quarter': '1999Q3', 'value': 0},
            {'code': '1', 'quarter': '1999Q4', 'value': 0},
        ),
    )
    async def test_success(self, statement):
        assert FinancialStatement(**statement)

    @allure.title('An error occurred during validation')
    @pytest.mark.parametrize(
        'statement',
        (
            {'code': '1', 'quarter': '', 'value': 0},
            {'code': '1', 'quarter': '1999', 'value': 0},
            {'code': '1', 'quarter': '1999Q0', 'value': 0},
            {'code': '1', 'quarter': '1999Q5', 'value': 0},
            {'code': '1', 'quarter': '19992Q1', 'value': 0},
            {'code': '1', 'quarter': '1999Q1 1999Q1', 'value': 0},
        ),
    )
    async def test_failed(self, statement):
        with pytest.raises(ValueError):
            FinancialStatement(**statement)
