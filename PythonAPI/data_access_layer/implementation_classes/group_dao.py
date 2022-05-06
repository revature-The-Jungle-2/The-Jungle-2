import random

from custom_exceptions import group_id_nonexistent

from custom_exceptions.group_name_already_taken import GroupNameAlreadyTaken
from custom_exceptions.group_not_found import GroupNotFound
from custom_exceptions.user_not_found import UserNotFound
from data_access_layer.abstract_classes.group_dao_abs import GroupDAO
from entities.group import Group
from util.database_connection import connection

schema_prefix = "p3."


class GroupDAOImp(GroupDAO):
    def get_creator(self, group_id: int):
        sql = "select first_name, last_name, username from "+schema_prefix+"user_table inner join "+schema_prefix+"group_table on " \
              +schema_prefix+"group_table.user_id = "+schema_prefix+"user_table.user_id where group_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [group_id])
        creator_record = cursor.fetchmany()
        return creator_record

    def create_group(self, group: Group):

        # Check to see if the user id is in the database, raise an error otherwise.
        sql = "select * from "+schema_prefix+"user_table where user_id = %(user_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"user_id": group.user_id})
        if not cursor.fetchone():
            raise UserNotFound('The user could not be found.')

        # Check to see if there is already a group with the same name, raise an error otherwise
        sql = "select * from "+schema_prefix+"group_table where group_name = %(group_name)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"group_name": group.group_name})
        if cursor.fetchone():
            raise GroupNameAlreadyTaken('That group name has already been taken.')

        # create the group
        sql = "insert into "+schema_prefix+"group_table values(default, %s, %s, %s, %s) returning group_id"
        cursor = connection.cursor()
        cursor.execute(sql, (group.user_id, group.group_name, group.group_about, group.image_format))
        connection.commit()
        group_id = cursor.fetchone()[0]
        group.group_id = group_id

        # add the creator as a member in the junction table
        sql = "insert into "+schema_prefix+"group_member_junction_table values(%s, %s) returning group_id, user_id"
        cursor = connection.cursor()
        cursor.execute(sql, (group_id, group.user_id))
        connection.commit()

        return group

    def join_group(self, group_id: int, user_id: int):
        # Check to see if the user id is in the database, raise an error otherwise.
        sql = "select * from "+schema_prefix+"user_table where user_id = %(user_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"user_id": user_id})
        if not cursor.fetchone():
            raise UserNotFound('The user could not be found.')

        # check if the group exists throw an error otherwise.
        sql = "select * from "+schema_prefix+"group_table where group_id = %(group_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"group_id": group_id})
        if not cursor.fetchone():
            raise GroupNotFound('The group could not be found.')

        sql = "insert into "+schema_prefix+"group_member_junction_table values(%s, %s) returning group_id, user_id"
        cursor = connection.cursor()
        cursor.execute(sql, (group_id, user_id))
        connection.commit()
        return True
