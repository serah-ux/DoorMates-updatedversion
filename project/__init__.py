import pymysql

# 1. Fake mysqlclient version
pymysql.version_info = (2, 2, 1, 'final', 0)
pymysql.install_as_MySQLdb()

# 2. Fake MariaDB server version check
from django.db.backends.base.base import BaseDatabaseWrapper
BaseDatabaseWrapper.check_database_version_supported = lambda self: None

# 3. Force-disable 'RETURNING' feature for older MariaDB
from django.db.backends.mysql.features import DatabaseFeatures

# We replace the property methods with functions that always return False
DatabaseFeatures.can_return_columns_from_insert = property(lambda self: False)
DatabaseFeatures.can_return_rows_from_bulk_insert = property(lambda self: False)