from pydantic import BaseModel

class MaquinaCreate(BaseModel):
    hostname: str
    sistema_operacional: str
    processador: str
    memoria_ram: float
    espaco_disco: float
    endereco_ip: str
