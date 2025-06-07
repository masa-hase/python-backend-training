"""
データベース操作のテスト（旧版）

【注意】このファイルは古いアーキテクチャのテストです。
新しいDDD準拠のテストは以下を使用してください：
- infrastructure/test_repositories.py（リポジトリテスト）
- infrastructure/test_database_models.py（モデルテスト）

Phase 4から継続した学習者のために残しています。
"""

# このファイルは非推奨です。
# DDD準拠の新しいテストは以下を使用してください：
# - tests/phase5/infrastructure/test_repositories.py
# - データベースモデルは infrastructure/ でテスト
# - ドメインエンティティは domain/ でテスト

import pytest


class TestDatabaseOperationsLegacy:
    """データベース操作のテスト（旧版・参考用）"""
    
    def test_legacy_note(self):
        """旧版テストの注意書き"""
        # 新しいDDD準拠のテスト構造を使用してください
        pass