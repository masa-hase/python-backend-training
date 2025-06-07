"""
LogAnalyzerクラスのテスト

Phase 1で作成したLogAnalyzerクラスをテストします。

【課題2】
LogAnalyzerクラスの各メソッドのテストを実装してください。
"""

import pytest
import tempfile
import os
from src.phase1.log_analyzer import LogAnalyzer


class TestLogAnalyzer:
    """LogAnalyzerクラスのテストクラス"""
    
    @pytest.fixture
    def analyzer(self):
        """テスト用のLogAnalyzerインスタンスを作成"""
        return LogAnalyzer()
    
    @pytest.fixture
    def sample_log_file(self):
        """テスト用の一時ログファイルを作成"""
        sample_content = """2024-01-15 09:23:45 INFO GET /api/users 200 45ms
2024-01-15 09:24:33 ERROR GET /api/data 500 234ms Database connection failed
2024-01-15 09:25:15 WARNING GET /api/reports 404 12ms Resource not found
2024-01-15 09:25:45 [ERROR] UserService: Failed to authenticate user
2024-01-15 09:26:03 INFO POST /api/logout 200 89ms"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.log', delete=False, encoding='utf-8') as f:
            f.write(sample_content)
            temp_file_path = f.name
        
        yield temp_file_path
        
        # クリーンアップ
        if os.path.exists(temp_file_path):
            os.unlink(temp_file_path)
    
    def test_read_log_file_success(self, analyzer, sample_log_file):
        """ログファイル読み込み成功のテスト"""
        result = analyzer.read_log_file(sample_log_file)
        
        assert result is True
        assert len(analyzer.log_data) == 5
        
        # 最初のログをチェック
        first_log = analyzer.log_data[0]
        assert first_log['level'] == 'INFO'
        assert first_log['method'] == 'GET'
        assert first_log['endpoint'] == '/api/users'
        assert first_log['line_number'] == 1
    
    def test_read_log_file_not_found(self, analyzer):
        """存在しないファイルの読み込みテスト"""
        result = analyzer.read_log_file("/nonexistent/file.log")
        
        assert result is False
        assert len(analyzer.log_data) == 0
    
    def test_filter_by_level(self, analyzer):
        """ログレベルフィルタのテスト"""
        # テストデータを直接設定
        analyzer.log_data = [
            {'level': 'INFO', 'message': 'test info'},
            {'level': 'ERROR', 'message': 'test error'},
            {'level': 'WARNING', 'message': 'test warning'},
            {'level': 'ERROR', 'message': 'another error'},
            {'level': 'INFO', 'message': 'another info'}
        ]
        
        # ERRORレベルでフィルタ
        error_logs = analyzer.filter_by_level('ERROR')
        assert len(error_logs) == 2
        assert all(log['level'] == 'ERROR' for log in error_logs)
        
        # INFOレベルでフィルタ
        info_logs = analyzer.filter_by_level('INFO')
        assert len(info_logs) == 2
        
        # 存在しないレベル
        debug_logs = analyzer.filter_by_level('DEBUG')
        assert len(debug_logs) == 0
        
        # 小文字でのフィルタ
        error_logs_lower = analyzer.filter_by_level('error')
        assert len(error_logs_lower) == 2
    
    def test_search_keyword(self, analyzer):
        """キーワード検索のテスト"""
        analyzer.log_data = [
            {'full_line': '2024-01-15 09:23:45 INFO GET /api/users 200 45ms', 'message': '', 'endpoint': '/api/users'},
            {'full_line': '2024-01-15 09:24:33 ERROR GET /api/data 500 234ms Database connection failed', 'message': 'Database connection failed', 'endpoint': '/api/data'},
            {'full_line': '2024-01-15 09:25:15 WARNING GET /api/reports 404 12ms Resource not found', 'message': 'Resource not found', 'endpoint': '/api/reports'},
            {'full_line': '2024-01-15 09:26:03 [ERROR] UserService: User authentication failed', 'message': 'User authentication failed', 'endpoint': ''}
        ]
        
        # メッセージで検索
        database_logs = analyzer.search_keyword('Database')
        assert len(database_logs) == 1
        assert 'Database' in database_logs[0]['message']
        
        # エンドポイントで検索
        users_logs = analyzer.search_keyword('/api/users')
        assert len(users_logs) == 1
        
        # 大文字・小文字を区別しない検索
        user_logs = analyzer.search_keyword('user')
        assert len(user_logs) == 2  # users と User がマッチ
        
        # 見つからないキーワード
        not_found = analyzer.search_keyword('nonexistent')
        assert len(not_found) == 0
    
    def test_count_by_level(self, analyzer):
        """レベル別集計のテスト"""
        analyzer.log_data = [
            {'level': 'INFO'},
            {'level': 'ERROR'},
            {'level': 'WARNING'},
            {'level': 'ERROR'},
            {'level': 'INFO'},
            {'level': 'INFO'}
        ]
        
        counts = analyzer.count_by_level()
        
        assert counts['INFO'] == 3
        assert counts['ERROR'] == 2
        assert counts['WARNING'] == 1
        
        # 存在しないレベルは集計されない
        assert 'DEBUG' not in counts
    
    def test_export_to_csv(self, analyzer):
        """CSV出力のテスト"""
        import csv
        
        test_data = [
            {'date': '2024-01-15', 'time': '09:23:45', 'level': 'INFO', 'message': 'test'},
            {'date': '2024-01-15', 'time': '09:24:33', 'level': 'ERROR', 'message': 'error'}
        ]
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            temp_csv_path = f.name
        
        try:
            # CSV出力テスト
            result = analyzer.export_to_csv(test_data, temp_csv_path)
            assert result is True
            
            # ファイルの内容を確認
            with open(temp_csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                
            assert len(rows) == 2
            assert rows[0]['level'] == 'INFO'
            assert rows[1]['level'] == 'ERROR'
            
            # 空のデータでのテスト
            empty_result = analyzer.export_to_csv([], temp_csv_path)
            assert empty_result is False
            
        finally:
            # クリーンアップ
            if os.path.exists(temp_csv_path):
                os.unlink(temp_csv_path)