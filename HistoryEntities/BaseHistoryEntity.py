from datetime import datetime

from Entities.BaseEntity import BaseEntity


class BaseHistoryEntity(BaseEntity):
    time_stamp: datetime

    def __init__(self):
        self.time_stamp = datetime.now()

