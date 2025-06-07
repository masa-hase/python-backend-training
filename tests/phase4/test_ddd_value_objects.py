"""
DDD バリューオブジェクトのテスト

【課題2-3】バリューオブジェクトをTDDで実装してください
"""

import pytest
from src.phase4.domain.value_objects.file_name import FileName
from src.phase4.domain.value_objects.file_size import FileSize


class TestFileName:
    """FileName バリューオブジェクトのテスト"""
    
    def test_create_valid_file_name(self):
        """有効なファイル名の作成テスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_file_name_validation(self):
        """ファイル名バリデーションのテスト"""
        # TODO: TDDで実装してください
        # - 最大長チェック
        # - 禁止文字チェック
        # - 拡張子チェック
        pass
    
    def test_get_extension(self):
        """拡張子取得のテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_get_base_name(self):
        """ベース名取得のテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_is_log_file(self):
        """ログファイル判定のテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_create_safe_name(self):
        """安全なファイル名生成のテスト"""
        # TODO: TDDで実装してください
        pass


class TestFileSize:
    """FileSize バリューオブジェクトのテスト"""
    
    def test_create_valid_file_size(self):
        """有効なファイルサイズの作成テスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_file_size_validation(self):
        """ファイルサイズバリデーションのテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_to_mb(self):
        """MB変換のテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_to_human_readable(self):
        """人間が読みやすい形式のテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_is_within_limit(self):
        """サイズ制限チェックのテスト"""
        # TODO: TDDで実装してください
        pass