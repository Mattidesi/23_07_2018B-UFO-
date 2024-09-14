from database.DB_connect import DBConnect
from model.arco import Arco
from model.state import State


class DAO():
    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
        from state s """

        cursor.execute(query)

        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
        from neighbor n
        where state1<state2 """

        cursor.execute(query)

        for row in cursor:
            result.append((row["state1"], row["state2"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def calcolaPeso(s1, s2, giorni, anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT count(*) as peso
    FROM (
        SELECT *
        FROM sighting s 
        WHERE state = %s AND year(`datetime`) = %s
    ) AS avv1
    JOIN (
        SELECT *
        FROM sighting s 
        WHERE state =%s AND year(`datetime`) = %s
    ) AS avv2
    ON DATEDIFF(avv1.`datetime`, avv2.`datetime`) < %s"""

        cursor.execute(query, (s1, anno, s2, anno, giorni))

        for row in cursor:
            result.append(row["peso"])

        cursor.close()
        conn.close()
        return result[0]
