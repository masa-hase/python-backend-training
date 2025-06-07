"""
ファイルアップロードAPIのテスト

【課題3】ファイルアップロードをTDDで実装してください
"""

import pytest
from fastapi.testclient import TestClient
from src.phase4.main import app
import tempfile
import io

client = TestClient(app)


class TestFileUploadAPI:
    """ファイルアップロードAPIのテスト"""
    
    def test_upload_log_file_success(self):
        """ログファイルアップロード成功のテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_upload_invalid_file(self):
        """不正なファイルアップロードのテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_get_uploaded_files(self):
        """アップロードファイル一覧取得のテスト"""
        # TODO: TDDで実装してください
        pass