from abc import ABC, abstractmethod
from typing import List

from entities.comment import Comment
from entities.returned_comment import ReturnedComment


class CommentDAO(ABC):

    # create reimbursement request
    @abstractmethod
    def create_comment(self, post_id: int, user_id: int, comment_text: str, group_id: int, reply_user: int) -> Comment:
        pass

    # get all comments by post id
    @abstractmethod
    def get_comment_by_post_id(self, post_id: int) -> List[ReturnedComment]:
        pass

    # delete comment
    @abstractmethod
    def delete_comment(self, comment_id: int) -> bool:
        pass
