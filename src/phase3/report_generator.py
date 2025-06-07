"""
レポート生成機能

【課題5】TDDで実装してください
"""

from typing import List, Dict, Any
from src.phase3.log_statistics import LogStatistics
from src.phase3.log_filters import AdvancedLogFilter


class ReportGenerator:
    """ログレポートを生成するクラス"""
    
    def __init__(self, log_data: List[Dict[str, Any]]):
        """
        初期化
        
        Args:
            log_data: レポート対象のログデータ
        """
        self.log_data = log_data
        self.statistics = LogStatistics(log_data)
    
    def generate_daily_summary(self, target_date: str) -> Dict[str, Any]:
        """日次サマリーレポートを生成"""
        # 指定日のログをフィルタ
        daily_logs = [log for log in self.log_data if log.get('date') == target_date]
        
        if not daily_logs:
            return {
                'date': target_date,
                'total_requests': 0,
                'error_count': 0,
                'error_rate': 0.0,
                'average_response_time': 0.0,
                'peak_hour': '',
                'status_code_distribution': {}
            }
        
        # 日次統計を計算
        daily_stats = LogStatistics(daily_logs)
        
        # エラー数をカウント
        error_count = len([log for log in daily_logs 
                         if log.get('level') == 'ERROR' or 
                            log.get('status_code', '').startswith(('4', '5'))])
        
        # ステータスコード分布
        status_distribution = {}
        for log in daily_logs:
            status = log.get('status_code', 'unknown')
            status_distribution[status] = status_distribution.get(status, 0) + 1
        
        return {
            'date': target_date,
            'total_requests': len(daily_logs),
            'error_count': error_count,
            'error_rate': (error_count / len(daily_logs)) * 100 if daily_logs else 0.0,
            'average_response_time': daily_stats.calculate_average_response_time(),
            'peak_hour': daily_stats.calculate_peak_hour(),
            'status_code_distribution': status_distribution
        }
    
    def generate_error_report(self) -> Dict[str, Any]:
        """エラーレポートを生成"""
        # エラーログを抽出
        error_logs = [log for log in self.log_data 
                     if log.get('level') == 'ERROR' or 
                        log.get('status_code', '').startswith(('4', '5'))]
        
        if not error_logs:
            return {
                'total_errors': 0,
                'error_rate': 0.0,
                'most_common_errors': [],
                'error_by_hour': {},
                'error_by_endpoint': {}
            }
        
        # エラーメッセージの集計
        error_messages = {}
        for log in error_logs:
            message = log.get('message', 'Unknown error')
            error_messages[message] = error_messages.get(message, 0) + 1
        
        # 最も多いエラーメッセージトップ3
        most_common = sorted(error_messages.items(), key=lambda x: x[1], reverse=True)[:3]
        
        # 時間帯別エラー数
        error_by_hour = {}
        for log in error_logs:
            if 'time' in log:
                hour = log['time'].split(':')[0]
                error_by_hour[hour] = error_by_hour.get(hour, 0) + 1
        
        # エンドポイント別エラー数
        error_by_endpoint = {}
        for log in error_logs:
            endpoint = log.get('endpoint', 'unknown')
            error_by_endpoint[endpoint] = error_by_endpoint.get(endpoint, 0) + 1
        
        return {
            'total_errors': len(error_logs),
            'error_rate': (len(error_logs) / len(self.log_data)) * 100 if self.log_data else 0.0,
            'most_common_errors': [{'message': msg, 'count': count} for msg, count in most_common],
            'error_by_hour': error_by_hour,
            'error_by_endpoint': error_by_endpoint
        }
    
    def generate_performance_report(self) -> Dict[str, Any]:
        """パフォーマンスレポートを生成"""
        # レスポンス時間の統計を計算
        avg_response_time = self.statistics.calculate_average_response_time()
        percentiles = self.statistics.calculate_response_time_percentiles()
        
        # エンドポイント別パフォーマンス
        endpoint_performance = {}
        for log in self.log_data:
            endpoint = log.get('endpoint', 'unknown')
            if endpoint not in endpoint_performance:
                endpoint_performance[endpoint] = []
            
            if 'response_time' in log and log['response_time'].endswith('ms'):
                try:
                    time_value = int(log['response_time'][:-2])
                    endpoint_performance[endpoint].append(time_value)
                except ValueError:
                    continue
        
        # エンドポイント別平均を計算
        endpoint_avg = {}
        for endpoint, times in endpoint_performance.items():
            if times:
                endpoint_avg[endpoint] = sum(times) / len(times)
        
        # 最も遅いエンドポイントトップ5
        slowest_endpoints = sorted(endpoint_avg.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            'average_response_time': avg_response_time,
            'percentiles': percentiles,
            'slowest_endpoints': [{'endpoint': ep, 'avg_time': time} for ep, time in slowest_endpoints],
            'total_requests_analyzed': len([log for log in self.log_data if 'response_time' in log])
        }