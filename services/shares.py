from models.share import Share
from schemas.share import ShareCreate, ShareUpdate
from services.crud_base import CRUDBase


class CRUDShare(CRUDBase[Share, ShareCreate, ShareUpdate]):
    ...


share = CRUDShare(Share)
