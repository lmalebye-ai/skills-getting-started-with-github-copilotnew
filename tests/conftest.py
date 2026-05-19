from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Keep tests isolated because the API mutates a global in-memory store."""
    original = deepcopy(activities)
    yield
    activities.clear()
    activities.update(original)
