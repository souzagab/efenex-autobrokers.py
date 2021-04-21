import sqlite3
from sqlite3 import Error

from src.lib.singleton import Singleton


@Singleton
class DatabaseConnection(object):
    connection = None

    def con(self):
        """
        Cria a conexão caso nao exista com o banco a partir do arquivo .db
            :return: Conexão

        """
        if self.connection is None:
            try:
                # TODO: Resolver path do banco pro deploy
                self.connection = sqlite3.connect("efenex.db")

            except Error as e:
                print(e)

        return self.connection
