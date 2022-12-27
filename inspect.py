import psycopg2
from timeit import default_timer as timer


class Inspect(object):

    @staticmethod
    def findExistRow(connection, tableName):
        cursor = connection.cursor()
        cursor.execute("select {}_id from public.\"{}\" ORDER BY random() LIMIT 1;"
                       .format(tableName.lower(), tableName))
        value = cursor.fetchall()
        return value[0][0]

    @staticmethod
    def findExistingId(connection, tableName, anyId):
        cursor = connection.cursor()
        cursor.execute("""SELECT {}_id FROM public.\"{}\" WHERE {}_id={};"""
                       .format(tableName.lower(), tableName, tableName.lower(), anyId))
        value = cursor.fetchall()
        return len(value) != 0

    @staticmethod
    def findItemName(connection, name):
        cursor = connection.cursor()
        cursor.execute("SELECT post_id, public.\"User\".user_id, public.\"User\".name, public.\"Post\".title, "
                       "public.\"Post\".body, public.\"Post\".datetime "
                       "FROM public.\"Post\" INNER JOIN public.\"User\" ON "
                       "public.\"Post\".user_id=public.\"User\".user_id"
                       " WHERE public.\"User\".name LIKE '%{}%';".format(name))
        value = cursor.fetchall()
        return value

    @staticmethod
    def findItemName(connection, name):
        cursor = connection.cursor()
        start = timer()
        cursor.execute("SELECT post_id, public.\"User\".user_id, public.\"User\".name, public.\"Post\".title, "
                       "public.\"Post\".body, public.\"Post\".datetime "
                       "FROM public.\"Post\" INNER JOIN public.\"User\" ON "
                       "public.\"Post\".user_id=public.\"User\".user_id"
                       " WHERE public.\"User\".name LIKE '%{}%';".format(name))
        value = cursor.fetchall()
        end = timer()
        print('Execution time is ', end - start)
        return value

    @staticmethod
    def findPostReactions(connection, reaction):
        cursor = connection.cursor()
        start = timer()
        cursor.execute("SELECT public.\"Post_Reaction\".user_id, public.\"Post\".post_id, value, "
                       "public.\"Post\".title, "
                       "public.\"Post\".body, public.\"Post\".datetime "
                       "FROM public.\"Post_Reaction\" INNER JOIN public.\"Post\" ON "
                       "public.\"Post_Reaction\".post_id=public.\"Post\".post_id "
                       "WHERE  value = {};".format(reaction))
        value = cursor.fetchall()
        end = timer()
        print('Execution time is ', end - start)
        return value

    @staticmethod
    def findRowBetweenDates(connection, first, second):
        cursor = connection.cursor()
        start = timer()
        cursor.execute("SELECT public.\"User\".user_id, public.\"User\".name, public.\"Comment\".post_id, body, "
                       "public.\"Comment\".datetime, comment_id "
                       "FROM public.\"Comment\" INNER JOIN public.\"User\" ON "
                       "public.\"Comment\".user_id=public.\"User\".user_id "
                       "WHERE  datetime BETWEEN to_date('{}','YYYY-MM-DD') "
                       "AND to_date('{}','YYYY-MM-DD'); ".format(first, second))
        value = cursor.fetchall()
        end = timer()
        print('Execution time is ', end - start)
        return value
