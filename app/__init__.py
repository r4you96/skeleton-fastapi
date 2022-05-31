from fastapi import FastAPI

from app.router import ok_response, ResponseModel


def create_app():
    app = FastAPI()

    @app.get('/health')
    def health_check():
        return

    @app.post('/forms')
    def post_form():

        return ok_response

    return app
