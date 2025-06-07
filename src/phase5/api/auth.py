"""
認証API（旧版）

【注意】このファイルは古いアーキテクチャです。
新しいDDD準拠の実装は api/controllers/auth_controller.py を使用してください。

Phase 4から継続した学習者のために残しています。
"""

# このファイルは非推奨です。
# DDD準拠の新しい実装は以下を使用してください：
# - api/controllers/auth_controller.py
# - application/use_cases/
# - domain/entities/ および domain/value_objects/
# - infrastructure/repositories/

from fastapi import APIRouter

router = APIRouter(prefix="/auth-legacy", tags=["認証（旧版）"], deprecated=True)

# 旧実装（参考用）
# 実際の開発では api/controllers/auth_controller.py を使用