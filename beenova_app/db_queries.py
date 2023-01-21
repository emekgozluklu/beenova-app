from beenova_app.db import get_db


class DBOperator:
    def __init__(self):
        self.db = get_db()

    # employee operations
    def create_employee(self, first_name, last_name, created_by, username, email, company, password_hash,
                        phone_number=None, is_admin=0, is_company_admin=0, is_activated=0, profile_photo="default_user.jpg"):
        query = """ 
            INSERT INTO employee (first_name, last_name, username, email, company, password_hash, phone_number, 
                                is_admin, is_company_admin, is_activated, created_by)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """

        self.db.execute(query, (first_name, last_name, username, email, company, password_hash, phone_number, is_admin,
                                is_company_admin, is_activated, created_by, profile_photo))
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

    def get_employees_of_company(self, company_id):
        query = """
            SELECT * FROM employee WHERE company=?;
        """

        result = self.db.execute(query, str(company_id)).fetchall()
        return [(res["id"], " ".join([res["first_name"], res["last_name"]])) for res in result]

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

    def get_company_by_id(self, company_id):
        query = """
            SELECT * FROM company WHERE id=?;
        """

        result = self.db.execute(query, (company_id,)).fetchone()
        return result

    # data source operations

    def get_data_source_by_id(self, data_source_id):
        query = """
            SELECT * FROM data_source WHERE id=?;
        """

        result = self.db.execute(query, (str(data_source_id),)).fetchone()
        return result

    def get_data_sources(self):

        query = """
            SELECT * FROM data_source;
        """

        result = self.db.execute(query).fetchall()
        return [(res["id"], res["title"]) for res in result]

    def get_available_data_sources(self, excluded_company_id=None):
        if excluded_company_id is None:
            query = """
                SELECT * FROM 
                data_source ds join employee e join company c on ds.responsible_employee = e.id and  e.id = c.id order by ds.created_at desc;
            """

            result = self.db.execute(query).fetchall()
        else:
            query = """
                SELECT * FROM data_source ds join employee e join company c 
                on ds.responsible_employee = e.id and e.id = c.id 
                WHERE e.company!=? order by c.name, ds.created_at desc;
            """

            result = self.db.execute(query, (excluded_company_id,)).fetchall()

        return result

    def update_datasource_table_name(self, data_source_id, table_name):
        query = """
            UPDATE data_source
            SET database_table_name=?
            WHERE id=?;
        """

        self.db.execute(query, (table_name, data_source_id))
        self.db.commit()

    # data source type operations

    def create_data_source(self, title, description, is_published, type_id, data_root, is_private, subscription_fee,
                           responsible_employee, created_by):

        query = """
            INSERT INTO data_source (title, description, is_published, type_id, data_root, is_private, subscription_fee,
                                    responsible_employee, created_by)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """

        self.db.execute(query, (title, description, is_published, type_id, data_root, is_private, subscription_fee,
                                responsible_employee, created_by))
        self.db.commit()

    def get_data_source_type_name(self, data_source_type_id):
        query = """
            SELECT name FROM data_source_type WHERE id=?;
        """

        result = self.db.execute(query, (data_source_type_id,)).fetchone()
        return result["name"]

    def get_data_source_types(self):
        # get data source types from db
        query = """
            SELECT * FROM data_source_type;
        """

        result = self.db.execute(query).fetchall()
        return [(res["id"], res["name"]) for res in result]

    # request operations

    def create_request(self, requester, data_source, request_message):

        query = """
            INSERT INTO request (requester, data_source, request_message, date_updated, status)
            VALUES (?, ?, ?, DATETIME('NOW'), ?);
        """

        self.db.execute(query, (requester, data_source, request_message, 0))
        self.db.commit()

    def get_pending_requests_of_company(self, company_id):
        query = """
            SELECT request.id AS request_id, request.requester, request.data_source, request.request_message, request.date_created, request.status,
            company.id AS company_id, company.name AS company_name,
            employee.first_name, employee.last_name,
            data_source.title AS data_source_title
            FROM request
            JOIN employee on request.requester = employee.id
            JOIN company on employee.company = company.id
            JOIN data_source on request.data_source = data_source.id
            JOIN employee e2 on data_source.responsible_employee = e2.id
            WHERE request.status=0 AND e2.company=?;
        """

        result = self.db.execute(query, (company_id,)).fetchall()
        return [(
            res['request_id'],
            res['company_name'],
            res['requester'],
            res['first_name'],
            res['last_name'],
            res['data_source_title'],
            res['request_message'],
            res['date_created'],
            res['status']
            ) for res in result]

    def get_request_related_info_by_id(self, request_id):
        query = """
            SELECT request.id, request.request_message, request.date_created, 
            company.name AS company_name, company.id AS company_id,
            employee.id as emp_id, employee.first_name, employee.last_name, employee.email, employee.phone_number, employee.profile_photo,
            data_source.id AS data_source_id, data_source.title, data_source.description, data_source.subscription_fee,
            data_source_type.description AS data_source_type_description
            FROM request
            JOIN employee on request.requester = employee.id
            JOIN company on employee.company = company.id
            JOIN data_source on request.data_source = data_source.id
            JOIN data_source_type on data_source.type_id = data_source_type.id
            WHERE request.id=?;
        """

        result = self.db.execute(query, (request_id,)).fetchone()
        return result

    def accept_request(self, request_id, data_source_id, requester_id, company_id):
        update_request_query = """
            UPDATE request
            SET status=2
            WHERE id=?;
        """

        insert_data_source_permission_query = """
            INSERT INTO data_source_permission (data_source, employee, permission_type)
            VALUES (?, ?, ?);
        """

        insert_subscription_query = """
            INSERT INTO subscription (subscriber, data_source, request, subscription_started, subscription_ended, subscription_type, status)
            VALUES (?, ?, ?, DATETIME('NOW'), null, 1, 1);
        """

        self.db.execute(update_request_query, (request_id,))
        self.db.execute(insert_data_source_permission_query, (data_source_id, requester_id, 'read'))
        self.db.execute(insert_subscription_query, (requester_id, data_source_id, request_id))
        self.db.commit()

    def reject_request(self, request_id):
        query = """
            UPDATE request
            SET status=3
            WHERE id=?;
        """

        self.db.execute(query, (request_id,))
        self.db.commit()

    # others

    def create_data_usage(self, data_source, data_user, start_time, end_time, usage_amount, subscription):
        pass

    def update_data_usage(self, data_usage_id, data_source=None, data_user=None, start_time=None, end_time=None,
                          usage_amount=None, subscription=None):
        pass

    def create_subscription(self, subscriber, data_source, request, subscription_started, subscription_ended,
                            subscription_type, status):
        pass

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
            SELECT ds.id ds_id, ds.title ds_title, ds.type_id type, e.first_name || ' ' || e.last_name maintainer,
            ds.created_at ds_created_at 
            FROM data_source ds join employee e on ds.responsible_employee = e.id 
            where e.company = ?
            ORDER by ds.created_at desc;
        """

        result = self.db.execute(query, (str(company_id),)).fetchall()
        return [(
                res['ds_id'],
                res["ds_title"],
                self.get_data_source_type_name(res["type"]),
                self.get_active_users_of_data_source(res["ds_id"]),
                res["maintainer"],
                res["ds_created_at"]
                ) for res in result]

    def get_data_sources_by_responsible_employee_id(self, employee_id):
        query = """
            SELECT * FROM data_source WHERE responsible_employee=?;
        """

        result = self.db.execute(query, (str(employee_id),)).fetchall()
        return [(
                res["title"],
                self.get_data_source_type_name(res["type_id"]),
                self.get_active_users_of_data_source(res["id"]),
                res["created_at"]
        ) for res in result]

    def get_active_users_of_data_source(self, data_source_id):
        query = """
            SELECT COUNT(*) cnt FROM subscription WHERE data_source=? AND status=?;
        """

        result = self.db.execute(query, (data_source_id, 1)).fetchone()["cnt"]
        return result

    def get_data_source_id_by_file_save_path(self, data_root):
        query = """
            SELECT id FROM data_source WHERE data_root=?;
        """

        result = self.db.execute(query, (data_root,)).fetchone()
        return result["id"]

    def check_if_data_source_exists(self, table_name):
        query = """
            SELECT * FROM data_source WHERE database_table_name=?;
        """

        result = self.db.execute(query, (table_name,)).fetchone()
        return result is not None

    def get_data_source_by_title(self, title):
        query = """
            SELECT * FROM data_source WHERE title=?;
        """

        result = self.db.execute(query, (title,)).fetchone()
        return result

    def create_data_source_permission(self, data_source_id, employee, permission_type):
        if permission_type not in ["read", "write", "delete"]:
            raise Exception("permission_type must be one of 'read', 'write', 'delete'")

        query = """
            INSERT INTO data_source_permission (data_source, employee, permission_type)
            VALUES (?, ?, ?);
        """

        self.db.execute(query, (data_source_id, employee, permission_type))
        self.db.commit()

    def check_if_user_has_permission(self, table_name, employee, method):
        query = """
            SELECT * FROM data_source_permission dsp JOIN data_source ds on dsp.data_source = ds.id 
            WHERE ds.database_table_name=? AND employee=? AND permission_type=?;
        """

        result = self.db.execute(query, (table_name, employee, method)).fetchone()
        return result is not None

    def execute_query(self, query):
        result = self.db.execute(query).fetchall()
        return result

    def get_table_columns(self, table_name):
        query = f"""
            PRAGMA table_info({table_name});
        """

        result = self.db.execute(query).fetchall()
        return [res['name'] for res in result]

    def update_datasource_url_endpoint(self, data_source_id, endpoint):
        query = """
            UPDATE data_source
            SET url_endpoint=?
            WHERE id=?;
        """

        self.db.execute(query, (endpoint, data_source_id))
        self.db.commit()

    def get_user_managed_data_source_ids(self, employee_id):
        query = """
            SELECT * FROM data_source WHERE responsible_employee=?;
        """

        result = self.db.execute(query, (employee_id,)).fetchall()
        return [res['id'] for res in result]

    def get_user_subscribed_data_source_ids(self, company_id):
        query = """
            SELECT * FROM subscription sub join data_source ds on sub.data_source = ds.id WHERE subscriber=?;
        """

        result = self.db.execute(query, (company_id,)).fetchall()
        return [res['id'] for res in result]

    def get_number_of_data_sources_of_company(self, company_id):
        query = """
            SELECT count(*) cnt FROM data_source ds join employee e on ds.responsible_employee = e.id WHERE e.company=?;
        """

        result = self.db.execute(query, (company_id,)).fetchone()['cnt']
        return int(result)

    def get_number_of_subscriptions_of_company(self, company_id):
        query = """
            SELECT count(*) cnt FROM subscription sub 
            join data_source ds on sub.data_source = ds.id 
            join employee e on sub.subscriber = e.id 
                WHERE e.company=?;
        """

        result = self.db.execute(query, (company_id,)).fetchone()['cnt']
        return int(result)

    def get_bandwidth_of_company(self, company_id, unit="GB"):
        query = """
            SELECT sum(usage_amount) usg FROM data_usage du join data_source ds on du.data_source = ds.id 
            where du.data_user=?;
        """

        result = self.db.execute(query, (company_id,)).fetchone()['usg']
        result = 0 if result is None else result

        if unit == "GB":
            return result * 1e-6
        elif unit == "MB":
            return result * 1e-3
        else:
            return result

    def get_number_of_pending_requests(self, company_id):
        query = """
            SELECT count(*) cnt FROM request req 
            join data_source ds on req.data_source = ds.id 
            join employee e on ds.responsible_employee = e.id
            WHERE e.company=? and status=?;
        """

        result = self.db.execute(query, (company_id, 0)).fetchone()['cnt']
        return int(result)

    def get_dashboard_numbers(self, company_id):
        num_data_sources = self.get_number_of_data_sources_of_company(company_id)
        num_subscriptions = self.get_number_of_subscriptions_of_company(company_id)
        bandwidth = self.get_bandwidth_of_company(company_id)
        num_pending_requests = self.get_number_of_pending_requests(company_id)

        return {
            "num_data_sources": num_data_sources,
            "num_subscriptions": num_subscriptions,
            "bandwidth": round(bandwidth, 2),
            "num_pending_requests": num_pending_requests
        }

    def get_subscriptions_of_company_for_dashboard_table(self, company_id):
        query = """
            SELECT 
                ds.id as ds_id,
                ds.title as data_source_title,
                dst.name as data_source_type,
                c2.name as company_name,
                ds.url_endpoint as data_source_url_endpoint,
                sub.subscription_started as subscription_date
            FROM subscription sub 
                join data_source ds on sub.data_source = ds.id 
                join employee e on sub.subscriber = e.id 
                join company c on e.company = c.id
                join employee e2 on ds.responsible_employee = e2.id
                join company c2 on c2.id = e2.company
                join data_source_type dst on ds.type_id = dst.id
                WHERE e.company=?;
        """

        result = self.db.execute(query, (company_id,)).fetchall()
        return [{
            "data_source_id": res["ds_id"],
            "data_source_title": res["data_source_title"],
            "data_source_type": res["data_source_type"],
            "company_name": res["company_name"],
            "data_source_url_endpoint": (res["data_source_url_endpoint"]+"/read") if res["data_source_url_endpoint"] else 'Not generated yet!',
            "subscription_date": res["subscription_date"]
        } for res in result]

    def get_data_usages_of_company(self, company_id):
        query = """
            SELECT 
                ds.title as data_source_title,
                dst.name as data_source_type,
                du.usage_amount as usage_amount
            FROM data_usage du 
                join data_source ds on du.data_source = ds.id 
                join employee e on ds.responsible_employee = e.id 
                join data_source_type dst on ds.type_id = dst.id
                WHERE e.company=?;
        """

        result = self.db.execute(query, (company_id,)).fetchall()
        return [{
            "data_source_title": res["data_source_title"],
            "data_source_type": res["data_source_type"],
            "usage_amount": res["usage_amount"]
        } for res in result]

    def get_maintainer_of_data_source(self, data_source_id):
        query = """
            SELECT * 
            FROM data_source 
            JOIN employee ON data_source.responsible_employee = employee.id
            WHERE data_source.id=?;
        """

        result = self.db.execute(query, (data_source_id,)).fetchone()
        return result

    def get_data_source_type_by_id(self, data_source_type_id):
        query = """
            SELECT * FROM data_source_type WHERE id=?;
        """

        result = self.db.execute(query, (data_source_type_id,)).fetchone()
        return result
