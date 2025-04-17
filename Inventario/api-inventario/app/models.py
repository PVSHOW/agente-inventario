from sqlalchemy import Column, Integer, String, Float, DateTime, func
from .database import Base

class Maquina(Base):
    __tablename__ = "maquinas"

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String)
    sistema_operacional = Column(String)
    processador = Column(String)
    memoria_ram = Column(Float)
    espaco_disco = Column(Float)
    endereco_ip = Column(String)
    data_coleta = Column(DateTime(timezone=True), server_default=func.now())
