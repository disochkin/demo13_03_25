from Entities import Order


class OrderRepo:
    __orders = [Order]

    def create(self, order):
        self.__orders.append(order)

    def update(self, id, is_approved, status):
        exist_order = next((item for item in self.__orders if item["id"] == id), None)
        if exist_order is None:
            raise ValueError(f"Заявка с id {id} не найдена.")
        if exist_order.status != status:
            exist_order.Status = status
        if exist_order.is_approved != is_approved:
            exist_order.is_approved = is_approved

    def delete_order(self, id):
        order_to_delete = next((item for item in self.__orders if item["id"] == id), None)
        if order_to_delete is None:
            raise ValueError(f"Заявка с id {id} не найдена.")
        self.__orders.remove(order_to_delete)

    def delete_old_orders(self):
        old_orders = next((item for item in self.__orders if item["id"] == id), None)
        if old_orders is not None:
            self.__orders = [item for item in self.__orders if item not in old_orders]