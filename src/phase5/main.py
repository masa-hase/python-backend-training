"""
Phase 5 メインアプリケーション（DDD準拠）

【課題17】FastAPIアプリケーションをDDD構造で構成してください
"""

from fastapi import FastAPI
from .api.controllers.auth_controller import router as auth_router
from .infrastructure.database.database_config import database_config

app = FastAPI(
    title="ログ解析システム Phase 5",
    description="DDD（ドメイン駆動設計）を適用したログ解析システム",
    version="5.0.0"
)


@app.on_event("startup")
async def startup_event():
    """アプリケーション起動時の処理"""
    # TODO: TDDで実装してください
    # - データベーステーブル作成
    # - 初期データ投入
    pass


@app.on_event("shutdown") 
async def shutdown_event():
    """アプリケーション終了時の処理"""
    # TODO: TDDで実装してください
    # - データベース接続クローズ
    pass


# API ルーターの登録
app.include_router(auth_router)

# 旧版のルーター（後方互換性のため）
# from .api.auth import router as auth_legacy_router
# app.include_router(auth_legacy_router)


@app.get("/")
async def root():
    """ルートエンドポイント"""
    return {
        "message": "ログ解析システム Phase 5 (DDD)",
        "version": "5.0.0",
        "architecture": "Domain-Driven Design",
        "features": [
            "ユーザー認証・認可",
            "ログファイル管理",
            "統計・レポート機能",
            "DDD設計パターン"
        ]
    }


@app.get("/health")
async def health_check():
    """ヘルスチェック"""
    # TODO: TDDで実装してください
    # - データベース接続確認
    # - システム状態確認
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)