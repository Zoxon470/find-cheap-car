from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from database.config import get_db
from services.car import BrandService

templates = Jinja2Templates(directory="templates")


router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(request: Request, db=Depends(get_db)):
    brands = await BrandService(db).get_brands()
    return templates.TemplateResponse("index.html",
        context={"request": request, "brands": brands}
    )
