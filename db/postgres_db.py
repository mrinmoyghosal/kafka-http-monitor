import json
import time

from postgres import Postgres

from config.logger import get_logger
from db.base_database import DatabaseClient, SQLQueries
from service.util import CONSTANTS

logger = get_logger("pg_database_client")


class PgDatabaseClient(DatabaseClient):
    """ Postgres Database Client Implementation """
    def __init__(self, config):
        super().__init__(config)

    def configure(self):
        """ Configure db client and create table"""
        self.db_client = Postgres(url=self._config.get(CONSTANTS.DB_HOST))
        self.create_table_if_no_exist()

    def create_table_if_no_exist(self):
        """ Create table if not exists """
        with self.db_client.get_cursor() as cursor:
            cursor.run(SQLQueries.CREATE_TABLE)

    def insert_data(self, data: str):
        """ Insert data to the table """
        try:
            msg = json.loads(data)
            with self.db_client.get_cursor() as cursor:
                cursor.run(SQLQueries.INSERT_DATA, msg)
            logger.info(f"Data saved successfully at - {time.monotonic()}")
        except Exception as e:
            logger.error(f"Cannot save data to db, following error occurred {e}")
