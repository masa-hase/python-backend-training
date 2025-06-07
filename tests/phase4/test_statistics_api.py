"""
統計APIのテスト

【課題5】統計機能をTDDで実装してください
"""

import pytest
from fastapi.testclient import TestClient
from src.phase4.main import app

client = TestClient(app)


class TestStatisticsAPI:
    """統計APIのテスト"""
    
    def test_get_hourly_statistics(self):
        """時間帯別統計取得のテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_get_response_time_statistics(self):
        """レスポンス時間統計取得のテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_get_error_statistics(self):
        """エラー統計取得のテスト"""
        # TODO: TDDで実装してください
        pass