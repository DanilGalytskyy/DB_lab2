class Check(object):
    @staticmethod
    def isUserAttributes(user):
        if 'name' and 'email' and 'password' not in user:
            return False
        return True

    @staticmethod
    def isPostAttributes(post):
        if 'datetime' and 'title' and 'user_id' not in post:
            return False
        return True

    @staticmethod
    def isCommentAttributes(comment):
        if 'body' and 'datetime' and 'user_id' and 'post_id' not in comment:
            return False
        return True

    @staticmethod
    def isPostReactionAttributes(post_reaction):
        if 'value' and 'datetime' and 'post_id' and 'user_id' not in post_reaction:
            return False
        return True

    @staticmethod
    def isCommentReactionAttributes(comment_reaction):
        if 'value' and 'datetime' and 'comment_id' and 'user_id' not in comment_reaction:
            return False
        return True

    @staticmethod
    def updateUser(user, older):
        i = 0
        options = ['name', 'phone_number', 'email', 'password']
        for key in options:
            i += 1
            if key not in user:
                user[key] = older[0][i]
        return user

    @staticmethod
    def updatePost(post, older):
        i = 0
        options = ['datetime', 'title', 'body', 'user_id']
        for key in options:
            i += 1
            if key not in post:
                post[key] = older[0][i]
        return post

    @staticmethod
    def updateComment(comment, older):
        i = 0
        options = ['body', 'datetime', 'user_id', 'post_id']
        for key in options:
            i += 1
            if key not in comment:
                comment[key] = older[0][i]
        return comment

    @staticmethod
    def updatePostReaction(post_reaction, older):
        i = 0
        options = ['value', 'datetime', 'post_id', 'user_id']
        for key in options:
            i += 1
            if key not in post_reaction:
                post_reaction[key] = older[0][i]
        return post_reaction

    @staticmethod
    def updateCommentReaction(comment_reaction, older):
        i = 0
        options = ['value', 'datetime', 'comment_id', 'user_id']
        for key in options:
            i += 1
            if key not in comment_reaction:
                comment_reaction[key] = older[0][i]
        return comment_reaction
