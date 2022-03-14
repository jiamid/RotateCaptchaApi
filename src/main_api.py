from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from uvicorn import run

from api.rotate_angle import router


API_HEADERS = '/rotate_captcha_api'

app = FastAPI(title='Rotate Captcha Api', openapi_url=f'{API_HEADERS}/openapi.json')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(router)

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080)
