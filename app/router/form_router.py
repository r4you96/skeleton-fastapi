from fastapi import APIRouter

from app.router import ok_response
from app.model.form import Form

router = APIRouter()


@router.get('/')
async def select_form():
    return Form(name='찰찰', age=35).json()


@router.get('/')
async def post_form(form_data: Form):
    return ok_response
