"""
ログ解析機能のテスト

Phase 1で作成したログ解析関数をテストします。

【課題1】
以下のテストクラスを実装してください。
"""

import pytest
from src.phase1.practice_string_parse import parse_log_line, parse_error_log_line


class TestLogParser:
    """ログ解析のテストクラス"""
    
    def test_parse_access_log_success(self):
        """正常なアクセスログの解析テスト"""
        log_line = "2024-01-15 09:23:45 INFO GET /api/users 200 45ms"
        result = parse_log_line(log_line)
        
        assert result is not None
        assert result["date"] == "2024-01-15"
        assert result["time"] == "09:23:45"
        assert result["datetime"] == "2024-01-15 09:23:45"
        assert result["level"] == "INFO"
        assert result["method"] == "GET"
        assert result["endpoint"] == "/api/users"
        assert result["status_code"] == "200"
        assert result["response_time"] == "45ms"
        assert result["message"] == ""
        assert result["full_line"] == log_line
    
    def test_parse_access_log_with_message(self):
        """メッセージ付きアクセスログの解析テスト"""
        log_line = "2024-01-15 09:24:33 ERROR GET /api/data 500 234ms Database connection failed"
        result = parse_log_line(log_line)
        
        assert result is not None
        assert result["date"] == "2024-01-15"
        assert result["time"] == "09:24:33"
        assert result["level"] == "ERROR"
        assert result["method"] == "GET"
        assert result["endpoint"] == "/api/data"
        assert result["status_code"] == "500"
        assert result["response_time"] == "234ms"
        assert result["message"] == "Database connection failed"
    
    def test_parse_access_log_invalid_format(self):
        """不正な形式のログの解析テスト"""
        # 要素数が不足
        invalid_line = "2024-01-15 09:23:45 INFO GET"
        result = parse_log_line(invalid_line)
        assert result is None
        
        # 完全に無効なフォーマット
        invalid_line2 = "invalid log format"
        result2 = parse_log_line(invalid_line2)
        assert result2 is None
    
    def test_parse_access_log_empty_line(self):
        """空行の解析テスト"""
        # 空行
        result = parse_log_line("")
        assert result is None
        
        # スペースのみ
        result2 = parse_log_line("   ")
        assert result2 is None
        
        # 改行のみ
        result3 = parse_log_line("\n")
        assert result3 is None
    
    def test_parse_error_log_success(self):
        """正常なエラーログの解析テスト"""
        log_line = "2024-01-15 09:23:45 [ERROR] UserService: Failed to validate user credentials"
        result = parse_error_log_line(log_line)
        
        assert result is not None
        assert result["date"] == "2024-01-15"
        assert result["time"] == "09:23:45"
        assert result["datetime"] == "2024-01-15 09:23:45"
        assert result["level"] == "ERROR"
        assert result["service"] == "UserService"
        assert result["message"] == "Failed to validate user credentials"
        assert result["full_line"] == log_line
    
    def test_parse_error_log_invalid_format(self):
        """不正な形式のエラーログの解析テスト"""
        # [ERROR]が含まれないログ
        invalid_line = "2024-01-15 09:23:45 INFO Some message"
        result = parse_error_log_line(invalid_line)
        assert result is None
        
        # 日時が不正
        invalid_line2 = "invalid-date [ERROR] Service: Message"
        result2 = parse_error_log_line(invalid_line2)
        assert result2 is None
        
        # 空行
        result3 = parse_error_log_line("")
        assert result3 is None
        
        # サービス名なし（コロンなし）
        log_without_service = "2024-01-15 09:23:45 [ERROR] Some error message"
        result4 = parse_error_log_line(log_without_service)
        assert result4 is not None
        assert result4["service"] == "Unknown"
        assert result4["message"] == "Some error message"