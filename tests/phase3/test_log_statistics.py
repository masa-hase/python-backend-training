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
                'status_code': '200',
                'response_time': '45ms'
            },
            {
                'date': '2024-01-15', 
                'time': '09:45:30',
                'level': 'INFO',
                'status_code': '200',
                'response_time': '67ms'
            },
            {
                'date': '2024-01-15',
                'time': '14:12:15',
                'level': 'ERROR',
                'status_code': '500',
                'response_time': '234ms'
            },
            {
                'date': '2024-01-15',
                'time': '14:30:22',
                'level': 'WARNING',
                'status_code': '404',
                'response_time': '12ms'
            }
        ]
    
    def test_count_by_hour(self, sample_logs):
        """時間帯別のアクセス数集計テスト"""
        # Red: 失敗するテストを先に書く
        stats = LogStatistics(sample_logs)
        result = stats.count_by_hour()
        
        expected = {
            '09': 2,  # 9時台に2件
            '14': 2   # 14時台に2件
        }
        assert result == expected
    
    def test_calculate_peak_hour(self, sample_logs):
        """ピーク時間の特定テスト"""
        stats = LogStatistics(sample_logs)
        peak_hour = stats.calculate_peak_hour()
        
        # 14時台に2件、最多
        assert peak_hour == '14'
        
        # 空のデータの場合
        empty_stats = LogStatistics([])
        assert empty_stats.calculate_peak_hour() == ''
    
    def test_calculate_error_rate_by_hour(self, sample_logs):
        """時間帯別エラー率の計算テスト"""
        stats = LogStatistics(sample_logs)
        error_rates = stats.calculate_error_rate_by_hour()
        
        expected = {
            '09': 0.0,   # 09時台: 2件中0件がエラー
            '14': 100.0  # 14時台: 2件中2件がエラー（ERROR+404）
        }
        assert error_rates == expected
    
    def test_extract_response_times(self, sample_logs):
        """レスポンス時間抽出のテスト"""
        stats = LogStatistics(sample_logs)
        response_times = stats.extract_response_times()
        
        expected = [45, 67, 234, 12]  # ms単位で抽出
        assert response_times == expected
        
        # 不正なデータの場合
        invalid_logs = [{'response_time': 'invalid'}, {'no_response_time': 'test'}]
        invalid_stats = LogStatistics(invalid_logs)
        assert invalid_stats.extract_response_times() == []
    
    def test_calculate_average_response_time(self, sample_logs):
        """平均レスポンス時間計算のテスト"""
        stats = LogStatistics(sample_logs)
        avg_time = stats.calculate_average_response_time()
        
        expected = (45 + 67 + 234 + 12) / 4  # 89.5
        assert avg_time == expected
        
        # 空のデータの場合
        empty_stats = LogStatistics([])
        assert empty_stats.calculate_average_response_time() == 0.0
    
    def test_calculate_response_time_percentiles(self, sample_logs):
        """レスポンス時間パーセンタイル計算のテスト"""
        stats = LogStatistics(sample_logs)
        percentiles = stats.calculate_response_time_percentiles()
        
        # ソート済み: [12, 45, 67, 234]
        assert 'p50' in percentiles
        assert 'p90' in percentiles  
        assert 'p95' in percentiles
        
        # 50%は中央値付近
        assert 45 <= percentiles['p50'] <= 67
        
        # 空のデータの場合
        empty_stats = LogStatistics([])
        empty_percentiles = empty_stats.calculate_response_time_percentiles()
        assert empty_percentiles == {'p50': 0.0, 'p90': 0.0, 'p95': 0.0}