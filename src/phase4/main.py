"""
Phase 4: DDD + TDD Web API

DDDアーキテクチャでログ解析Web APIを構築
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.controllers.log_file_controller import router as log_file_router

app = FastAPI(
    title="ログ解析API - DDD版",
    description="Phase 4で作成するDDD + TDD Web API",
    version="1.0.0"
)

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーター登録
app.include_router(log_file_router)


@app.get("/")
async def root():
    """ルートエンドポイント"""
    return {
        "message": "ログ解析API - DDD版",
        "version": "1.0.0",
        "architecture": "Domain Driven Design",
        "development": "Test Driven Development"
    }


@app.get("/health")
async def health_check():
    """ヘルスチェックエンドポイント"""
    return {"status": "healthy", "architecture": "DDD", "testing": "TDD"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)