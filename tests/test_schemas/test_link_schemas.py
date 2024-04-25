import pytest
from app.schemas.link_schema import Link
from pydantic import ValidationError

def test_link_model():
    # Valid link data
    rel = "self"
    href = "https://api.example.com/qr/123"
    action = "GET"
    link_type = "application/json"

    # Create a link instance
    link = Link(rel=rel, href=href, action=action, type=link_type)

    # Validate the fields
    assert link.rel == rel
    assert str(link.href) == href  # Convert Url object to string for comparison
    assert link.action == action
    assert link.type == link_type
