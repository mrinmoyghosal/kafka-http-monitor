from abc import ABC, abstractmethod


class DatabaseClient(ABC):
    """ Abstract Database Client"""
    _config: dict

    @abstractmethod
    def __init__(self, config):
        self._config = config
        self.configure()

    @abstractmethod
    def configure(self):
        """
        Abstract method for configuring database client
        :return:
        """
        pass

    @abstractmethod
    def insert_data(self, data):
        """
        Abstract method for inserting data to database
        :param data:
        :return:
        """
        pass


class SQLQueries:
    """ SQL Queries"""
    CREATE_TABLE: str = """
        CREATE TABLE IF NOT EXISTS event_history (
            address text,
            response_status integer,
            response_time_in_seconds real,
            content_type varchar(255),
            regex_pattern_found boolean,
            regex_pattern varchar(255),
            created timestamp default current_timestamp 
        )
    """

    INSERT_DATA: str = """
        INSERT INTO event_history (
            address, 
            response_status, 
            response_time_in_seconds, 
            content_type, 
            regex_pattern_found,
            regex_pattern
        ) VALUES (
            %(address)s, 
            %(response_status)s, 
            %(response_time_in_seconds)s, 
            %(content_type)s, 
            %(regex_pattern_found)s,
            %(regex_pattern)s
        )
    """
