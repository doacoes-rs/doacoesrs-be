import datetime
import uuid
import time
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class ItemType(str, Enum):
    ALIMENTOS = "ALIMENTOS"
    ROUPAS = "ROUPAS"
    REMEDIOS = "REMEDIOS"
    HIGIENE = "HIGIENE"
    LIMPEZA = "LIMPEZA"
    PET = "PETS"
    OUTROS = "OUTROS"


class Location(BaseModel):
    id: str = uuid.uuid4()
    name: str
    zip_code: str
    address: str
    number: str
    city: str
    state: str
    complement: Optional[str] = None
    contacts: Optional[str] = ""
    comments: Optional[str] = None
    items: Optional[List[ItemType]] = []
    expiration_date: Optional[int] = int(time.time())


class Contact(BaseModel):
    name: str
    phone_number: str
