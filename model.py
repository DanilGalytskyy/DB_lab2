import psycopg2
import queriesSQL as SQL
import inspect


class Model(object):

    def __init__(self):
        self._connection = self.connect_to_db()

    @property
    def connection(self):
        return self._connection

    @staticmethod
    def connect_to_db():
        connection = psycopg2.connect(host="localhost", port="5432", user="postgres", password="qwerty123")
        return connection

    def disconnect_from_db(self):
        if self.connection is not None:
            self.connection.close()


class ModelUser(Model):

    def __init__(self):
        super().__init__()
        self._tableName = "User"

    @property
    def tableName(self):
        return self._tableName

    def read_user(self, userId):
        return SQL.select_one(self.connection, self._tableName, userId)

    def read_users(self):
        return SQL.select_all(self.connection, self._tableName)

    def create_user(self, name, phone_number, email, password):
        return SQL.insert_one_user(self.connection, name, phone_number, email, password)

    def create_many_users(self, count):
        return SQL.insert_many_random_users(self.connection, count)

    def reform_user(self, user_id, name, phone_number, email, password):
        return SQL.update_one_user(self.connection, user_id, name, phone_number, email, password)

    def remove_user(self, userId):
        return SQL.delete_one(self.connection, self._tableName, userId)


class ModelPost(Model):
    def __init__(self):
        super().__init__()
        self._tableName = "Post"

    @property
    def tableName(self):
        return self._tableName

    def read_posts(self):
        return SQL.select_all(self.connection, self._tableName)

    def read_post(self, postId):
        return SQL.select_one(self.connection, self._tableName, postId)

    def read_users_posts(self, name):
        return inspect.Inspect.findItemName(self.connection, name)

    def create_post(self, datetime, title, body, user_id):
        return SQL.insert_one_post(self.connection, datetime, title, body, user_id)

    def create_many_posts(self, count):
        try:
            userId = inspect.Inspect.findExistRow(self.connection, "User")
            assert inspect.Inspect.findExistingId(self.connection, "User", userId), '\033[91m item id isn\'t exist ' \
                                                                                    '\033[0m '
            SQL.insert_many_random_posts(self.connection, userId, count)
            return True
        except Exception as err:
            print(err)
            return False

    def reform_post(self, post_id, datetime, title, body, user_id):
        return SQL.update_one_post(self.connection, post_id, datetime, title, body, user_id)

    def remove_post(self, postId):
        return SQL.delete_one(self.connection, self._tableName, postId)


class ModelComment(Model):
    def __init__(self):
        super().__init__()
        self._tableName = "Comment"

    @property
    def tableName(self):
        return self._tableName

    def read_comment(self, commentId):
        return SQL.select_one(self.connection, self._tableName, commentId)

    def read_comments(self):
        return SQL.select_all(self.connection, self._tableName)

    def read_comment_byDates(self, first, second=None):
        return inspect.Inspect.findRowBetweenDates(self.connection, first, second)

    def create_comment(self, body, datetime, user_id, post_id):
        return SQL.insert_one_comment(self.connection, body, datetime, user_id, post_id)

    def create_many_comments(self, count):
        try:
            userId = inspect.Inspect.findExistRow(self.connection, "User")
            postId = inspect.Inspect.findExistRow(self.connection, "Post")
            assert inspect.Inspect.findExistingId(self.connection, "User", userId), '\033[91m item id isn\'t exist ' \
                                                                                    '\033[0m '
            assert inspect.Inspect.findExistingId(self.connection, "Post", postId), '\033[91m item id isn\'t exist ' \
                                                                                    '\033[0m '
            SQL.insert_many_random_comments(self.connection, userId, postId, count)
            return True
        except Exception as err:
            print(err)
            return False

    def reform_comment(self, comment_id, body, datetime, user_id, post_id):
        return SQL.update_one_comment(self.connection, comment_id, body, datetime, user_id, post_id)

    def remove_comment(self, commentId):
        return SQL.delete_one(self.connection, self._tableName, commentId)


class ModelPost_Reaction(Model):
    def __init__(self):
        super().__init__()
        self._tableName = "Post_Reaction"

    @property
    def tableName(self):
        return self._tableName

    def read_post_reactions(self):
        return SQL.select_all(self.connection, self._tableName)

    def read_post_reaction(self, reactionId):
        return SQL.select_one(self.connection, self._tableName, reactionId)

    def read_reactions_ByLikeDislike(self, reaction):
        return inspect.Inspect.findPostReactions(self.connection, reaction)

    def create_post_reaction(self, value, datetime, post_id, user_id):
        return SQL.insert_post_reaction(self.connection, value, datetime, post_id, user_id)

    def create_random_post_reaction(self):
        try:
            userId = inspect.Inspect.findExistRow(self.connection, "User")
            postId = inspect.Inspect.findExistRow(self.connection, "Post")
            assert inspect.Inspect.findExistingId(self.connection, "User", userId), '\033[91m item id isn\'t exist ' \
                                                                                    '\033[0m '
            assert inspect.Inspect.findExistingId(self.connection, "Post", postId), '\033[91m item id isn\'t exist ' \
                                                                                    '\033[0m '
            SQL.insert_random_post_reaction(self.connection, postId, userId, )
            return True
        except Exception as err:
            print(err)
            return False

    def reform_post_reaction(self, post_reaction_id, value, datetime, post_id, user_id):
        return SQL.update_one_post_reaction(self.connection, post_reaction_id, value, datetime, post_id, user_id)

    def remove_post_reaction(self, post_reactionId):
        return SQL.delete_one(self.connection, self._tableName, post_reactionId)


class ModelComment_Reaction(Model):
    def __init__(self):
        super().__init__()
        self._tableName = "Comment_Reaction"

    @property
    def tableName(self):
        return self._tableName

    def read_comment_reactions(self):
        return SQL.select_all(self.connection, self._tableName)

    def read_comment_reaction(self, comment_reactionId):
        return SQL.select_one(self.connection, self._tableName, comment_reactionId)

    def create_comment_reaction(self, value, datetime, comment_id, user_id):
        return SQL.insert_comment_reaction(self.connection, value, datetime, comment_id, user_id)

    def create_random_comment_reaction(self):
        try:
            userId = inspect.Inspect.findExistRow(self.connection, "User")
            commentId = inspect.Inspect.findExistRow(self.connection, "Comment")
            assert inspect.Inspect.findExistingId(self.connection, "User", userId), '\033[91m item id isn\'t exist ' \
                                                                                    '\033[0m '
            assert inspect.Inspect.findExistingId(self.connection, "Comment",
                                                  commentId), '\033[91m item id isn\'t exist ' \
                                                              '\033[0m '
            SQL.insert_random_comment_reaction(self.connection, commentId, userId)
            return True
        except Exception as err:
            print(err)
            return False

    def reform_comment_reaction(self, comment_reaction_id, value, datetime, comment_id, user_id):
        return SQL.update_one_comment_reaction(self.connection, comment_reaction_id, value, datetime, comment_id,
                                               user_id)

    def remove_comment_reaction(self, comment_reactionId):
        return SQL.delete_one(self.connection, self._tableName, comment_reactionId)
