import pytest
from app.schemas.pagination_schema import Pagination, PaginationLink, EnhancedPagination
from pydantic import HttpUrl

# Test Pagination Model
def test_pagination_model():
    page = 1
    per_page = 10
    total_items = 50
    total_pages = 5
    pagination = Pagination(page=page, per_page=per_page, total_items=total_items, total_pages=total_pages)
    
    assert pagination.page == page
    assert pagination.per_page == per_page
    assert pagination.total_items == total_items
    assert pagination.total_pages == total_pages

# Test PaginationLink Model
def test_pagination_link_model():
    rel = "next"
    href = "https://example.com/api/users?page=2"
    pagination_link = PaginationLink(rel=rel, href=href)
    
    assert pagination_link.rel == rel
    assert pagination_link.href == HttpUrl(href)  # Corrected assertion

# Test EnhancedPagination Model
def test_enhanced_pagination_model():
    page = 1
    per_page = 10
    total_items = 50
    total_pages = 5
    links = [
        PaginationLink(rel="next", href="https://example.com/api/users?page=2"),
        PaginationLink(rel="prev", href="https://example.com/api/users?page=1"),
    ]
    enhanced_pagination = EnhancedPagination(page=page, per_page=per_page, total_items=total_items, total_pages=total_pages, links=links)
    
    assert enhanced_pagination.page == page
    assert enhanced_pagination.per_page == per_page
    assert enhanced_pagination.total_items == total_items
    assert enhanced_pagination.total_pages == total_pages
    assert len(enhanced_pagination.links) == 2
