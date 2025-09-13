from enum import EnumType
from typing import List
from uuid import UUID

from Entities.BaseEntity import BaseEntity


class PartnerType(EnumType):
    IP = "Индивидуальный предприниматель",
    LLC = "Общество с ограниченной ответственностью"


class Partner(BaseEntity):
    type: PartnerType
    name: str
    org_address: str
    inn: str
    directorFullName: str
    phone: str
    email: str
    logo: str
    rate: float
    sellplaces: str
    saleSize: float
    realization_history: List


class Realization:
    id: UUID
    partnerID: int
    sum: float
