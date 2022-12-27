import model
import view
import consoleView
import controller


def main():
    user = controller.ConrtrollerUser(model.ModelUser, view.View)
    post = controller.ControllerPost(model.ModelPost, view.View)
    comment = controller.ControllerComment(model.ModelComment, view.View)
    post_reaction = controller.ControllerPostReaction(model.ModelPost_Reaction, view.View)
    comment_reaction = controller.ControllerCommentReaction(model.ModelComment_Reaction, view.View)
    consoleView.menu(user, post, comment, post_reaction, comment_reaction)
    user.disconnect()
    post.disconnect()
    comment.disconnect()
    post_reaction.disconnect()
    comment_reaction.disconnect()


if __name__ == '__main__':
    main()
