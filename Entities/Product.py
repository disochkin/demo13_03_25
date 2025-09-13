from datetime import date
from enum import Enum
from xmlrpc.client import DateTime

from Entities.BaseEntity import BaseEntity


class ProductTypeEnum(Enum):
    LIVING = "Гостиные",
    HALL= "Прихожие",
    UPFURNITURE = "МягкаяМебель",
    BED = "Кровати",
    CLOSET = "Шкафы",
    DRESSER = "Комоды"


class Size:
    height: float
    length: float
    width: float

class Product(BaseEntity):
    article: str
    type: ProductTypeEnum
    packageSize: Size
    brutto: float
    netto: float
    base_price: float
    work_shop_name: str
    product_people_count: int
    production_delay_time: float
    quality_certificate: str
    standart_number: str
    name: str
    description: str
    image: str
    price: float
    min_price: float
    production_date: date
    count: int
    # вероятно должно быть приватным
    # public double Sum => Price * Count;
