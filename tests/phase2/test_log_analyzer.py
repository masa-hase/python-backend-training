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
        # TODO: 実装してください
        # ヒント: tempfile.NamedTemporaryFile を使用
        pass
    
    def test_read_log_file_success(self, analyzer, sample_log_file):
        """ログファイル読み込み成功のテスト"""
        # TODO: 実装してください
        pass
    
    def test_read_log_file_not_found(self, analyzer):
        """存在しないファイルの読み込みテスト"""
        # TODO: 実装してください
        pass
    
    def test_filter_by_level(self, analyzer):
        """ログレベルフィルタのテスト"""
        # TODO: 実装してください
        # ヒント: analyzer.log_data に直接テストデータを設定
        pass
    
    def test_search_keyword(self, analyzer):
        """キーワード検索のテスト"""
        # TODO: 実装してください
        pass
    
    def test_count_by_level(self, analyzer):
        """レベル別集計のテスト"""
        # TODO: 実装してください
        pass
    
    def test_export_to_csv(self, analyzer):
        """CSV出力のテスト"""
        # TODO: 実装してください
        # ヒント: tempfile で一時ファイルを作成し、内容を確認
        pass