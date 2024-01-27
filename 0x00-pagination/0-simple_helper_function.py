#!/usr/bin/env python3
""" simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indexes for pagination.
      """
    if page <= 0 or page_size <= 0:
        raise ValueError(
            "Both page and page_size should be positive integers.")

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
