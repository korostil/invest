from models.company import Company
from schemas.company import CompanyCreate, CompanyUpdate
from services.crud_base import CRUDBase


class CRUDCompany(CRUDBase[Company, CompanyCreate, CompanyUpdate]):
    ...


company = CRUDCompany(Company)
