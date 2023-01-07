from sqlalchemy import create_engine
from beenova_app.db import get_db


class DBOperator:

    def __init__(self):
        # engine = create_engine(current_app.config.get("DATABASE"), echo=True)
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

    def get_employee_by_id(self):
        pass

    def get_employee_by_email(self):
        pass

    def create_company(self):
        pass

    def create_data_source(self):
        pass

    def create_request(self):
        pass
