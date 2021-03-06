#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from dataclasses import dataclass
from datetime import datetime
from gql.gql.datetime_utils import DATETIME_FIELD
from gql.gql.graphql_client import GraphqlClient
from functools import partial
from numbers import Number
from typing import Any, Callable, List, Mapping, Optional

from dataclasses_json import DataClassJsonMixin

from gql.gql.enum_utils import enum_field
from .user_role_enum import UserRole
from .user_status_enum import UserStatus


@dataclass
class UsersQuery(DataClassJsonMixin):
    @dataclass
    class UsersQueryData(DataClassJsonMixin):
        @dataclass
        class UserConnection(DataClassJsonMixin):
            @dataclass
            class UserEdge(DataClassJsonMixin):
                @dataclass
                class User(DataClassJsonMixin):
                    id: str
                    authID: str
                    email: str
                    status: UserStatus = enum_field(UserStatus)
                    role: UserRole = enum_field(UserRole)

                node: Optional[User] = None

            edges: List[UserEdge]

        users: Optional[UserConnection] = None

    data: UsersQueryData

    __QUERY__: str = """
    query UsersQuery {
  users {
    edges {
      node {
        id
        authID
        email
        status
        role
      }
    }
  }
}

    """

    @classmethod
    # fmt: off
    def execute(cls, client: GraphqlClient) -> UsersQueryData:
        # fmt: off
        variables = {}
        response_text = client.call(cls.__QUERY__, variables=variables)
        return cls.from_json(response_text).data
