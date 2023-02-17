import asyncio
import pytest
import strawberry
from fastapi import FastAPI
from fastapi.testclient import TestClient
from .app import Query, Mutation, CheckFav
from .__init__ import schema

@pytest.mark.asyncio
async def test_query_async():
    ...

    resp = await schema.execute(Query, variable_values={"city": "Paris"})

    ...

@pytest.mark.asyncio
async def test_mutation():
    mutation = """
        mutation TestMutation($title: String!, $author: String!) {
            addBook(title: $title, author: $author) {
                title
            }
        }
    """

    resp = await schema.execute(
        mutation,
        variable_values={
            "city": "London",
        },
    )

    assert resp.errors is None
    assert resp.data["addBook"] == {
        "title": "The Little Prince",
    }