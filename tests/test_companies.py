import pytest

from models.company import Company


class CompanyValidationTestCase:
    @pytest.mark.parametrize(
        'ratio',
        ({'title': 'P', 'industry': 'Regional Banks', 'sector': 'Finance'},),
    )
    def test_success(self, ratio):
        assert Company(**ratio)

    @pytest.mark.parametrize(
        'ratio',
        (
            {'title': ''},
            {'title': 'P', 'industry': 'a', 'sector': 'Finance'},
            {'title': 'P', 'industry': 'Regional Banks', 'sector': 'a'},
        ),
    )
    def test_failed(self, ratio):
        with pytest.raises(ValueError):
            Company(**ratio)
