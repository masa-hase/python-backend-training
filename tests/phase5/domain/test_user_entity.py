"""
ユーザーエンティティのテスト

【課題18】ドメインエンティティをTDDで実装・テストしてください
"""

import pytest
from datetime import datetime
from src.phase5.domain.entities.user import User
from src.phase5.domain.value_objects.email import Email
from src.phase5.domain.value_objects.password import Password
from src.phase5.domain.value_objects.user_name import UserName


class TestUserEntity:
    """ユーザーエンティティのテスト"""
    
    def test_create_user_with_valid_data(self):
        """有効なデータでユーザーを作成"""
        # TODO: TDDで実装してください
        # - 有効なEmail、Password、UserNameでUserエンティティ作成
        # - 作成されたエンティティの検証
        pass
    
    def test_user_authenticate_with_correct_password(self):
        """正しいパスワードで認証成功"""
        # TODO: TDDで実装してください
        pass
    
    def test_user_authenticate_with_wrong_password(self):
        """間違ったパスワードで認証失敗"""
        # TODO: TDDで実装してください
        pass
    
    def test_inactive_user_cannot_authenticate(self):
        """非アクティブユーザーは認証不可"""
        # TODO: TDDで実装してください
        pass
    
    def test_change_password_with_valid_current_password(self):
        """有効な現在のパスワードでパスワード変更成功"""
        # TODO: TDDで実装してください
        pass
    
    def test_change_password_with_invalid_current_password(self):
        """無効な現在のパスワードでパスワード変更失敗"""
        # TODO: TDDで実装してください
        pass
    
    def test_update_email(self):
        """メールアドレス更新"""
        # TODO: TDDで実装してください
        pass
    
    def test_deactivate_user(self):
        """ユーザー無効化"""
        # TODO: TDDで実装してください
        pass
    
    def test_record_login(self):
        """ログイン記録"""
        # TODO: TDDで実装してください
        pass
    
    def test_get_user_info_excludes_password(self):
        """ユーザー情報取得でパスワードが除外される"""
        # TODO: TDDで実装してください
        pass