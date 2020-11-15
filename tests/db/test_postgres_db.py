from pytest_mock import MockerFixture
from db.postgres_db import PgDatabaseClient
from db.postgres_db import logger


def test_postgres_db_client_create_table_if_not_exists(mocker: MockerFixture):
    mocker.patch('db.postgres_db.Postgres', autospec=True)
    spy_db_client = mocker.spy(PgDatabaseClient, 'create_table_if_no_exist')
    PgDatabaseClient(mocker.MagicMock())
    spy_db_client.assert_called_once()


def test_postgres_db_insert_data_raises_exception_if_data_is_not_json_decodable(mocker: MockerFixture):
    mocker.patch('db.postgres_db.Postgres', autospec=True)
    logger_patched = mocker.patch.object(logger, 'error', autospec=True)
    db_client = PgDatabaseClient(mocker.MagicMock())
    db_client.insert_data("")
    logger_patched.assert_called_once_with("Cannot save data to db, following error occurred Expecting value: line 1 "
                                           "column 1 (char 0)")


def test_postgres_db_insert_data_as_expected(mocker: MockerFixture):
    mocker.patch('db.postgres_db.Postgres', autospec=True)
    logger_patched = mocker.patch.object(logger, 'info', autospec=True)
    db_client = PgDatabaseClient(mocker.MagicMock())
    db_client.insert_data('{"a":"b"}')
    logger_patched.assert_called_once_with("Data saved successfully")

