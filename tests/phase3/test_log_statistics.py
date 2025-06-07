"""
ログ統計機能のTDDテスト

【課題2】時間帯別統計機能をTDDで実装してください
"""

import pytest
from src.phase3.log_statistics import LogStatistics


class TestLogStatistics:
    """ログ統計のテストクラス"""
    
    @pytest.fixture
    def sample_logs(self):
        """テスト用のログデータ"""
        return [
            {
                'date': '2024-01-15',
                'time': '09:23:45',
                'level': 'INFO',
                'status': '200',
                'message': '45ms'
            },
            {
                'date': '2024-01-15', 
                'time': '09:45:30',
                'level': 'INFO',
                'status': '200',
                'message': '67ms'
            },
            {
                'date': '2024-01-15',
                'time': '14:12:15',
                'level': 'ERROR',
                'status': '500',
                'message': '234ms'
            }
        ]
    
    def test_count_by_hour(self, sample_logs):
        """時間帯別のアクセス数集計テスト"""
        # Red: 失敗するテストを先に書く
        stats = LogStatistics(sample_logs)
        result = stats.count_by_hour()
        
        expected = {
            '09': 2,  # 9時台に2件
            '14': 1   # 14時台に1件
        }
        assert result == expected
    
    def test_calculate_peak_hour(self, sample_logs):
        """ピーク時間の特定テスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_calculate_error_rate_by_hour(self, sample_logs):
        """時間帯別エラー率の計算テスト"""
        # TODO: TDDで実装してください
        pass