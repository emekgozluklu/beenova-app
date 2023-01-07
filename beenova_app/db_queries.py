from beenova_app.db import get_db


class DBOperator:
    def __init__(self):
        self.db = get_db()

    def create_employee(self, first_name, last_name, created_by, username, email, company, phone_number=None,
                        is_admin=0, is_company_admin=0, is_activated=0):
        query = """ 
            INSERT INTO employee (first_name, last_name, username, email, company, phone_number, is_admin, 
                                  is_company_admin, is_activated, created_by)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """

        self.db.execute(query, (first_name, last_name, username, email, company, phone_number, is_admin,
                                is_company_admin, is_activated, created_by))
        self.db.commit()

    def update_employee(self, employee_id, first_name=None, last_name=None, created_by=None, username=None, email=None,
                        company=None, phone_number=None, is_admin=None, is_company_admin=None, is_activated=None):
        query = """
            UPDATE employee
            SET first_name=?, last_name=?, username=?, email=?, company=?, phone_number=?, is_admin=?,
                is_company_admin=?, is_activated=?, created_by=?
            WHERE id=?;
        """

        self.db.execute(query, (first_name, last_name, username, email, company, phone_number, is_admin,
                                is_company_admin, is_activated, created_by, employee_id))
        self.db.commit()

    def get_employee_by_id(self, employee_id):
        query = """
            SELECT * FROM employee WHERE id=?;
        """

        result = self.db.execute(query, (employee_id,)).fetchone()
        return result

    def get_employee_by_email(self, email):
        query = """
            SELECT * FROM employee WHERE email=?;
        """

        result = self.db.execute(query, (email,)).fetchone()
        return result

    def create_data_source(self, name, url, created_by, company_id):
        pass

    def create_data_usage(self, data_source, data_user, start_time, end_time, usage_amount, subscription):
        query = """
            INSERT INTO data_usage (data_source, data_user, start_time, end_time, usage_amount, subscription)
            VALUES (?, ?, ?, ?, ?, ?);
        """

        self.db.execute(query, (data_source, data_user, start_time, end_time, usage_amount, subscription))
        self.db.commit()

    def update_data_usage(self, data_usage_id, data_source=None, data_user=None, start_time=None, end_time=None,
                          usage_amount=None, subscription=None):
        query = """
            UPDATE data_usage
            SET data_source=?, data_user=?, start_time=?, end_time=?, usage_amount=?, subscription=?
            WHERE id=?;
        """

        self.db.execute(query, (data_source, data_user, start_time, end_time,
                                usage_amount, subscription, data_usage_id))
        self.db.commit()

    def create_subscription(self, subscriber, data_source, request, subscription_started, subscription_ended,
                            subscription_type, status):
        query = """
            INSERT INTO subscription (subscriber, data_source, request, subscription_started, subscription_ended,
                                     subscription_type, status)
            VALUES (?, ?, ?, ?, ?, ?, ?);
        """

        self.db.execute(query, (subscriber, data_source, request, subscription_started, subscription_ended,
                                subscription_type, status))
        self.db.commit()

    def create_request(self, requester, data_source, request, request_type, status):
        query = """
            INSERT INTO request (requester, data_source, request_message, date_updated, status)
            VALUES (?, ?, ?, ?, ?);
        """

        self.db.execute(query, (requester, data_source, request, request_type, status))
        self.db.commit()

    def register_employee(self, first_name, last_name, email, phone_number="", is_company_admin=0, is_admin=0,
                          is_activated=0, created_by=0):
        username = email.split("@")[0]
        query = """
            INSERT INTO employee (
            first_name, last_name, email, phone_number, is_company_admin, is_admin, is_activated, username, created_by
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """

        self.db.execute(query, (first_name, last_name, email, phone_number, is_company_admin, is_admin, is_activated,
                                username, created_by))
        self.db.commit()

    def register_company(self, name, admin_id):
        query = """
            INSERT INTO company (name, admin_id)
            VALUES (?, ?);
        """

        self.db.execute(query, (name, admin_id))
        self.db.commit()

    def get_employee_id_by_email(self, email):
        query = """
            SELECT id FROM employee WHERE email=?;
        """

        result = self.db.execute(query, (email,)).fetchone()
        return result

    def delete_employee_by_id(self, company_admin_id):
        query = """
            DELETE FROM employee WHERE id=?;
        """

        self.db.execute(query, (company_admin_id,))
        self.db.commit()

