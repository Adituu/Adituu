from fastapi import APIRouter, UploadFile, File, HTTPException, status
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get('/', response_model=HTMLResponse)
async def route_index():
    pass
