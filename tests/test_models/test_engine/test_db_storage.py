#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
from os import getenv
import MySQLdb


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
class Test_DBStorage(unittest.TestCase):
    """ Class to test db storage """

    def setUp(self):
        """ Set up MySQL environment """
        hbnb_user = getenv("HBNB_MYSQL_USER")
        hbnb_passwd = getenv("HBNB_MYSQL_PWD")
        hbnb_db = getenv("HBNB_MYSQL_DB")
        hbnb_host = getenv("HBNB_MYSQL_HOST")
        self.db = MySQLdb.connect(host=hbnb_host,
                                  user=hbnb_user,
                                  passwd=hbnb_passwd,
                                  db=hbnb_db,
                                  charset='utf8')
        self.curr = self.db.cursor()
        storage.reload()

    def tearDown(self):
        """ Close db at the end of tests """
        self.curr.close()
        self.db.close()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_retrieve_user_data(self):
        """ check user data exists """
        self.curr.execute("SELECT * FROM users")
        user_data = self.query.fetchall()
        self.assertEqual(len(user_data), 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_tables(self):
        """ test tables """
        self.curr.execute("SHOW TABLES")
        table_data = self.curr.fetchall()
        self.assertEqual(len(table_data), 7)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_state_data(self):
        """ check state data exits """
        self.curr.execute("SELECT * FROM states")
        state_data = self.curr.fetchall()
        self.assertEqual(len(state_data), 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_state_add(self):
        """ check state data insertion """
        self.curr.execute("SELECT * FROM states")
        state_data = self.curr.fetchall()
        self.assertEqual(len(state_data), 0)
        state = State(name="California")
        state.save()
        self.db.autocommit(True)
        self.curr.execute("SELECT * FROM states")
        state_data = self.curr.fetchall()
        self.assertEqual(len(state_data), 1)


if __name__ == '__main__':
    unittest.main()
