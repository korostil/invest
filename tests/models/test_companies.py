import allure
import pytest

from models.company import Company

pytestmark = [pytest.mark.asyncio]


@allure.feature('Модель данных')
@allure.story('Валидация данных компании')
@allure.label('layer', 'unit')
class CompanyValidationTestCase:
    @allure.title('Валидация прошла успешно')
    @pytest.mark.parametrize(
        'ratio', ({'title': 'P', 'industry': 'Regional Banks', 'sector': 'Finance'},)
    )
    async def test_success(self, ratio):
        assert Company(**ratio)

    @allure.title('При валидации возникли ошибки')
    @pytest.mark.parametrize(
        'ratio',
        (
            {'title': ''},
            {'title': 'P', 'industry': 'a', 'sector': 'Finance'},
            {'title': 'P', 'industry': 'Regional Banks', 'sector': 'a'},
        ),
    )
    async def test_failed(self, ratio):
        with pytest.raises(ValueError):
            Company(**ratio)
