from typing import List

import pytest

from custom_exceptions.post_exceptions import InvalidInput, InputTooLong, NoInputGiven, WrongTypeInput
from data_access_layer.implementation_classes.group_post_dao import GroupPostDAO
from entities.group_post import GroupPost
from service_layer.abstract_classes.group_post_service_abs import GroupPostServiceAbs


class GroupPostService(GroupPostServiceAbs):
    def __init__(self, post_dao: GroupPostDAO):
        self.post_dao = post_dao

    def service_create_post(self, post: GroupPost) -> GroupPost:
        if post.user_id <= 0:
            raise InvalidInput("Invalid Input!")
        if type(post.post_id) != int:
            raise WrongTypeInput("You need to enter number for post ID!")
        if post.post_text == "":
            raise NoInputGiven("No Input Given!")
        if len(post.post_text) > 500:
            raise InputTooLong("Messages too long!")
        return self.post_dao.create_post(post)

    def service_create_post_image(self, image: str) -> bool:
        pass

    def service_get_post_by_id(self, post_id: int) -> GroupPost:
        return self.post_dao.get_post_by_id(post_id)

    def service_get_all_posts(self) -> List[GroupPost]:
        return self.post_dao.get_all_posts()

    def service_get_all_posts_by_group_id(self, group_id: int) -> List[GroupPost]:
        return self.post_dao.get_all_posts_by_group_id(group_id)

    def service_delete_post_by_post_id(self, post_id: int) -> bool:
        return self.post_dao.delete_post_by_post_id(post_id)
