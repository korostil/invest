import allure
import pytest

from schemas.company import Company

pytestmark = [pytest.mark.asyncio]


@allure.feature('Data model')
@allure.story('Company info validation')
@allure.label('layer', 'unit')
class CompanyValidationTestCase:
    @allure.title('Statement is valid')
    @pytest.mark.parametrize(
        'ratio', ({'title': 'P', 'industry': 'Regional Banks', 'sector': 'Finance'},)
    )
    async def test_success(self, ratio):
        assert Company(**ratio)

    @allure.title('An error occurred during validation')
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
