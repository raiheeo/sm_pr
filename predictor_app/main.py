from fastapi import FastAPI
from predictor_app.api import auth, mobile
import uvicorn


predictor_app = FastAPI(title='SmartPhone Predictor')

predictor_app.include_router(auth.auth_router)
predictor_app.include_router(mobile.mobile_router)

if __name__ == '__main__':
    uvicorn.run(predictor_app, host='127.0.0.1', port=8000)

