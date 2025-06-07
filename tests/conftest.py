"""
pytest設定とフィクスチャ

共通的に使用するテストデータやセットアップを定義します。
Phase毎に使用するフィクスチャを整理しています。
"""

import pytest
import tempfile
import os
from typing import List, Dict


# Phase 2以降で使用する共通フィクスチャ
@pytest.fixture
def sample_log_data():
    """テスト用のサンプルログデータ"""
    return [
        {
            'date': '2024-01-15',
            'time': '09:23:45',
            'level': 'INFO',
            'method': 'GET',
            'path': '/api/users',
            'status': '200',
            'message': '45ms',
            'raw_line': '2024-01-15 09:23:45 INFO GET /api/users 200 45ms'
        },
        {
            'date': '2024-01-15',
            'time': '09:24:33',
            'level': 'ERROR',
            'method': 'GET',
            'path': '/api/data',
            'status': '500',
            'message': 'Database connection failed',
            'raw_line': '2024-01-15 09:24:33 ERROR GET /api/data 500 234ms Database connection failed'
        },
        {
            'date': '2024-01-15',
            'time': '09:25:15',
            'level': 'WARNING',
            'method': 'GET',
            'path': '/api/reports',
            'status': '404',
            'message': 'Resource not found',
            'raw_line': '2024-01-15 09:25:15 WARNING GET /api/reports 404 12ms Resource not found'
        }
    ]


@pytest.fixture
def temp_log_file():
    """一時的なログファイルを作成（Phase 2以降で使用）"""
    # TODO: 学習者が実装してください
    # ヒント: tempfile.NamedTemporaryFile を使用し、yield でファイルパスを返す
    pass


@pytest.fixture
def temp_csv_file():
    """一時的なCSVファイルパスを提供（Phase 2以降で使用）"""
    # TODO: 学習者が実装してください
    pass