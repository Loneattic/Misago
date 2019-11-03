import pytest

from ...database.queries import insert
from ...tables import cache_versions


@pytest.fixture
async def cache_version(db):
    await insert(cache_versions, cache="test_cache", version="version")
    return {"cache": "test_cache", "version": "version"}