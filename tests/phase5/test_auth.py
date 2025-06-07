"""
認証機能のテスト（旧版）

【注意】このファイルは古いアーキテクチャのテストです。
新しいDDD準拠のテストは以下を使用してください：
- api/test_auth_controller.py
- domain/test_user_entity.py
- domain/test_value_objects.py
- application/test_use_cases.py
- infrastructure/test_repositories.py

Phase 4から継続した学習者のために残しています。
"""

# このファイルは非推奨です。
# DDD準拠の新しいテストは以下のディレクトリを使用してください：
# - tests/phase5/domain/     # ドメイン層のテスト
# - tests/phase5/application/  # アプリケーション層のテスト
# - tests/phase5/infrastructure/  # インフラ層のテスト
# - tests/phase5/api/        # API層のテスト

import pytest


class TestAuthenticationLegacy:
    """認証機能のテスト（旧版・参考用）"""
    
    def test_legacy_note(self):
        """旧版テストの注意書き"""
        # 新しいDDD準拠のテスト構造を使用してください
        pass