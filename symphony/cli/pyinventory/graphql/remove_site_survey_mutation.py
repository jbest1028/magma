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


@dataclass
class RemoveSiteSurveyMutation(DataClassJsonMixin):
    @dataclass
    class RemoveSiteSurveyMutationData(DataClassJsonMixin):
        removeSiteSurvey: str

    data: RemoveSiteSurveyMutationData

    __QUERY__: str = """
    mutation RemoveSiteSurveyMutation($id: ID!) {
  removeSiteSurvey(id: $id)
}

    """

    @classmethod
    # fmt: off
    def execute(cls, client: GraphqlClient, id: str) -> RemoveSiteSurveyMutationData:
        # fmt: off
        variables = {"id": id}
        response_text = client.call(cls.__QUERY__, variables=variables)
        return cls.from_json(response_text).data
