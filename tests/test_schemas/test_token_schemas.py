import pytest
from app.schemas.token_schemas import Token, TokenData, RefreshTokenRequest
from pydantic import ValidationError

@pytest.fixture
def sample_token_data():
    return {
        "access_token": "sample_access_token",
        "token_type": "bearer"
    }

@pytest.fixture
def sample_token_data_invalid():
    return {
        "access_token": None,
        "token_type": "bearer"
    }

@pytest.fixture
def sample_token_data_empty():
    return {}

@pytest.fixture
def sample_tokendata_data():
    return {
        "username": "user@example.com"
    }

@pytest.fixture
def sample_tokendata_data_invalid():
    return {
        "username": None
    }

@pytest.fixture
def sample_refresh_token_request():
    return {
        "refresh_token": "sample_refresh_token"
    }

@pytest.fixture
def sample_refresh_token_request_invalid():
    return {
        "refresh_token": None
    }

def test_token_model(sample_token_data):
    token = Token(**sample_token_data)
    assert token.access_token == sample_token_data["access_token"]
    assert token.token_type == sample_token_data["token_type"]

def test_token_model_empty(sample_token_data_empty):
    with pytest.raises(ValueError):
        Token(**sample_token_data_empty)

def test_tokendata_model(sample_tokendata_data):
    tokendata = TokenData(**sample_tokendata_data)
    assert tokendata.username == sample_tokendata_data["username"]

def test_refreshtokenrequest_model(sample_refresh_token_request):
    refresh_token_request = RefreshTokenRequest(**sample_refresh_token_request)
    assert refresh_token_request.refresh_token == sample_refresh_token_request["refresh_token"]

def test_refreshtokenrequest_model_invalid(sample_refresh_token_request_invalid):
    with pytest.raises(ValueError):
        RefreshTokenRequest(**sample_refresh_token_request_invalid)
