"""
高度なログフィルタリング機能

【課題4】TDDで実装してください
"""

from typing import List, Dict, Any, Optional
from datetime import date, datetime


class AdvancedLogFilter:
    """高度なログフィルタリングを行うクラス"""
    
    def __init__(self, log_data: List[Dict[str, Any]]):
        """
        初期化
        
        Args:
            log_data: フィルタ対象のログデータ
        """
        self.log_data = log_data
    
    def filter_by_date_range(self, start_date: date, end_date: date) -> List[Dict[str, Any]]:
        """日付範囲でフィルタリング"""
        filtered_logs = []
        
        for log in self.log_data:
            if 'date' in log:
                try:
                    # "2024-01-15" 形式をdateオブジェクトに変換
                    log_date = datetime.strptime(log['date'], '%Y-%m-%d').date()
                    
                    if start_date <= log_date <= end_date:
                        filtered_logs.append(log)
                except ValueError:
                    # 日付形式が不正な場合はスキップ
                    continue
                    
        return filtered_logs
    
    def filter_by_response_time_range(self, min_time: int, max_time: int) -> List[Dict[str, Any]]:
        """レスポンス時間範囲でフィルタリング"""
        filtered_logs = []
        
        for log in self.log_data:
            if 'response_time' in log:
                time_str = log['response_time']
                
                if time_str.endswith('ms'):
                    try:
                        time_value = int(time_str[:-2])  # "ms"を除去
                        
                        if min_time <= time_value <= max_time:
                            filtered_logs.append(log)
                    except ValueError:
                        continue  # 解析できない場合はスキップ
                        
        return filtered_logs
    
    def filter_by_multiple_conditions(self, **conditions) -> List[Dict[str, Any]]:
        """複数条件でフィルタリング"""
        filtered_logs = self.log_data
        
        # レベルでフィルタ
        if 'level' in conditions:
            filtered_logs = [log for log in filtered_logs 
                           if log.get('level') == conditions['level']]
        
        # メソッドでフィルタ
        if 'method' in conditions:
            filtered_logs = [log for log in filtered_logs 
                           if log.get('method') == conditions['method']]
        
        # ステータスコードでフィルタ
        if 'status_code' in conditions:
            filtered_logs = [log for log in filtered_logs 
                           if log.get('status_code') == conditions['status_code']]
        
        # エンドポイントでフィルタ（部分マッチ）
        if 'endpoint' in conditions:
            filtered_logs = [log for log in filtered_logs 
                           if conditions['endpoint'] in log.get('endpoint', '')]
        
        # 最小レスポンス時間
        if 'min_response_time' in conditions:
            min_time = conditions['min_response_time']
            filtered_logs = [log for log in filtered_logs 
                           if self._extract_response_time(log) >= min_time]
        
        # 最大レスポンス時間
        if 'max_response_time' in conditions:
            max_time = conditions['max_response_time']
            filtered_logs = [log for log in filtered_logs 
                           if self._extract_response_time(log) <= max_time]
        
        return filtered_logs
    
    def _extract_response_time(self, log: Dict[str, Any]) -> int:
        """ログからレスポンス時間を抽出"""
        if 'response_time' not in log:
            return 0
            
        time_str = log['response_time']
        if time_str.endswith('ms'):
            try:
                return int(time_str[:-2])
            except ValueError:
                return 0
        return 0