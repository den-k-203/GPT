from typing import List, Optional
from pydantic import BaseModel

class DestructionObject(BaseModel):
    title: str
    position: List[float]
    postName: str
    address: str
    typeInfrastructure: str
    area: float
    imgPath: str
    description: str
    percentageOfDestruction: str
    dateOfDestruction: str
    dateOfRecovery: str
    typeDestruction: str
    countVictims: int
    whatDestroyed: str
    areaName: str
    neighborhood: str
    stateDestruction: str
    _id: Optional[str]

    def __str__(self) -> str:
        return (
            f"Об'єктРуйнації("
            f"Тип інфраструктури='{self.typeInfrastructure}', "
            f"Відсоток руйнації='{self.percentageOfDestruction}%', "
            f"Дата руйнації='{self.dateOfDestruction}', "
            f"Дата відновлення='{self.dateOfRecovery}', "
            f"Тип руйнації='{self.typeDestruction}', "
            f"Кількість жертв={self.countVictims}, "
            f"Зброя якою зруйновано='{self.whatDestroyed}', "
            f"Район='{self.neighborhood}', "
            f"Стан руйнації='{self.stateDestruction}'"
            f")"
        )

    def to_json(self) -> str:
        return self.json()