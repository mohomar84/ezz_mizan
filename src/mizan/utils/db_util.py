import sqlite3


class DB_Utils:

    @staticmethod
    def get_aya(sura: int, aya: int):
        """

        :param sura:
        :param aya:
        :return:
        """
        conn = sqlite3.connect('csc455_HW3.db')

        with open('../../DB_Quran/quran.sql', 'r') as sql_file:
            conn.executescript(sql_file.read())
            conn.execute("SELECT text FROM quran_text where sura = " + sura + " and aya = " + aya)

        conn.close()
     #   for row in cursor.execute("SELECT text FROM quran_text where sura = " + sura + " and aya = " + aya):
     #       print(row)
