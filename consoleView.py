from consolemenu import *
from consolemenu.items import *


def menu(user, post, comment, post_reaction, comment_reaction):
    newUser = {
        'name': "Danylo",
        'phone_number': "+380669286120",
        'email': "galytskyyd@gmail.com",
        'password': "qwerty123"
    }
    newPost = {
        'datetime': "2022-12-02",
        'title': "Blog",
        'body': "I am good",
        'user_id': "1"
    }
    newComment = {
        'body': "I am good",
        'datetime': "2022-12-02",
        'user_id': "7",
        'post_id': "2"
    }
    newPostReaction = {
        'value': "False",
        'datetime': "2022-12-02",
        'post_id': "7",
        'user_id': "2"
    }

    newCommentReaction = {
        'value': "False",
        'datetime': "2022-12-02",
        'comment_id': "1",
        'user_id': "7"
    }
    mainMenu = ConsoleMenu("BD Blog")
    menu_user = ConsoleMenu("User")
    menu_post = ConsoleMenu("Post")
    menu_comment = ConsoleMenu("Comment")
    menu_post_reaction = ConsoleMenu("Post_Reaction")
    menu_comment_reaction = ConsoleMenu("Comment_Reaction")

    function_insert_user = FunctionItem("Create user", user.insert_user, [newUser])
    function_insert_many_user = FunctionItem("Create many random users", user.insert_many_users, [])
    function_show_users = FunctionItem("Show Users", user.show_users, [])
    function_show_user = FunctionItem("Show User", user.show_user, [])
    function_update_user = FunctionItem("Update User", user.update_user, [newUser])
    function_delete_user = FunctionItem("Delete User", user.delete_user, [])
    menu_user.append_item(function_insert_user)
    menu_user.append_item(function_insert_many_user)
    menu_user.append_item(function_show_user)
    menu_user.append_item(function_show_users)
    menu_user.append_item(function_update_user)
    menu_user.append_item(function_delete_user)

    function_show_post = FunctionItem("Show Post", post.show_post, [])
    function_show_posts = FunctionItem("Show Posts", post.show_posts, [])
    function_show_posts_by_username = FunctionItem("Show Posts by UserName", post.show_posts_by_userName, [])
    function_insert_post = FunctionItem("Create Post", post.insert_post, [newPost])
    function_insert_many_posts = FunctionItem("Create random Posts", post.insert_many_posts, [])
    function_update_post = FunctionItem("Update Post", post.update_post, [newPost])
    function_delete_post = FunctionItem("Delete Post", post.delete_post, [])
    menu_post.append_item(function_show_post)
    menu_post.append_item(function_show_posts)
    menu_post.append_item(function_show_posts_by_username)
    menu_post.append_item(function_insert_post)
    menu_post.append_item(function_insert_many_posts)
    menu_post.append_item(function_update_post)
    menu_post.append_item(function_delete_post)

    function_show_comments = FunctionItem("Show Comments", comment.show_comments, [])
    function_show_comment = FunctionItem("Show Comment", comment.show_comment, [])
    function_show_comment_byDate = FunctionItem("Show Comments and User by date", comment.show_comments_byDates, [])
    function_insert_comment = FunctionItem("Create Comment", comment.insert_comment, [newComment])
    function_insert_many_comment = FunctionItem("Create random Comments", comment.insert_many_comments, [])
    function_update_comment = FunctionItem("Update Comment", comment.update_comment, [newComment])
    function_delete_comment = FunctionItem("Delete Comment", comment.delete_comment, [])
    menu_comment.append_item(function_show_comments)
    menu_comment.append_item(function_show_comment)
    menu_comment.append_item(function_show_comment_byDate)
    menu_comment.append_item(function_insert_comment)
    menu_comment.append_item(function_insert_many_comment)
    menu_comment.append_item(function_update_comment)
    menu_comment.append_item(function_delete_comment)

    function_show_post_reactions = FunctionItem("Show Post reactions", post_reaction.show_post_reactions, [])
    function_show_post_reaction = FunctionItem("Show Post reaction", post_reaction.show_post_reaction, [])
    function_show_post_reactions_byLikeDislike = FunctionItem("Show reactions by Likes/Dislikes",
                                                              post_reaction.show_reactions_ByLikeDislike, [])
    function_insert_post_reaction = FunctionItem("Create Post reaction", post_reaction.insert_post_reaction,
                                                 [newPostReaction])
    function_random_post_reaction = FunctionItem("Create random Post reaction",
                                                 post_reaction.insert_random_post_reaction, [])
    function_update_post_reaction = FunctionItem("Update Post reaction", post_reaction.update_post_reaction,
                                                 [newPostReaction])
    function_delete_post_reaction = FunctionItem("Delete Post reaction", post_reaction.delete_post_reaction, [])
    menu_post_reaction.append_item(function_show_post_reactions)
    menu_post_reaction.append_item(function_show_post_reaction)
    menu_post_reaction.append_item(function_show_post_reactions_byLikeDislike)
    menu_post_reaction.append_item(function_insert_post_reaction)
    menu_post_reaction.append_item(function_random_post_reaction)
    menu_post_reaction.append_item(function_update_post_reaction)
    menu_post_reaction.append_item(function_delete_post_reaction)

    function_show_comment_reactions = FunctionItem("Show Comment reactions", comment_reaction.show_comment_reactions,
                                                   [])
    function_show_comment_reaction = FunctionItem("Show Comment reaction", comment_reaction.show_comment_reaction, [])
    function_insert_comment_reaction = FunctionItem("Create Comment reaction", comment_reaction.insert_comment_reaction,
                                                    [newCommentReaction])
    function_random_comment_reaction = FunctionItem("Create random Comment reaction",
                                                    comment_reaction.insert_random_comment_reaction, [])
    function_update_comment_reaction = FunctionItem("Update Comment reaction", comment_reaction.update_comment_reaction,
                                                    [newCommentReaction])
    function_delete_comment_reaction = FunctionItem("Delete Comment reaction", comment_reaction.delete_comment_reaction,
                                                    [])

    menu_comment_reaction.append_item(function_show_comment_reactions)
    menu_comment_reaction.append_item(function_show_comment_reaction)
    menu_comment_reaction.append_item(function_insert_comment_reaction)
    menu_comment_reaction.append_item(function_random_comment_reaction)
    menu_comment_reaction.append_item(function_update_comment_reaction)
    menu_comment_reaction.append_item(function_delete_comment_reaction)

    submenu_user = SubmenuItem("User", menu_user, mainMenu)
    submenu_post = SubmenuItem("Post", menu_post, mainMenu)
    submenu_comment = SubmenuItem("Comment", menu_comment, mainMenu)
    submenu_post_reactions = SubmenuItem("Post reactions", menu_post_reaction, mainMenu)
    submenu_comment_reactions = SubmenuItem("Comment reactions", menu_comment_reaction, mainMenu)
    mainMenu.append_item(submenu_user)
    mainMenu.append_item(submenu_post)
    mainMenu.append_item(submenu_comment)
    mainMenu.append_item(submenu_post_reactions)
    mainMenu.append_item(submenu_comment_reactions)
    mainMenu.show()
