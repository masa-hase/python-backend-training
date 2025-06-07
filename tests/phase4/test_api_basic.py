"""
基本的なAPIテスト

【課題2】APIのテストをTDDで実装してください
"""

import pytest
from fastapi.testclient import TestClient
from src.phase4.main import app

client = TestClient(app)


class TestBasicAPI:
    """基本APIのテスト"""
    
    def test_root_endpoint(self):
        """ルートエンドポイントのテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_health_check(self):
        """ヘルスチェックのテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_get_logs_endpoint(self):
        """ログ取得エンドポイントのテスト"""
        # TODO: TDDで実装してください
        pass