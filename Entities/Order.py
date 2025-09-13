from datetime import datetime
from enum import EnumType
from uuid import UUID

from Entities.BaseEntity import BaseEntity

class OrderStatusEnum(EnumType):
    Created=1,
    WaitPayment=2,
    FullPayment=3,
    Completed=4

class Order(BaseEntity):
    partner_id: UUID
    is_approved: bool #по умолч false
    date: datetime # по умолч DateTime.Now
    status: OrderStatusEnum # по умолч OrderStatusEnum.Created
    products: []


    def __init__(self,partner_id, products):
        self.partner_id = partner_id
        self.is_approved = False
        self.date = datetime.now()
        self.status = OrderStatusEnum.Created
        self.products = products

