from custom_exceptions.connection_error import ConnectionErrorr
from data_access_layer.abstract_classes.like_post_dao_abs import LikePostDAO
from util.database_connection import connection


class LikePostDaoImp(LikePostDAO):
    def like_post(self,post_id:int):
            sql = "update post_table set likes = likes + 1 where post_id=%s returning likes"
            cursor = connection.cursor()
            cursor.execute(sql,[post_id])
            connection.commit()
            generated_likes_number = cursor.fetchone()[0]
            if  generated_likes_number > 0:
                     return generated_likes_number

            else:
                raise ConnectionErrorr('post not found')

    def like_comment(self, comment_id: int):
            sql = "update comment_table set likes = likes + 1 where comment_id=%s returning likes"
            cursor = connection.cursor()
            cursor.execute(sql, [comment_id])
            connection.commit()
            generated_likes_number = cursor.fetchone()[0]
            if generated_likes_number > 0:
                return generated_likes_number

            else:
                raise ConnectionErrorr('comment not found')
