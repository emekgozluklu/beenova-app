import sqlite3
import pandas as pd

from beenova_app.db_queries import DBOperator
from flask import g


def normalize_sql_table_name(table_name):
    return table_name.replace(" ", "_").replace("-", "_").lower()


class DataSourceFileHandler:

    def __init__(self, data_source_id, file_path):
        self.db_operator = DBOperator()

        self.data_source_id = data_source_id
        self.data_source = self.db_operator.get_data_source_by_id(self.data_source_id)
        self.file_path = file_path

        self.table_name = normalize_sql_table_name(self.data_source["title"])

    def update_datasource_table_name(self):
        self.db_operator.update_datasource_table_name(self.data_source_id, self.table_name)

    def update_data_source_url_endpoint(self):
        endpoint = f"/api/v1/{self.table_name}"
        self.db_operator.update_datasource_url_endpoint(self.data_source_id, endpoint)

    def handle_csv(self):
        try:
            pd.read_csv(self.file_path).to_sql(self.table_name, g.db, if_exists="fail")
        except ValueError:
            self.table_name = self.table_name + "_1"
            pd.read_csv(self.file_path).to_sql(self.table_name, g.db, if_exists="fail")

        self.update_datasource_table_name()
        self.update_data_source_url_endpoint()


class APIRequestHandler:
    def __init__(self, args, table_name, method):
        self.args = args
        self.table_name = table_name
        self.db_operator = DBOperator()
        self.method = method

    def validate_args(self):
        table_columns = self.db_operator.get_table_columns(self.table_name)
        table_columns += ["columns"]

        for arg in self.args.keys():
            if arg not in table_columns:
                return False
        return True

    def read_query_builder(self):
        columns = self.args.pop("columns") if "columns" in self.args else ["*"]
        conditions = [(cond, self.args[cond]) for cond in self.args.keys()]

        query = f"SELECT"

        for column in columns[:-1]:
            query += f" {column},"

        query += f" {columns[-1]} FROM {self.table_name} WHERE 1=1"

        for cond in conditions[:-1]:
            query += f" AND {cond[0]} = '{cond[1]}'"
        if conditions:
            query += f" AND {conditions[-1][0]} = '{conditions[-1][1]}'"
        query += ";"

        return query

    def handle_request(self):
        if self.validate_args():
            if self.method == "read":
                query = self.read_query_builder()
                return self.db_operator.execute_query(query)
            elif self.method == "write":
                pass
            elif self.method == "delete":
                pass
        else:
            return "Invalid arguments", 400
