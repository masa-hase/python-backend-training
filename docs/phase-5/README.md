# Phase 5: 応用技術

## 🎯 Phase 5 の目標

本格的なWebアプリケーションとして必要な応用技術を実装します。
データベース接続、認証機能、CI/CDパイプラインなどを学習し、プロダクションレディなアプリケーションを完成させます。

## ⏰ 推定学習時間

- **総時間**: 残り時間（約8-12時間）
- **データベース連携**: 3-4時間
- **認証機能**: 3-4時間
- **CI/CD**: 2-3時間
- **デプロイ**: 2-3時間

## 📚 学習内容

### 1. データベース連携
- SQLiteからPostgreSQLへの移行
- SQLAlchemyを使ったORM
- データベースマイグレーション
- 非同期データベース操作

### 2. 認証・認可
- JWT（JSON Web Token）認証
- ユーザー登録・ログイン
- API認証の実装
- ロールベースアクセス制御

### 3. CI/CD パイプライン
- GitHub Actionsの設定
- 自動テスト実行
- コード品質チェック
- 自動デプロイ

### 4. 本番環境対応
- 環境変数管理
- ログ設定
- エラー監視
- パフォーマンス最適化

## 🎯 最終的なアプリケーション構成

```
python-backend-training/
├── src/phase5/
│   ├── api/                 # API エンドポイント
│   ├── auth/               # 認証機能
│   ├── database/           # データベース関連
│   ├── models/             # データモデル
│   ├── services/           # ビジネスロジック
│   └── main.py             # アプリケーション起動
├── migrations/             # データベースマイグレーション
├── .github/workflows/      # CI/CD設定
└── docker-compose.yml      # 開発環境
```

## 📋 学習手順

### Step 1: データベース連携（3-4時間）

#### 1.1 データベース設計

**models/database.py**
```python
"""
データベース設定とモデル定義

【課題1】SQLAlchemyでデータベース設定を実装してください
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from datetime import datetime

DATABASE_URL = "sqlite+aiosqlite:///./app.db"  # 開発用SQLite
# DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"  # 本番用

Base = declarative_base()


class User(Base):
    """ユーザーモデル"""
    # TODO: 実装してください
    pass


class LogFile(Base):
    """ログファイルモデル"""
    # TODO: 実装してください
    pass


class LogEntry(Base):
    """ログエントリモデル"""
    # TODO: 実装してください
    pass


# データベースエンジンとセッション
engine = create_async_engine(DATABASE_URL)
SessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_database():
    """データベースセッションを取得"""
    # TODO: 実装してください
    pass
```

#### 1.2 データベース操作のTDD

**tests/phase5/test_database.py**
```python
"""
データベース操作のテスト

【課題2】データベース操作をTDDで実装してください
"""

import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from src.phase5.models.database import User, LogFile, LogEntry


class TestDatabaseOperations:
    """データベース操作のテスト"""
    
    @pytest.fixture
    async def db_session(self):
        """テスト用データベースセッション"""
        # TODO: 実装してください
        pass
    
    async def test_create_user(self, db_session):
        """ユーザー作成のテスト"""
        # TODO: TDDで実装してください
        pass
    
    async def test_create_log_file(self, db_session):
        """ログファイル作成のテスト"""
        # TODO: TDDで実装してください
        pass
    
    async def test_query_log_entries(self, db_session):
        """ログエントリ検索のテスト"""
        # TODO: TDDで実装してください
        pass
```

### Step 2: 認証機能（3-4時間）

#### 2.1 JWT認証の実装

**auth/jwt_auth.py**
```python
"""
JWT認証機能

【課題3】JWT認証をTDDで実装してください
"""

from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = "your-secret-key-here"  # 本番では環境変数から取得
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()


class AuthService:
    """認証サービス"""
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """パスワード検証"""
        # TODO: TDDで実装してください
        pass
    
    @staticmethod
    def get_password_hash(password: str) -> str:
        """パスワードハッシュ化"""
        # TODO: TDDで実装してください
        pass
    
    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
        """アクセストークン生成"""
        # TODO: TDDで実装してください
        pass
    
    @staticmethod
    def verify_token(token: str) -> dict:
        """トークン検証"""
        # TODO: TDDで実装してください
        pass
```

#### 2.2 認証APIエンドポイント

**api/auth.py**
```python
"""
認証API

【課題4】認証エンドポイントをTDDで実装してください
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from ..auth.jwt_auth import AuthService
from ..models.database import get_database
from ..models.schemas import UserCreate, UserResponse, Token

router = APIRouter(prefix="/auth", tags=["認証"])


@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate, db: AsyncSession = Depends(get_database)):
    """ユーザー登録"""
    # TODO: TDDで実装してください
    pass


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_database)):
    """ログイン"""
    # TODO: TDDで実装してください
    pass


@router.get("/me", response_model=UserResponse)
async def get_current_user(current_user = Depends(AuthService.get_current_user)):
    """現在のユーザー情報取得"""
    # TODO: TDDで実装してください
    pass
```

#### 2.3 認証テスト

**tests/phase5/test_auth.py**
```python
"""
認証機能のテスト

【課題5】認証機能をTDDで実装してください
"""

import pytest
from fastapi.testclient import TestClient
from src.phase5.main import app

client = TestClient(app)


class TestAuthentication:
    """認証機能のテスト"""
    
    def test_user_registration(self):
        """ユーザー登録のテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_user_login(self):
        """ユーザーログインのテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_protected_endpoint_access(self):
        """認証が必要なエンドポイントのテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_invalid_token_access(self):
        """無効なトークンでのアクセステスト"""
        # TODO: TDDで実装してください
        pass
```

### Step 3: CI/CD パイプライン（2-3時間）

#### 3.1 GitHub Actions設定

**.github/workflows/ci.yml**
```yaml
# CI/CDパイプライン設定
# 【課題6】GitHub Actionsを設定してください

name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop_* ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:13
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test_db
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install uv
      # TODO: uv のインストール設定
      
    - name: Install dependencies
      # TODO: 依存関係のインストール
      
    - name: Run tests
      # TODO: テスト実行の設定
      
    - name: Code quality checks
      # TODO: コード品質チェック（black, isort, mypy）
      
    - name: Upload coverage
      # TODO: カバレッジレポートのアップロード
```

#### 3.2 コード品質設定

**pyproject.toml** (追加設定)
```toml
# 【課題7】コード品質ツールの設定を追加してください

[tool.black]
line-length = 100
target-version = ['py311']

[tool.isort]
profile = "black"
line_length = 100

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
python_classes = "Test*"
python_functions = "test_*"
addopts = "-v --tb=short --cov=src --cov-report=html --cov-report=xml"
```

### Step 4: 本番環境対応（2-3時間）

#### 4.1 環境設定

**config/settings.py**
```python
"""
アプリケーション設定

【課題8】環境変数を使った設定管理を実装してください
"""

from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """アプリケーション設定"""
    
    # データベース設定
    database_url: str = "sqlite+aiosqlite:///./app.db"
    
    # JWT設定
    secret_key: str = "your-secret-key-here"
    access_token_expire_minutes: int = 30
    
    # ログ設定
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # TODO: その他の設定を追加
    
    class Config:
        env_file = ".env"


settings = Settings()
```

#### 4.2 Docker設定

**Dockerfile**
```dockerfile
# 【課題9】Dockerfileを作成してください

FROM python:3.11-slim

WORKDIR /app

# TODO: Dockerの設定を実装してください
```

**docker-compose.yml**
```yaml
# 【課題10】docker-composeを設定してください

version: '3.8'

services:
  app:
    # TODO: アプリケーションサービス設定
    
  postgres:
    # TODO: PostgreSQLサービス設定
    
  redis:
    # TODO: Redisサービス設定（キャッシュ用）
```

## 📝 完成チェックリスト

Phase 5 完了時に以下が実装されていることを確認してください：

### データベース機能
- [ ] SQLAlchemyを使ったORM実装
- [ ] データベースマイグレーション
- [ ] 非同期データベース操作
- [ ] データベーステストの実装

### 認証機能
- [ ] JWT認証の実装
- [ ] ユーザー登録・ログイン機能
- [ ] パスワードハッシュ化
- [ ] 認証が必要なエンドポイントの保護

### CI/CD
- [ ] GitHub Actionsパイプライン
- [ ] 自動テスト実行
- [ ] コード品質チェック
- [ ] カバレッジレポート

### 本番環境対応
- [ ] 環境変数による設定管理
- [ ] Dockerコンテナ化
- [ ] docker-compose設定
- [ ] ログ設定
- [ ] エラーハンドリング

### 統合テスト
- [ ] API全体の統合テスト
- [ ] 認証フローのテスト
- [ ] データベース操作のテスト
- [ ] エラーケースのテスト

## 🎉 Phase 5 完了後 - プロジェクト総まとめ

### 習得したスキル
- **Phase 1**: Python基礎、ファイル操作、CLI開発
- **Phase 2**: テスト作成、pytest使用方法
- **Phase 3**: TDD実践、テストファーストの開発
- **Phase 4**: Web API開発、FastAPI、REST API設計
- **Phase 5**: データベース、認証、CI/CD、本番環境対応

### 完成したアプリケーション
- フル機能のログ解析Web API
- データベース連携
- ユーザー認証機能
- 自動テスト・デプロイ環境
- 本番環境レディ

### 次のステップ
1. **実際のプロダクト開発**: 学習した技術を実際のプロジェクトで活用
2. **さらなる技術学習**: 
   - マイクロサービス
   - Kubernetes
   - 監視・ログ集約
   - パフォーマンス最適化
3. **チーム開発**: Git Flow、コードレビュー、ペアプログラミング

## 💡 本番運用のベストプラクティス

### 1. セキュリティ
- HTTPS必須
- CORS設定
- SQL Injection対策
- 機密情報の環境変数管理

### 2. パフォーマンス
- データベースインデックス
- キャッシュ戦略
- 非同期処理
- レスポンス最適化

### 3. 監視・運用
- ヘルスチェック
- メトリクス収集
- ログ集約
- アラート設定

### 4. スケーラビリティ
- 水平スケーリング対応
- ロードバランサー
- データベース分散
- CDN活用

おめでとうございます！これで本格的なバックエンド開発者としてのスキルが身についています！