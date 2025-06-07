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
        # TODO: TDDで実装してください
        pass
    
    def calculate_peak_hour(self) -> str:
        """最もアクセスが多い時間帯を特定"""
        # TODO: TDDで実装してください
        pass
    
    def calculate_error_rate_by_hour(self) -> Dict[str, float]:
        """時間帯別のエラー率を計算"""
        # TODO: TDDで実装してください
        pass
    
    def extract_response_times(self) -> List[int]:
        """レスポンス時間を抽出してリストで返す"""
        # TODO: TDDで実装してください
        pass
    
    def calculate_average_response_time(self) -> float:
        """平均レスポンス時間を計算"""
        # TODO: TDDで実装してください
        pass
    
    def calculate_response_time_percentiles(self) -> Dict[str, float]:
        """レスポンス時間のパーセンタイル（50%, 90%, 95%）を計算"""
        # TODO: TDDで実装してください
        pass