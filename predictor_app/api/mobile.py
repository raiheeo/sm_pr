from predictor_app.db.models import Mobile
from predictor_app.db.schema import MobileSchema
from predictor_app.db.database import SessionLocal
from sqlalchemy.orm import Session
from typing import  List
from fastapi import Depends, HTTPException, APIRouter, status
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


predictor_code_router = APIRouter(prefix='/predictor', tags=['Predictor'])

BASE_DIR = Path(__file__).resolve().parent.parent.parent

model_path = BASE_DIR / 'mobile_price_model_job.pkl'
scaler_path = BASE_DIR / 'scaler.pkl'

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#get
@predictor_code_router.get('/', response_model=List[MobileSchema])
async def mobile_list(db: Session = Depends(get_db)):
    mobile_db = db.query(Mobile).all()
    return mobile_db
#post
@predictor_code_router.post('/', response_model=MobileSchema)
async def mobile_create(mobile: MobileSchema, db: Session = Depends(get_db)):
    mobile_db = Mobile(**mobile.dict())

    db.add(mobile_db)
    db.commit()
    db.refresh(mobile_db)
    return mobile_db
#sec get
@predictor_code_router.get('/{mobile_id}', response_model=MobileSchema)
async def mobile_detail(mobile_id: int, db: Session = Depends(get_db)):
    mobile_db = db.query(Mobile).filter(Mobile.id == mobile_id).first()
    if mobile_db is None:
        raise HTTPException(status_code=404, detail='This information not found')
    return mobile_db

#put
@predictor_code_router.put('/{mobile_id}', response_model=MobileSchema)
async def mobile_update(mobile_id: int, mobile: MobileSchema, db: Session = Depends(get_db)):
    mobile_db = db.query(Mobile).filter(Mobile.id == mobile_id).first()
    if mobile_db is None:
        raise HTTPException(status_code=404, detail='This information not found')

    for mobile_key, mobile_value in mobile.dict().items():
        setattr(mobile_db, mobile_key, mobile_value)

    db.add(mobile_db)
    db.commit()
    db.refresh(mobile_db)
    return mobile_db

#rm
@predictor_code_router.delete('/{mobile_id}')
async def mobile_delete(mobile_id: int, db: Session = Depends(get_db)):
    mobile_db = db.query(Mobile).filter(Mobile.id == mobile_id).first()
    if mobile_db is None:
        raise HTTPException(status_code=404, detail='This information not found')
    db.add(mobile_db)
    db.commit()
    return {'message:' 'The mobile is deleted'}


model_columns = [
    'Battery',
    'Processor',
    'Front_Cam'
    'Rating',
    'Num_Ratings',
    'RAM',
    'ROM',
]
#th get
@predictor_code_router.post('/predict/')
async def predict_price(mobile: MobileSchema):
    input_data = {
        'Rating': mobile.Rating,
        'Battery': mobile.Battery,
        'Processor': mobile.Processor,
        'Front_Cam': mobile.Front_Cam,
        'Num_Ratings': mobile.Num_Ratings,
        'RAM': mobile.RAM,
        'ROM': mobile.ROM,
    }
    input_df = pd.DataFrame([input_data])
    scaler_dr = scaler.transform(input_df)
    predicted_price = model.predict(scaler_dr)[0]
    return {'predicted_price': round(predicted_price)}

















