import allure
import pytest

from schemas.company import CompanyResponse

pytestmark = [pytest.mark.asyncio]


@allure.feature('Data model')
@allure.story('Company info validation')
@allure.label('layer', 'unit')
class CompanyValidationTestCase:
    @allure.title('Statement is valid')
    @pytest.mark.parametrize(
        'company',
        (
            {
                'title': 'The big company',
                'industry': 'Regional Banks',
                'sector': 'Finance',
            },
        ),
    )
    async def test_success(self, company):
        assert CompanyResponse(**company)

    @allure.title('An error occurred during validation')
    @pytest.mark.parametrize(
        'company',
        (
            {'title': ''},
            {'title': 'The big company', 'industry': 'a', 'sector': 'Finance'},
            {'title': 'The big company', 'industry': 'Regional Banks', 'sector': 'a'},
        ),
    )
    async def test_failed(self, company):
        with pytest.raises(ValueError):
            CompanyResponse(**company)
