from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Maquina
from .schemas import MaquinaCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/inventario")
def receber_dados(maquina: MaquinaCreate, db: Session = Depends(get_db)):
    nova = Maquina(**maquina.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return {"mensagem": "Dados salvos com sucesso", "id": nova.id}
