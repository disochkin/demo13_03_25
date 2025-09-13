class RealizationRepo:
    __realization = []
    def add(self, partnerId, realization):
        realization.PartnerId = partnerId
        self.__realization.append(realization)

    def get_sum(self, partner_id):
        return sum(item.value for item in self.__realization if item.partner_id == partner_id)

    def get(self, partnerId):
        return next((item for item in self.__realization if item.partner_id == partnerId), None)
