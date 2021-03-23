import allure
import pytest

from models.company import FinancialStatement


@allure.feature('Модель данных')
@allure.story('Валидация данных финансового показателя')
@allure.label('layer', 'unit')
class QuarterValidationTestCase:
    @allure.title('Валидация прошла успешно')
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        'statement',
        (
            {'title': 'Cash and cash equivalents', 'quarter': '1999Q1', 'value': 0},
            {'title': 'Cash and cash equivalents', 'quarter': '1999Q2', 'value': 0},
            {'title': 'Cash and cash equivalents', 'quarter': '1999Q3', 'value': 0},
            {'title': 'Cash and cash equivalents', 'quarter': '1999Q4', 'value': 0},
        ),
    )
    async def test_success(self, statement):
        assert FinancialStatement(**statement)

    @allure.title('При валидации возникли ошибки')
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        'statement',
        (
            {'title': 'Cash and cash equivalents', 'quarter': '', 'value': 0},
            {'title': 'Cash and cash equivalents', 'quarter': '1999', 'value': 0},
            {'title': 'Cash and cash equivalents', 'quarter': '1999Q0', 'value': 0},
            {'title': 'Cash and cash equivalents', 'quarter': '1999Q5', 'value': 0},
            {'title': 'Cash and cash equivalents', 'quarter': '19992Q1', 'value': 0},
            {
                'title': 'Cash and cash equivalents',
                'quarter': '1999Q1 1999Q1',
                'value': 0,
            },
        ),
    )
    async def test_failed(self, statement):
        with pytest.raises(ValueError):
            FinancialStatement(**statement)
