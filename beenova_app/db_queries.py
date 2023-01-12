from beenova_app.db import get_db


class DBOperator:
    def __init__(self):
        self.db = get_db()

    # helpers
    def get_data_source_type_name(self, data_source_type_id):
        query = """
            SELECT name FROM data_source_type WHERE id=?;
        """

        result = self.db.execute(query, (data_source_type_id,)).fetchone()
        return result["name"]

    # employee operations
    def create_employee(self, first_name, last_name, created_by, username, email, company, password_hash,
                        phone_number=None, is_admin=0, is_company_admin=0, is_activated=0):
        query = """ 
            INSERT INTO employee (first_name, last_name, username, email, company, password_hash, phone_number, 
                                is_admin, is_company_admin, is_activated, created_by)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """

        self.db.execute(query, (first_name, last_name, username, email, company, password_hash, phone_number, is_admin,
                                is_company_admin, is_activated, created_by))
        self.db.commit()

    def update_employee_with_id(self, employee_id, **kwargs):
        employee = self.get_employee_by_id(employee_id)
        attrs = ["first_name", "last_name", "username", "email", "company", "phone_number", "is_admin",
                 "is_company_admin", "is_activated"]
        updated_employee = dict()
        for k in attrs:
            if k in kwargs:
                updated_employee[k] = kwargs[k]
            else:
                updated_employee[k] = employee[k]

        query = """
            UPDATE employee
            SET first_name=?, last_name=?, username=?, email=?, company=?, phone_number=?, is_admin=?,
                is_company_admin=?, is_activated=?
            WHERE id=?;
        """

        self.db.execute(query, tuple(updated_employee.values()) + (employee_id,))
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

    def get_employee_by_username(self, username):
        query = """
            SELECT * FROM employee WHERE username=?;
        """

        result = self.db.execute(query, (username,)).fetchone()
        return result

    def delete_employee_by_id(self, company_admin_id):
        query = """
            DELETE FROM employee WHERE id=?;
        """

        self.db.execute(query, (company_admin_id,))
        self.db.commit()

    # company operations
    def register_company(self, name, admin_id):
        query = """
            INSERT INTO company (name, admin_id)
            VALUES (?, ?);
        """

        self.db.execute(query, (name, admin_id))
        self.db.commit()

    def get_company_by_name(self, company_name):
        query = """
            SELECT * FROM company WHERE name=?;
        """

        result = self.db.execute(query, (company_name,)).fetchone()
        return result

    def get_data_source_by_id(self):
        query = """
            SELECT * FROM data_source WHERE id=?;
        """

        result = self.db.execute(query, (id,)).fetchone()
        return result

    def get_data_source_types(self):
        # get data source types from db
        query = """
            SELECT * FROM data_source_type;
        """

        result = self.db.execute(query).fetchall()
        return [(res["id"], res["name"]) for res in result]

    def get_employees_of_company(self, company_id):
        query = """
            SELECT * FROM employee WHERE company=?;
        """

        result = self.db.execute(query, str(company_id)).fetchall()
        return [(res["id"], res["first_name"] + res["last_name"]) for res in result]

    # method signatures for other operations
    def create_data_source(self, name, url, created_by, company_id):
        pass

    def get_data_sources(self):

        query = """
            SELECT * FROM data_source;
        """

        result = self.db.execute(query).fetchall()
        return [(res["id"], res["title"]) for res in result]
        

    def create_data_usage(self, data_source, data_user, start_time, end_time, usage_amount, subscription):
        pass

    def update_data_usage(self, data_usage_id, data_source=None, data_user=None, start_time=None, end_time=None,
                          usage_amount=None, subscription=None):
        pass

    def create_subscription(self, subscriber, data_source, request, subscription_started, subscription_ended,
                            subscription_type, status):
        pass

    def create_request(self, requester, data_source, request_message):
        
        query = """
            INSERT INTO request (requester, data_source, request_message, date_updated, status)
            VALUES (?, ?, ?, DATETIME('NOW'), ?);
        """

        self.db.execute(query, (requester, data_source, request_message, 0))
        self.db.commit()

    def create_request_demo(self, first_name, last_name, email, company, phone_number, message):

        query = """
            INSERT INTO demo_request (first_name, last_name, email, company, phone_number, message)
            VALUES (?, ?, ?, ?, ?, ?);
        """

        self.db.execute(query, (first_name, last_name, email, company, phone_number, message))
        self.db.commit()

    def get_data_sources_of_company_for_dashboard_table(self, company_id):
        # join data sources and employee tables and get data sources of company
        query = """
            SELECT ds.id ds_id, ds.title title, ds.type_id type, e.first_name || ' ' || e.last_name maintainer, ds.created_at created_at
             FROM data_source ds join employee e on ds.responsible_employee = e.id where e.company = ?;
        """

        result = self.db.execute(query, (str(company_id),)).fetchall()
        return [(
                res["title"],
                self.get_data_source_type_name(res["type"]),
                len(self.get_active_users_of_data_source(res["ds_id"])),
                res["maintainer"],
                res["created_at"]
                ) for res in result]

    def get_active_users_of_data_source(self, data_source_id):
        query = """
            SELECT * FROM subscription WHERE data_source=? AND status=?;
        """
        print(data_source_id)

        result = self.db.execute(query, (data_source_id, '1')).fetchall()
        return list(result)



