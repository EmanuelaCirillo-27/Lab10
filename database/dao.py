from database.DB_connect import DBConnect
from model.filiale import Filiale

class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """

    @staticmethod
    def read_all_filiali():
        conn = DBConnect.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            try:

                query="""SELECT * FROM filiale"""
                cursor.execute(query)
                result = []
                for row in cursor:
                    filiale = Filiale(**row)
                    result.append(filiale)
                return result
            finally:
                cursor.close()
        finally:
            conn.close()

    @staticmethod
    def read_all_collegamenti():
        conn = DBConnect.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            try:

                query = """SELECT LEAST(id_filiale_origine,id_filiale_destinazione) as origine,
                                    GREATEST(id_filiale_origine,id_filiale_destinazione) as arrivo,
                                    SUM(importo) AS somma,
                                    COUNT(*) AS conteggio
                                    FROM bonifico
                                    GROUP BY origine,arrivo"""
                cursor.execute(query)
                result = []
                for row in cursor:
                    result.append(row)
                return result
            finally:
                cursor.close()
        finally:
            conn.close()