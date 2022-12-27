import inputData
import checkData


class ConrtrollerUser(object):
    def __init__(self, model, view):
        self.model = model()
        self.view = view()

    def show_users(self):
        users = self.model.read_users()
        self.view.show_list_users(users)

    def show_user(self):
        user_id = inputData.Input.input_id(self.model.tableName)
        user = self.model.read_user(user_id)
        self.view.show_list_users(user)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()

    def insert_user(self, user):
        try:
            user = inputData.Input.input_update_user(user)
            assert checkData.Check.isUserAttributes(user), 'Some user attribute was not add'
            self.model.create_user(user['name'], user['phone_number'], user['email'], user['password'])
            self.view.display_added(user['name'], self.model.tableName)
        except Exception as err:
            print(err)

    def insert_many_users(self):
        try:
            count = inputData.Input.input_count()
            assert count > 1, '\033[91m count must be more one \033[0m'
            self.model.create_many_users(count)
            self.view.display_many_added(count, self.model.tableName)
        except Exception as err:
            print(err)

    def update_user(self, user):
        try:
            user_id = inputData.Input.input_id(self.model.tableName)
            user = inputData.Input.input_update_user(user)
            old = self.model.read_user(user_id)
            newUser = checkData.Check.updateUser(user, old)
            check = self.model.reform_user(user_id, newUser['name'], newUser['phone_number'], newUser['email'],
                                           newUser['password'], )
            self.view.display_added(user['name'], self.model.tableName)
            if check:
                self.view.display_user_updated(user_id, old[0][1], old[0][2], newUser['name'], newUser['phone_number'],
                                               newUser['email'], newUser['password'])
        except Exception as err:
            print(err)

    def delete_user(self):
        try:
            userId = inputData.Input.input_id(self.model.tableName)
            self.model.remove_user(userId)
            self.view.display_deletion(userId, self.model.tableName)
        except Exception as err:
            print(err)


class ControllerPost(object):
    def __init__(self, model, view):
        self.model = model()
        self.view = view()

    def show_posts(self):
        posts = self.model.read_posts()
        self.view.show_list_posts(posts)

    def show_post(self):
        postId = inputData.Input.input_id(self.model.tableName)
        posts = self.model.read_post(postId)
        self.view.show_list_posts(posts)

    def show_posts_by_userName(self):
        name = inputData.Input.input_name()
        items = self.model.read_users_posts(name)
        self.view.show_list_users_posts(items)

    def insert_post(self, post):
        try:
            post = inputData.Input.input_update_post(post)
            assert checkData.Check.isPostAttributes(post), 'Some post attribute was not add'
            check = self.model.create_post(post['datetime'], post['title'], post['body'], post['user_id'])
            if check:
                self.view.display_added(post['title'], self.model.tableName)
        except Exception as err:
            print(err)

    def insert_many_posts(self):
        try:
            count = inputData.Input.input_count()
            assert count > 1, '\033[91m count must be more one \033[0m'
            self.model.create_many_posts(count)
            self.view.display_many_added(count, self.model.tableName)
        except Exception as err:
            print(err)

    def update_post(self, post):
        try:
            postId = inputData.Input.input_id(self.model.tableName)
            post = inputData.Input.input_update_post(post)
            old = self.model.read_post(postId)
            newPost = checkData.Check.updatePost(post, old)
            check = self.model.reform(postId, newPost['datetime'], newPost['title'], newPost['body'],
                                      newPost['user_id'])
            if check:
                self.view.display_added(post['title'], self.model.tableName)
        except Exception as err:
            print(err)

    def delete_post(self):
        try:
            userId = inputData.Input.input_id(self.model.tableName)
            self.model.remove_post(userId)
            self.view.display_deletion(userId, self.model.tableName)
        except Exception as err:
            print(err)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()


class ControllerComment(object):
    def __init__(self, model, view):
        self.model = model()
        self.view = view()

    def show_comments(self):
        comments = self.model.read_comments()
        self.view.show_list_comments(comments)

    def show_comment(self):
        commentId = inputData.Input.input_id(self.model.tableName)
        comments = self.model.read_comment(commentId)
        self.view.show_list_comments(comments)

    def show_comments_byDates(self):
        try:
            values = inputData.Input.input_two_values()
            items = self.model.read_comment_byDates(values[0], values[1])
            self.view.show_list_comments_ByDates(items)
        except Exception as err:
            print(err)
            return False

    def insert_comment(self, comment):
        try:
            comment = inputData.Input.input_update_comment(comment)
            assert checkData.Check.isCommentAttributes(comment), 'Some comment attribute was not add'
            check = self.model.create_comment(comment['body'], comment['datetime'], comment['user_id'],
                                              comment['post_id'])
            if check:
                self.view.display_added(comment['body'], self.model.tableName)
        except Exception as err:
            print(err)

    def insert_many_comments(self):
        try:
            count = inputData.Input.input_count()
            assert count > 1, '\033[91m count must be more one \033[0m'
            self.model.create_many_comments(count)
            self.view.display_many_added(count, self.model.tableName)
        except Exception as err:
            print(err)

    def update_comment(self, comment):
        try:
            commentId = inputData.Input.input_id(self.model.tableName)
            comment = inputData.Input.input_update_comment(comment)
            old = self.model.read_comment(commentId)
            newComment = checkData.Check.updateComment(comment, old)
            assert checkData.Check.isCommentAttributes(comment), 'Some comment attribute was not add'
            check = self.model.reform_comment(commentId, newComment['body'], newComment['datetime'],
                                              newComment['user_id'],
                                              newComment['post_id'])
            if check:
                self.view.display_added(comment['body'], self.model.tableName)
        except Exception as err:
            print(err)

    def delete_comment(self):
        try:
            commentId = inputData.Input.input_id(self.model.tableName)
            self.model.remove_comment(commentId)
            self.view.display_deletion(commentId, self.model.tableName)
        except Exception as err:
            print(err)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()


class ControllerPostReaction(object):
    def __init__(self, model, view):
        self.model = model()
        self.view = view()

    def show_post_reactions(self):
        reaction = self.model.read_post_reactions()
        self.view.show_list_post_reactions(reaction)

    def show_post_reaction(self):
        reactionId = inputData.Input.input_id(self.model.tableName)
        reactions = self.model.read_post_reaction(reactionId)
        self.view.show_list_post_reactions(reactions)

    def show_reactions_ByLikeDislike(self):
        value = inputData.Input.input_reaction()
        reactions = self.model.read_reactions_ByLikeDislike(value)
        self.view.show_list_posts_ByLikeDislike(reactions)

    def insert_post_reaction(self, post_reaction):
        try:
            post_reaction = inputData.Input.input_update_post_reaction(post_reaction)
            assert checkData.Check.isPostReactionAttributes(post_reaction), 'Some comment attribute was not add'
            check = self.model.create_post_reaction(post_reaction['value'], post_reaction['datetime'],
                                                    post_reaction['post_id'],
                                                    post_reaction['user_id'])
            if check:
                self.view.display_added(post_reaction['value'], self.model.tableName)
        except Exception as err:
            print(err)

    def insert_random_post_reaction(self):
        try:
            self.model.create_random_post_reaction()
            self.view.display_added('random', self.model.tableName)
        except Exception as err:
            print(err)

    def update_post_reaction(self, post_reaction):
        try:
            post_reactionId = inputData.Input.input_id(self.model.tableName)
            post_reaction = inputData.Input.input_update_post_reaction(post_reaction)
            old = self.model.read_post_reaction(post_reactionId)
            newPost_Reaction = checkData.Check.updatePostReaction(post_reaction, old)
            assert checkData.Check.isPostReactionAttributes(post_reaction), 'Some comment attribute was not add'
            check = self.model.reform_post_reaction(post_reactionId, newPost_Reaction['value'],
                                                    newPost_Reaction['datetime'],
                                                    newPost_Reaction['post_id'],
                                                    newPost_Reaction['user_id'])
            if check:
                self.view.display_added(newPost_Reaction['value'], self.model.tableName)
        except Exception as err:
            print(err)

    def delete_post_reaction(self):
        try:
            post_reactionId = inputData.Input.input_id(self.model.tableName)
            self.model.remove_post_reaction(post_reactionId)
            self.view.display_deletion(post_reactionId, self.model.tableName)
        except Exception as err:
            print(err)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()


class ControllerCommentReaction(object):
    def __init__(self, model, view):
        self.model = model()
        self.view = view()

    def show_comment_reactions(self):
        reaction = self.model.read_comment_reactions()
        self.view.show_list_comment_reactions(reaction)

    def show_comment_reaction(self):
        reactionId = inputData.Input.input_id(self.model.tableName)
        reaction = self.model.read_comment_reaction(reactionId)
        self.view.show_list_comment_reactions(reaction)

    def insert_comment_reaction(self, comment_reaction):
        try:
            comment_reaction = inputData.Input.input_update_comment_reaction(comment_reaction)
            assert checkData.Check.isCommentReactionAttributes(comment_reaction), 'Some comment attribute was not add'
            check = self.model.create_comment_reaction(comment_reaction['value'], comment_reaction['datetime'],
                                                       comment_reaction['comment_id'],
                                                       comment_reaction['user_id'])
            if check:
                self.view.display_added(comment_reaction['value'], self.model.tableName)
        except Exception as err:
            print(err)

    def insert_random_comment_reaction(self):
        try:
            self.model.create_random_comment_reaction()
            self.view.display_added('random', self.model.tableName)
        except Exception as err:
            print(err)

    def update_comment_reaction(self, comment_reaction):
        try:
            comment_reactionId = inputData.Input.input_id(self.model.tableName)
            comment_reaction = inputData.Input.input_update_comment_reaction(comment_reaction)
            old = self.model.read_comment_reaction(comment_reactionId)
            newComment_Reaction = checkData.Check.updateCommentReaction(comment_reaction, old)
            assert checkData.Check.isCommentReactionAttributes(comment_reaction), 'Some comment attribute was not add'
            check = self.model.reform_comment_reaction(comment_reactionId, newComment_Reaction['value'],
                                                       newComment_Reaction['datetime'],
                                                       newComment_Reaction['comment_id'],
                                                       newComment_Reaction['user_id'])
            if check:
                self.view.display_added(newComment_Reaction['value'], self.model.tableName)
        except Exception as err:
            print(err)

    def delete_comment_reaction(self):
        try:
            comment_reactionId = inputData.Input.input_id(self.model.tableName)
            self.model.remove_comment_reaction(comment_reactionId)
            self.view.display_deletion(comment_reactionId, self.model.tableName)
        except Exception as err:
            print(err)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()
