"""
ログ統計分析機能

【課題2-3】TDDで実装してください

実装手順:
1. test_log_statistics.py のテストを実行して失敗を確認
2. テストを通すための最小限のコードを実装
3. コードを整理・改善
"""

from typing import List, Dict, Any
from collections import defaultdict


class LogStatistics:
    """ログの統計分析を行うクラス"""
    
    def __init__(self, log_data: List[Dict[str, Any]]):
        """
        初期化
        
        Args:
            log_data: 解析対象のログデータ
        """
        self.log_data = log_data
    
    def count_by_hour(self) -> Dict[str, int]:
        """時間帯別のアクセス数を集計"""
        hour_counts = defaultdict(int)
        
        for log in self.log_data:
            if 'time' in log:
                # "09:23:45" 形式から時間を抽出
                time_str = log['time']
                hour = time_str.split(':')[0]  # 最初の2桁が時間
                hour_counts[hour] += 1
                
        return dict(hour_counts)
    
    def calculate_peak_hour(self) -> str:
        """最もアクセスが多い時間帯を特定"""
        hour_counts = self.count_by_hour()
        
        if not hour_counts:
            return ""
            
        # 最大値を持つ時間を返す
        peak_hour = max(hour_counts.items(), key=lambda x: x[1])[0]
        return peak_hour
    
    def calculate_error_rate_by_hour(self) -> Dict[str, float]:
        """時間帯別のエラー率を計算"""
        hour_total = defaultdict(int)
        hour_errors = defaultdict(int)
        
        for log in self.log_data:
            if 'time' in log:
                hour = log['time'].split(':')[0]
                hour_total[hour] += 1
                
                # エラーとみなす条件
                if (log.get('level') == 'ERROR' or 
                    (log.get('status_code', '').startswith('4') or 
                     log.get('status_code', '').startswith('5'))):
                    hour_errors[hour] += 1
        
        error_rates = {}
        for hour in hour_total:
            error_rates[hour] = (hour_errors[hour] / hour_total[hour]) * 100
            
        return error_rates
    
    def extract_response_times(self) -> List[int]:
        """レスポンス時間を抽出してリストで返す"""
        response_times = []
        
        for log in self.log_data:
            if 'response_time' in log:
                time_str = log['response_time']
                # "45ms" 形式から数値を抽出
                if time_str.endswith('ms'):
                    try:
                        time_value = int(time_str[:-2])  # "ms"を除去
                        response_times.append(time_value)
                    except ValueError:
                        continue  # 解析できない場合はスキップ
                        
        return response_times
    
    def calculate_average_response_time(self) -> float:
        """平均レスポンス時間を計算"""
        response_times = self.extract_response_times()
        
        if not response_times:
            return 0.0
            
        return sum(response_times) / len(response_times)
    
    def calculate_response_time_percentiles(self) -> Dict[str, float]:
        """レスポンス時間のパーセンタイル（50%, 90%, 95%）を計算"""
        response_times = self.extract_response_times()
        
        if not response_times:
            return {'p50': 0.0, 'p90': 0.0, 'p95': 0.0}
            
        sorted_times = sorted(response_times)
        n = len(sorted_times)
        
        def percentile(data, p):
            k = (n - 1) * p / 100
            f = int(k)
            c = k - f
            if f == n - 1:
                return float(data[f])
            return float(data[f] * (1 - c) + data[f + 1] * c)
        
        return {
            'p50': percentile(sorted_times, 50),
            'p90': percentile(sorted_times, 90),
            'p95': percentile(sorted_times, 95)
        }