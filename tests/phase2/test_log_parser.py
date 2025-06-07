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
        # TODO: 実装してください
        # ヒント: "2024-01-15 09:23:45 INFO GET /api/users 200 45ms" のようなログを解析
        pass
    
    def test_parse_access_log_with_message(self):
        """メッセージ付きアクセスログの解析テスト"""
        # TODO: 実装してください
        # ヒント: "2024-01-15 09:24:33 ERROR GET /api/data 500 234ms Database connection failed"
        pass
    
    def test_parse_access_log_invalid_format(self):
        """不正な形式のログの解析テスト"""
        # TODO: 実装してください
        # ヒント: 要素数が足りない行、空行などをテスト
        pass
    
    def test_parse_access_log_empty_line(self):
        """空行の解析テスト"""
        # TODO: 実装してください
        pass
    
    def test_parse_error_log_success(self):
        """正常なエラーログの解析テスト"""
        # TODO: 実装してください
        # ヒント: "2024-01-15 09:23:45 [ERROR] UserService: Failed to validate user credentials"
        pass
    
    def test_parse_error_log_invalid_format(self):
        """不正な形式のエラーログの解析テスト"""
        # TODO: 実装してください
        pass