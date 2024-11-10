from database.DB_connect import DBConnect
from model.edges import Edge
from model.states import State


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
    def getYears():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct year(s.`datetime`) as year
                        from sighting s 
                        order by year(s.`datetime`) desc
"""
            cursor.execute(query)
            for row in cursor:
                result.append(row['year'])
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getAllEdges(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select  s1.id as s1,s2.id as s2
                    from state s1,state s2,neighbor n 
                    where s1.id = n.state1 
                    and s2.id = n.state2 
                    and s1.id < s2.id 
                    group by s1.id,s2.id
"""

        cursor.execute(query)

        for row in cursor:
            result.append(Edge(idMap[row["s1"]],idMap[row["s2"]]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllWeight(s1,s2,year,gg):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT count(*) as weight
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
                    ON DATEDIFF(avv1.`datetime`, avv2.`datetime`) < %s


"""

        cursor.execute(query,(s1,year,s2,year,gg))

        for row in cursor:
            result.append(row["weight"])

        cursor.close()
        conn.close()
        return result[0]


