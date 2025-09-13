from uuid import UUID

from HistoryEntities.BaseHistoryEntity import BaseHistoryEntity


class RateChangesHistory(BaseHistoryEntity):
    partner_id: UUID
    __value: float

    def __init__(self, value):
        self.__value = value
