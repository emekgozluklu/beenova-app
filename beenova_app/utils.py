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

    def handle_csv(self):
        try:
            pd.read_csv(self.file_path).to_sql(self.table_name, g.db, if_exists="fail")
        except ValueError:
            self.table_name = self.table_name + "_1"
            pd.read_csv(self.file_path).to_sql(self.table_name, g.db, if_exists="fail")
