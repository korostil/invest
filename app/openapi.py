from typing import Any, Optional

from fastapi.openapi.utils import get_openapi


def openapi_schema() -> Optional[dict[str, Any]]:
    from main import app

    openapi_schema = get_openapi(
        title='Invest helper',
        version='1.0',
        description='Designed to help invest',
        routes=app.routes,
        tags=[
            {'name': 'companies', 'description': 'Manage companies'},
            {'name': 'shares', 'description': 'Manage shares'},
        ],
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema
