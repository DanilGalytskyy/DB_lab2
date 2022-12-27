import psycopg2


def select_one(connection, tableName, attributeId):
    try:
        cursor = connection.cursor()
        cursor.execute("select * from public.\"{}\" where {}_id = {}".format(tableName, tableName.lower(), attributeId))

        record = cursor.fetchall()
        return record

    except(Exception, psycopg2.Error) as error:
        print("Error with fetching one data", error)


def select_all(connection, tableName):
    try:
        cursor = connection.cursor()
        cursor.execute("select * from public.\"{}\"".format(tableName, tableName))

        record = cursor.fetchall()
        return record

    except(Exception, psycopg2.Error) as error:
        print("Error with fetching all data", error)


def insert_one_user(connection, name, phone_number, email, password):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"User\" (name, phone_number, email, password)"
                       "values ('{}', '{}', '{}', '{}')".format(name, phone_number, email, password))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with user inserting", error)


def insert_many_random_users(connection, count):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"User\" (name, phone_number, email, password)"
                       "select left(md5(random()::text), 10),"
                       "concat('+380',trunc(random()*1000000000)::int),"
                       "concat(left(md5(random()::text), 10),'@example.com'), left(md5(random()::text), 20)"
                       "FROM generate_series(1, {})".format(count))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with user inserting", error)


def insert_one_post(connection, datetime, title, body, user_id):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"Post\" (datetime, title, body, user_id)"
                       "values ('{}', '{}', '{}', '{}')".format(datetime, title, body, user_id))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with post inserting", error)


def insert_many_random_posts(connection, userId, count):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"Post\" (datetime, title, body, user_id)"
                       "select NOW() + (random() * (NOW()+'90 days' - NOW())) + '30 days', "
                       "left(md5(random()::text), 10), left(md5(random()::text), 20), {} "
                       "from generate_series(1, {})".format(userId, count))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with post inserting", error)


def insert_one_comment(connection, body, datetime, user_id, post_id):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"Comment\" (body, datetime, user_id, post_id)"
                       "values ('{}', '{}', '{}', '{}')".format(body, datetime, user_id, post_id))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with comment inserting", error)


def insert_many_random_comments(connection, userId, postId, count):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"Comment\" (body, datetime, user_id, post_id)"
                       "select left(md5(random()::text), 10),"
                       "NOW() + (random() * (NOW()+'90 days' - NOW())) + '30 days',"
                       "{}, {} from generate_series(1, {})".format(userId, postId, count))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with comment inserting", error)


def insert_post_reaction(connection, value, datetime, post_id, user_id):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"Post_Reaction\" (value, datetime, post_id, user_id)"
                       "values ({}, '{}', {}, {})".format(value, datetime, post_id, user_id))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with post reaction inserting", error)


def insert_random_post_reaction(connection, post_id, user_id):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"Post_Reaction\" (value, datetime, post_id, user_id)"
                       "select round(random())::int::boolean,"
                       "NOW() + (random() * (NOW()+'90 days' - NOW())) + '30 days',"
                       "{}, {}".format(post_id, user_id))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with post reaction inserting", error)


def insert_comment_reaction(connection, value, datetime, comment_id, user_id):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"Comment_Reaction\" (value, datetime, comment_id, user_id)"
                       "values ({}, '{}', {}, {})".format(value, datetime, comment_id, user_id))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with comment reaction inserting", error)


def insert_random_comment_reaction(connection, comment_id, user_id):
    try:
        cursor = connection.cursor()
        cursor.execute("insert into public.\"Comment_Reaction\" (value, datetime, comment_id, user_id)"
                       "select round(random())::int::boolean,"
                       "NOW() + (random() * (NOW()+'90 days' - NOW())) + '30 days',"
                       "{}, {}".format(comment_id, user_id))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with comment reaction inserting", error)


def update_one_post(connection, post_id, new_datetime, new_title, new_body, new_user_id):
    try:
        cursor = connection.cursor()
        cursor.execute("update public.\"Post\" set datetime = '{}', title = '{}', body = '{}', user_id = '{}'"
                       "where post_id = {}".format(new_datetime, new_title, new_body, new_user_id, post_id))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with post updating", error)


def update_one_user(connection, user_id, new_name, new_phone_number, new_email, new_password):
    try:
        cursor = connection.cursor()
        cursor.execute("update public.\"User\" set name = '{}', phone_number = '{}', email = '{}', password = '{}'"
                       "where user_id = {}".format(new_name, new_phone_number, new_email, new_password, user_id))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with user updating", error)


def update_one_comment(connection, comment_id, body, datetime, user_id, post_id):
    try:
        cursor = connection.cursor()
        cursor.execute("update public.\"Comment\" set body = '{}', datetime = '{}', user_id = '{}', post_id = '{}'"
                       "where comment_id = {}".format(body, datetime, user_id, post_id, comment_id))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with comment updating", error)


def update_one_post_reaction(connection, post_reactionId, value, datetime, post_id, user_id):
    try:
        cursor = connection.cursor()
        cursor.execute("update public.\"Post_Reaction\" set value = {}, datetime = '{}', post_id = {}, user_id = "
                       "{} "
                       "where post_reaction_id = {}".format(value, datetime, post_id, user_id, post_reactionId))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with post reaction updating", error)


def update_one_comment_reaction(connection, comment_reactionId, value, datetime, comment_id, user_id):
    try:
        cursor = connection.cursor()
        cursor.execute("update public.\"Comment_Reaction\" set value = {}, datetime = '{}', comment_id = {}, user_id = "
                       "{} "
                       "where comment_reaction_id = {}".format(value, datetime, comment_id, user_id,
                                                               comment_reactionId))
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.Error) as error:
        print("Error with post reaction updating", error)


def delete_one(connection, tableName, elementId):
    try:
        cursor = connection.cursor()
        cursor.execute("delete from public.\"{}\" where {}_id = {}".format(tableName, tableName.lower(), elementId))
        connection.commit()
    except(Exception, psycopg2.Error) as error:
        print("Error with user deleting", error)
