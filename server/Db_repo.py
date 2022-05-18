from Customer import Customer


class DbRepo:
    def __init__(self, local_session):
        self.local_session = local_session

    def get_customer_by_id(self, id_to_get):
        return self.local_session.query(Customer).get(id_to_get).all()

    def get_all_customers(self):
        return self.local_session.query(Customer).all()

    def add(self, customer):
        self.local_session.add(customer)
        self.local_session.commit()

    def update_by_column_value(self, table_class, column_name, value, data):
        self.local_session.query(table_class).filter(column_name == value).update(data)
        self.local_session.commit()

    def add_all(self, rows_list):
        self.local_session.add_all(rows_list)
        self.local_session.commit()

    def delete_customer(self, customer):
        self.local_session.query(Customer).filter(Customer.id == customer.id).delete(synchronize_session=False)
        self.local_session.commit()

    def delete_customer_by_id(self, id_to_remove):
        self.local_session.query(Customer).filter(Customer.id == id_to_remove).delete(synchronize_session=False)
        self.local_session.commit()

    def put_by_id(self, id_to_update, data):
        exist_object = self.local_session.query(Customer).filter(Customer.id == id_to_update)
        if not exist_object:
            self.local_session.add(exist_object)
        exist_object.update(data)
        self.local_session.commit()

    def patch_by_id(self, id_column_name, id_to_update, data):
        exist_object = self.local_session.query(Customer).filter(id_column_name == id_to_update)
        if not exist_object:
            return
        exist_object.update(data)
        self.local_session.commit()

    def drop_all_tables(self):
        self.local_session.execute('drop TABLE customers CASCADE')
        self.local_session.commit()

    def reset_db(self):
        self.add_all([Customer(name='Mor', address='Yavne'),
                      Customer(name='Yuli', address='Tel-aviv'),
                      Customer(name='sharon', address='Rishon-Le-Zion'),
                      Customer(name='Roi', address='Bat-Yam'),
                      Customer(name='Adi', address='Haifa')])

