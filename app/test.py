def test_city():
    query = """
        query TestCity($title: String!) {
            weather(title: $title) {
                city
            }
        }
    """

    result = main.execute_sync(
        query,
        variable_values={"city": "Florence"},
    )

    assert result.errors is None
    
@pytest.mark.asyncio
async def test_mutation():
    mutation = """
        mutation TestMutation($title: String!, $author: String!) {
            addFavorite(title: $title, author: $author) {
                city
            }
        }
    """

    resp = await main.execute(
        mutation,
        variable_values={
            "city": "Florence",
        },
    )

    assert resp.errors is None
    assert resp.data["addFavorite"] == {
        "city": "Florence",
    }