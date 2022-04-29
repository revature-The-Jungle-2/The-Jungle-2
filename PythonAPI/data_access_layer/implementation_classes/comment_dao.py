from typing import List

from custom_exceptions.comment_not_found import CommentNotFound
from custom_exceptions.post_not_found import PostNotFound
from data_access_layer.abstract_classes.comment_dao_abs import CommentDAO
from entities.comment import Comment
from entities.returned_comment import ReturnedComment
from util.database_connection import connection


class CommentDAOImp(CommentDAO):

    def create_comment(self, post_id: int, user_id: int, comment_text: str, group_id: int, reply_user: int) -> Comment:
        # Check to see if the post id is in the database, raise an error otherwise.
        sql = f"select * from post_table where post_id = %(post_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"post_id": post_id})
        if not cursor.fetchone():
            raise PostNotFound('The post could not be found.')

        sql = "insert into comment_table values(default, %s, %s, %s, %s, %s, %s, default) returning comment_id "
        cursor = connection.cursor()
        cursor.execute(sql, (post_id, user_id, group_id, reply_user, comment_text, 0))
        connection.commit()
        generated_id = cursor.fetchone()[0]

        # Grab the newly created comment from the table
        sql = "select * from comment_table where comment_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (generated_id,))
        comment_record = cursor.fetchone()
        return Comment(*comment_record)

    def get_comment_by_post_id(self, post_id: int) -> List[ReturnedComment]:
        # Check to see if the post id is in the database, raise an error otherwise.
        sql = f"select * from post_table where post_id = %(post_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"post_id": post_id})
        if not cursor.fetchone():
            raise PostNotFound('The post could not be found.')

        sql = "select ct.comment_id, ct.post_id, ct.user_id , ct.group_id, ct.username, ct.comment_text, ct.likes, " \
              "ct.date_time_of_creation, ut.username from comment_table as ct inner join user_table as ut " \
              "on ct.user_id = ut.user_id where post_id = %s;"
        cursor = connection.cursor()
        cursor.execute(sql, [post_id])
        comment_record = cursor.fetchall()
        comment_list = []
        for comments in comment_record:
            comment_list.append(ReturnedComment(*comments))
        return comment_list

    def delete_comment(self, comment_id: int) -> bool:
        # Check to see if the comment id is in the database, raise an error otherwise.
        sql = f"select * from comment_table where comment_id = %(comment_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"comment_id": comment_id})
        if not cursor.fetchone():
            raise CommentNotFound("Comment Not Found")

        sql = "delete from comment_table where comment_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [comment_id])
        connection.commit()
        return True
