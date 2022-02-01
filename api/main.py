from calendar import c
from fastapi import FastAPI

from api.views.purchase_views import purchase_router
from api.views.customer_view import customer_router


app = FastAPI(openapi_url="/openapi.json",
              title="Customer purchasing app",
              description="Test application, no auth.",
              version="1",)

app.router.prefix = "/api/v1"

app.include_router(purchase_router, prefix="/purchases")
app.include_router(customer_router, prefix="/customers")
