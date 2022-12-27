class View(object):

    @staticmethod
    def show_list_users(users):
        if (users):
            print("---------------------------Users---------------------------")
            print("|UserId|", "Name|", "Phone Number|", "  Email  |", "Password  |")
            for row in users:
                print("| ", row[0], " |", row[1], "|", row[2], "|", row[3], "|", row[4], "|")
            print("-----------------------------------------------------------")
        else:
            print("There is nothing with this id")

    @staticmethod
    def show_list_posts(posts):
        if (posts):
            print("-----------------------------------------Posts---------------------------------------")
            print("|PostId|", "         Time         |", "   Title    |", "      Body       |", "UserId|")
            for row in posts:
                print("| ", row[0], " |", row[1], "|", row[2], "|", row[3], "|", row[4], "|")
            print("-------------------------------------------------------------------------------------")
        else:
            print("There is nothing with this id")

    @staticmethod
    def show_list_comments(comments):
        if (comments):
            print("--------------------------------------Comments---------------------------------------")
            print("|commentId|", "  Body  |", "          datetime             |", "userId|", "postId|")
            for row in comments:
                print("| ", row[0], " |", row[1], "|", row[2], "|", row[3], "|", row[4], "|")
            print("-------------------------------------------------------------------------------------")
        else:
            print("There is nothing with this id")

    @staticmethod
    def show_list_post_reactions(post_reactions):
        if (post_reactions):
            print("-----------------------------------PostReaction-------------------------------------------")
            print("|reactionId|", " value  |", "          datetime             |", "postId|", "userId|")
            for row in post_reactions:
                print("| ", row[0], " |", row[1], "|", row[2], "|", row[3], "|", row[4], "|")
            print("------------------------------------------------------------------------------------------")
        else:
            print("There is nothing with this id")

    @staticmethod
    def show_list_comment_reactions(comment_reactions):
        if (comment_reactions):
            print("--------------------------------CommentReaction-------------------------------------------")
            print("|reactionId|", " value  |", "          datetime             |", "commentId|", "userId|")
            for row in comment_reactions:
                print("| ", row[0], " |", row[1], "|", row[2], "|", row[3], "|", row[4], "|")
            print("------------------------------------------------------------------------------------------")
        else:
            print("There is nothing with this id")

    @staticmethod
    def delete_connection():
        print('**************************************************************')
        print("PostgresSQL connection is closed")
        print('**************************************************************')

    @staticmethod
    def display_added(name, tableName):
        print('\033[92m++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Hooray! You create new {} - {} to our {} list!'
              .format(tableName.lower(), name, tableName))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_many_added(count, tableName):
        print('\033[92m++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Hooray! You create new {} random rows to our {} list!'
              .format(count, tableName))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_deletion(anyId, tableName):
        print('--------------------------------------------------------------')
        print('You have just deleted row with id:{} from table {}'
              .format(anyId, tableName))
        print('--------------------------------------------------------------')

    @staticmethod
    def display_user_updated(userId, oldName, oldPhone, oldEmail, oldPassword, newName, newPhone, newEmail,
                             newPassword):
        print('--------------------------------------------------------------')
        print('Change {} name: {} --> {}'
              .format(userId, oldName, newName))
        print('Change {} phone: {} --> {}'
              .format(userId, oldPhone, newPhone))
        print('Change {} email: {} --> {}'
              .format(userId, oldEmail, newEmail))
        print('Change {} password: {} --> {}'
              .format(userId, oldPassword, newPassword))
        print('--------------------------------------------------------------')

    @staticmethod
    def show_list_users_posts(items):
        if items:
            print("--------------------------------------Users+Posts---------------------------------------")
            print("|post_d|", "User_id|", "name     |", "  title   |", "  body   |", "    datetime        |")
            for row in items:
                print("|", row[0], "\t|", row[1], "\t|", row[2],
                      "|", row[3], "|", row[4], "\t|", row[5],
                      "|")
            print("----------------------------------------------------------------------------------------")
        else:
            print("There is nothing with this id")

    @staticmethod
    def show_list_posts_ByLikeDislike(items):
        if items:
            print("--------------------------------------PostReaction+Posts---------------------------------------")
            print("|user_d|", "post_id|", "reaction     |", "  title   |", "  body   |", "    datetime        |")
            for row in items:
                print("|", row[0], "\t|", row[1], "\t|", row[2],
                      "|", row[3], "|", row[4], "\t|", row[5],
                      "|")
            print("----------------------------------------------------------------------------------------")
        else:
            print("There is nothing with this id")

    @staticmethod
    def show_list_comments_ByDates(items):
        if items:
            print("-----------------------------------------Users+Comments---------------------------------------")
            print("|user_id|", " name   |", "post_id|", "  body   |", "      datetime      |", "   comment_id   |")
            for row in items:
                print("|", row[0], "\t|", row[1], "\t|", row[2],
                      "|", row[3], "|", row[4], "\t|", row[5],
                      "|")
            print("---------------------------------------------------------------------------------------------")
        else:
            print("There is nothing with this id")