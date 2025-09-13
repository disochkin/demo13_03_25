from Entities import Partner
from HistoryEntities.RateChangeHistory import RateChangesHistory


class PartnerRepository:
    __partners = [Partner]
    __rates = [RateChangesHistory]

    def create(self, partner):
        self.__partners.append(partner)

    def update_rate(self, id, value):
        exist_partner = next((item for item in self.__partners if item["id"] == id), None)
        if exist_partner is None:
            raise ValueError(f"Партнер с id {id} не найден.")
        exist_partner.Rate = value
        change_history = RateChangesHistory(value)
        self.__rates.append(change_history)

    def add(self, partnerId, realization):
        realization.partnerID = partnerId





