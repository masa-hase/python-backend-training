"""
レスポンス時間統計のTDDテスト

【課題3】レスポンス時間統計をTDDで実装してください
"""

import pytest
from src.phase3.log_statistics import LogStatistics


class TestResponseTimeStatistics:
    """レスポンス時間統計のテスト"""
    
    @pytest.fixture
    def response_time_logs(self):
        """レスポンス時間付きログデータ"""
        return [
            {'message': '45ms', 'status': '200'},
            {'message': '67ms', 'status': '200'},
            {'message': '234ms', 'status': '500'},
            {'message': '12ms', 'status': '200'},
            {'message': '456ms', 'status': '500'}
        ]
    
    def test_extract_response_times(self, response_time_logs):
        """レスポンス時間の抽出テスト"""
        stats = LogStatistics(response_time_logs)
        times = stats.extract_response_times()
        
        expected = [45, 67, 234, 12, 456]
        assert times == expected
    
    def test_calculate_average_response_time(self, response_time_logs):
        """平均レスポンス時間の計算テスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_calculate_response_time_percentiles(self, response_time_logs):
        """レスポンス時間のパーセンタイル計算テスト"""
        # TODO: TDDで実装してください
        # ヒント: 50%, 90%, 95%のパーセンタイルを計算
        pass