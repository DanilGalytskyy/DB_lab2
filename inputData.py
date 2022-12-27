class Input(object):

    @staticmethod
    def input_update_user(user):
        inputName = input("Enter user name: ")
        inputPhone = input("Enter user phone number: ")
        inputEmail = input("Enter user email: ")
        inputPassword = input("Enter user password: ")
        return {
            'name': inputName,
            'phone_number': inputPhone,
            'email': inputEmail,
            'password': inputPassword
        }

    @staticmethod
    def input_update_post(post):
        inputDate = input("Enter post date: ")
        inputTitle = input("Enter post title: ")
        inputBody = input("Enter post body: ")
        inputUser_id = input("Enter user_id: ")
        return {
            'datetime': inputDate,
            'title': inputTitle,
            'body': inputBody,
            'user_id': inputUser_id
        }

    @staticmethod
    def input_update_comment(comment):
        inputBody = input("Enter comment: ")
        inputDate = input("Enter comment date: ")
        inputUser_id = input("Enter user_id: ")
        inputPost_id = input("Enter post_id: ")
        return {
            'body': inputBody,
            'datetime': inputDate,
            'user_id': inputUser_id,
            'post_id': inputPost_id
        }

    @staticmethod
    def input_update_post_reaction(post_reaction):
        inputValue = input("Enter value: ")
        inputDate = input("Enter reaction date: ")
        inputPost_id = input("Enter post_id: ")
        inputUser_id = input("Enter user_id: ")
        return {
            'value': inputValue,
            'datetime': inputDate,
            'post_id': inputPost_id,
            'user_id': inputUser_id
        }

    @staticmethod
    def input_update_comment_reaction(comment_reaction):
        inputValue = input("Enter value: ")
        inputDate = input("Enter reaction date: ")
        inputComment_id = input("Enter comment_id: ")
        inputUser_id = input("Enter user_id: ")
        return {
            'value': inputValue,
            'datetime': inputDate,
            'comment_id': inputComment_id,
            'user_id': inputUser_id
        }

    @staticmethod
    def input_id(tableName):
        inputId = input("Enter {} id: ".format(tableName))
        return inputId

    @staticmethod
    def input_name():
        inputName = input("Enter name of user ")
        return inputName

    @staticmethod
    def input_reaction():
        inputReact = input("Enter like or dislike: ")
        if inputReact == 'like':
            inputReact = 'true'
            return inputReact
        elif inputReact == 'dislike':
            inputReact = 'false'
            return inputReact

    @staticmethod
    def input_count():
        inputCount = input("Enter more than 1 random row: ")
        return int(inputCount)

    @staticmethod
    def input_two_values():
        firstValue = input("Enter start date: ")
        secondValue = input("Enter finish date: ")
        return [firstValue, secondValue]
