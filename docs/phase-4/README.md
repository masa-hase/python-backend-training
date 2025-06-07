# Phase 4: Web API開発 + DDD実践

## 🎯 Phase 4 の目標

これまでのCLIログ解析ツールをWebアプリケーション化し、REST APIとして提供します。
FastAPIを使用してTDDでWeb API開発を学習し、さらにDDD（ドメイン駆動設計）の基礎を実践します。

## ⏰ 推定学習時間

- **総時間**: 15-18時間
- **FastAPI基礎学習**: 2-3時間
- **DDD基礎理解**: 3-4時間
- **TDD + DDDでAPI実装**: 8-10時間
- **リファクタリング**: 2-3時間

## 📚 学習内容

### 1. Web API基礎
- REST APIの概念
- HTTPメソッド（GET、POST、PUT、DELETE）
- リクエスト・レスポンスの形式
- ステータスコード

### 2. FastAPI基礎
- FastAPIの基本概念
- ルーティング
- パスパラメータ・クエリパラメータ
- リクエストボディ・レスポンスモデル

### 3. DDD基礎
- ドメインモデルの設計
- エンティティとバリューオブジェクト
- ドメインサービス
- リポジトリパターン
- レイヤードアーキテクチャ

### 4. TDD + DDD実践
- ドメインロジックのテスト駆動開発
- ドメインサービスのテスト
- リポジトリのテスト
- APIレイヤーのテスト

## 🏗 DDDアーキテクチャ構成

```
src/phase4/
├── main.py                    # FastAPI アプリケーション起動
├── api/                       # プレゼンテーション層
│   ├── controllers/          # API コントローラー
│   └── schemas/              # API スキーマ（リクエスト・レスポンス）
├── domain/                    # ドメイン層
│   ├── entities/             # エンティティ
│   ├── value_objects/        # バリューオブジェクト
│   ├── services/             # ドメインサービス
│   └── repositories/         # リポジトリインターフェース
├── infrastructure/           # インフラストラクチャ層
│   ├── repositories/         # リポジトリ実装
│   └── external/             # 外部サービス
└── application/              # アプリケーション層
    ├── use_cases/            # ユースケース
    └── dto/                  # データ転送オブジェクト
```

## 🎯 DDDの学習目標

### ドメインモデリング
- **ログファイル管理ドメイン**: ファイルのアップロード、管理、削除
- **ログ解析ドメイン**: ログの解析、統計計算、レポート生成
- **ユーザー管理ドメイン**: ユーザーの認証、権限管理

### DDDパターンの実践
- **エンティティ**: `LogFile`, `User`, `AnalysisReport`
- **バリューオブジェクト**: `FileName`, `LogLevel`, `ResponseTime`
- **ドメインサービス**: `LogAnalysisService`, `StatisticsCalculator`
- **リポジトリ**: `ILogFileRepository`, `IUserRepository`

## 🌐 作成するAPI仕様

### 基本エンドポイント

#### 1. ログファイル操作
```
POST /api/logs/upload
- ログファイルをアップロード
- レスポンス: アップロード結果

GET /api/logs
- アップロードされたログファイル一覧
- レスポンス: ファイル情報のリスト

DELETE /api/logs/{file_id}
- 指定したログファイルを削除
```

#### 2. ログ解析
```
GET /api/analysis/logs/{file_id}
- 基本的なログ解析結果を取得
- クエリパラメータ: level, keyword

GET /api/analysis/logs/{file_id}/summary
- ログのサマリー情報を取得
- レスポンス: 総数、レベル別集計等
```

#### 3. 統計情報
```
GET /api/statistics/logs/{file_id}/hourly
- 時間帯別統計を取得

GET /api/statistics/logs/{file_id}/response-time
- レスポンス時間統計を取得

GET /api/statistics/logs/{file_id}/errors
- エラー統計を取得
```

#### 4. レポート生成
```
GET /api/reports/logs/{file_id}/daily
- 日次レポートを取得
- クエリパラメータ: date

GET /api/reports/logs/{file_id}/performance
- パフォーマンスレポートを取得
```

## 📋 学習手順

### Step 1: DDDとFastAPI基礎学習（3-4時間）

#### 1.1 DDD基礎理解

**ドメイン駆動設計とは？**
- **ドメイン**: 解決すべきビジネス問題の領域
- **ドメインモデル**: ビジネスルールとロジックを表現するオブジェクト
- **レイヤードアーキテクチャ**: 関心事の分離による設計

**DDDの利点**:
- ビジネスロジックとインフラの分離
- テストしやすい設計
- 変更に強いアーキテクチャ
- チーム間の共通言語

#### 1.1 FastAPIのインストールと基本設定

```bash
# pyproject.tomlにFastAPI関連パッケージを追加済み
uv add fastapi uvicorn
```

#### 1.2 最初のAPI作成

**src/web_api/main.py**
```python
"""
FastAPI基礎練習

【練習1】基本的なAPIエンドポイントを作成してください
"""

from fastapi import FastAPI

app = FastAPI(
    title="ログ解析API",
    description="Phase 4で作成するログ解析Web API",
    version="1.0.0"
)


@app.get("/")
async def root():
    """ルートエンドポイント"""
    # TODO: 実装してください
    pass


@app.get("/health")
async def health_check():
    """ヘルスチェックエンドポイント"""
    # TODO: 実装してください
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**練習1**: 上記のAPIを実装し、ブラウザで動作確認してください。

```bash
# APIサーバー起動
python src/web_api/main.py

# 別ターミナルで確認
curl http://localhost:8000/
curl http://localhost:8000/health
```

#### 1.3 パスパラメータとクエリパラメータ

**練習2**: パラメータを使用するエンドポイントを追加

```python
@app.get("/api/logs/{file_id}")
async def get_log_file(file_id: int, level: str = None, keyword: str = None):
    """ログファイル取得（パラメータ練習）"""
    # TODO: 実装してください
    pass
```

### Step 2: データモデルの定義（1-2時間）

#### 2.1 Pydanticモデルの作成

**src/web_api/models.py**
```python
"""
APIのデータモデル定義

【課題1】Pydanticモデルを定義してください
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime


class LogEntry(BaseModel):
    """ログエントリのモデル"""
    # TODO: 実装してください
    pass


class LogFileSummary(BaseModel):
    """ログファイルサマリーのモデル"""
    # TODO: 実装してください
    pass


class HourlyStatistics(BaseModel):
    """時間帯別統計のモデル"""
    # TODO: 実装してください
    pass


class ResponseTimeStatistics(BaseModel):
    """レスポンス時間統計のモデル"""
    # TODO: 実装してください
    pass


class ErrorReport(BaseModel):
    """エラーレポートのモデル"""
    # TODO: 実装してください
    pass
```

### Step 3: TDDでAPI実装（8-10時間）

#### 3.1 APIテストの基本

**tests/test_api_basic.py**
```python
"""
基本的なAPIテスト

【課題2】APIのテストをTDDで実装してください
"""

import pytest
from fastapi.testclient import TestClient
from src.web_api.main import app

client = TestClient(app)


class TestBasicAPI:
    """基本APIのテスト"""
    
    def test_root_endpoint(self):
        """ルートエンドポイントのテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_health_check(self):
        """ヘルスチェックのテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_get_logs_endpoint(self):
        """ログ取得エンドポイントのテスト"""
        # TODO: TDDで実装してください
        pass
```

#### 3.2 ファイルアップロードAPIのTDD

**tests/test_file_upload_api.py**
```python
"""
ファイルアップロードAPIのテスト

【課題3】ファイルアップロードをTDDで実装してください
"""

import pytest
from fastapi.testclient import TestClient
from src.web_api.main import app
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
```

#### 3.3 ログ解析APIのTDD

**tests/test_log_analysis_api.py**
```python
"""
ログ解析APIのテスト

【課題4】ログ解析機能をTDDで実装してください
"""

import pytest
from fastapi.testclient import TestClient
from src.web_api.main import app

client = TestClient(app)


class TestLogAnalysisAPI:
    """ログ解析APIのテスト"""
    
    @pytest.fixture
    def uploaded_file_id(self):
        """テスト用のアップロード済みファイルID"""
        # TODO: テスト用ファイルをアップロードしてIDを返す
        pass
    
    def test_get_log_analysis(self, uploaded_file_id):
        """ログ解析結果取得のテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_get_log_summary(self, uploaded_file_id):
        """ログサマリー取得のテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_filter_logs_by_level(self, uploaded_file_id):
        """ログレベルフィルタのテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_search_logs_by_keyword(self, uploaded_file_id):
        """キーワード検索のテスト"""
        # TODO: TDDで実装してください
        pass
```

#### 3.4 統計APIのTDD

**tests/test_statistics_api.py**
```python
"""
統計APIのテスト

【課題5】統計機能をTDDで実装してください
"""

import pytest
from fastapi.testclient import TestClient
from src.web_api.main import app

client = TestClient(app)


class TestStatisticsAPI:
    """統計APIのテスト"""
    
    def test_get_hourly_statistics(self):
        """時間帯別統計取得のテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_get_response_time_statistics(self):
        """レスポンス時間統計取得のテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_get_error_statistics(self):
        """エラー統計取得のテスト"""
        # TODO: TDDで実装してください
        pass
```

### Step 4: APIの実装（スケルトン）

#### 4.1 メインAPIファイル

**src/web_api/main.py**
```python
"""
メインAPIファイル

【課題2-5】各エンドポイントをTDDで実装してください
"""

from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from fastapi.responses import JSONResponse
from typing import List, Optional
import uvicorn

from .models import (
    LogEntry, LogFileSummary, HourlyStatistics, 
    ResponseTimeStatistics, ErrorReport
)
from .services import LogAnalysisService, FileManager

app = FastAPI(
    title="ログ解析API",
    description="Phase 4で作成するログ解析Web API",
    version="1.0.0"
)

# サービスクラスのインスタンス
log_service = LogAnalysisService()
file_manager = FileManager()


@app.get("/")
async def root():
    """ルートエンドポイント"""
    # TODO: TDDで実装してください
    pass


@app.get("/health")
async def health_check():
    """ヘルスチェックエンドポイント"""
    # TODO: TDDで実装してください
    pass


# ファイル操作エンドポイント
@app.post("/api/logs/upload")
async def upload_log_file(file: UploadFile = File(...)):
    """ログファイルをアップロード"""
    # TODO: TDDで実装してください
    pass


@app.get("/api/logs")
async def get_uploaded_files():
    """アップロードされたファイル一覧を取得"""
    # TODO: TDDで実装してください
    pass


@app.delete("/api/logs/{file_id}")
async def delete_log_file(file_id: int):
    """指定したログファイルを削除"""
    # TODO: TDDで実装してください
    pass


# ログ解析エンドポイント
@app.get("/api/analysis/logs/{file_id}", response_model=List[LogEntry])
async def get_log_analysis(
    file_id: int,
    level: Optional[str] = Query(None),
    keyword: Optional[str] = Query(None)
):
    """ログ解析結果を取得"""
    # TODO: TDDで実装してください
    pass


@app.get("/api/analysis/logs/{file_id}/summary", response_model=LogFileSummary)
async def get_log_summary(file_id: int):
    """ログサマリー情報を取得"""
    # TODO: TDDで実装してください
    pass


# 統計エンドポイント
@app.get("/api/statistics/logs/{file_id}/hourly", response_model=HourlyStatistics)
async def get_hourly_statistics(file_id: int):
    """時間帯別統計を取得"""
    # TODO: TDDで実装してください
    pass


@app.get("/api/statistics/logs/{file_id}/response-time", response_model=ResponseTimeStatistics)
async def get_response_time_statistics(file_id: int):
    """レスポンス時間統計を取得"""
    # TODO: TDDで実装してください
    pass


@app.get("/api/statistics/logs/{file_id}/errors", response_model=ErrorReport)
async def get_error_statistics(file_id: int):
    """エラー統計を取得"""
    # TODO: TDDで実装してください
    pass


# レポートエンドポイント
@app.get("/api/reports/logs/{file_id}/daily")
async def get_daily_report(file_id: int, date: Optional[str] = Query(None)):
    """日次レポートを取得"""
    # TODO: TDDで実装してください
    pass


@app.get("/api/reports/logs/{file_id}/performance")
async def get_performance_report(file_id: int):
    """パフォーマンスレポートを取得"""
    # TODO: TDDで実装してください
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

#### 4.2 サービスクラス

**src/web_api/services.py**
```python
"""
APIのビジネスロジック

【課題6】サービスクラスをTDDで実装してください
"""

from typing import List, Dict, Any, Optional
import os
import json
from ..log_analyzer import LogAnalyzer
from ..log_statistics import LogStatistics
from ..report_generator import ReportGenerator


class FileManager:
    """ファイル管理サービス"""
    
    def __init__(self, upload_dir: str = "uploaded_logs"):
        self.upload_dir = upload_dir
        os.makedirs(upload_dir, exist_ok=True)
    
    def save_uploaded_file(self, file_content: bytes, filename: str) -> int:
        """アップロードファイルを保存"""
        # TODO: TDDで実装してください
        pass
    
    def get_file_list(self) -> List[Dict[str, Any]]:
        """ファイル一覧を取得"""
        # TODO: TDDで実装してください
        pass
    
    def delete_file(self, file_id: int) -> bool:
        """ファイルを削除"""
        # TODO: TDDで実装してください
        pass
    
    def get_file_path(self, file_id: int) -> Optional[str]:
        """ファイルパスを取得"""
        # TODO: TDDで実装してください
        pass


class LogAnalysisService:
    """ログ解析サービス"""
    
    def __init__(self):
        self.file_manager = FileManager()
    
    def analyze_log_file(self, file_id: int, level: str = None, keyword: str = None) -> Dict[str, Any]:
        """ログファイルを解析"""
        # TODO: TDDで実装してください
        pass
    
    def get_log_summary(self, file_id: int) -> Dict[str, Any]:
        """ログサマリーを取得"""
        # TODO: TDDで実装してください
        pass
    
    def get_hourly_statistics(self, file_id: int) -> Dict[str, Any]:
        """時間帯別統計を取得"""
        # TODO: TDDで実装してください
        pass
    
    def get_response_time_statistics(self, file_id: int) -> Dict[str, Any]:
        """レスポンス時間統計を取得"""
        # TODO: TDDで実装してください
        pass
    
    def get_error_statistics(self, file_id: int) -> Dict[str, Any]:
        """エラー統計を取得"""
        # TODO: TDDで実装してください
        pass
```

### Step 5: APIテストの実行と改善（2-3時間）

#### 5.1 APIテストの実行

```bash
# APIテストを実行
python -m pytest tests/test_*api*.py -v

# テストカバレッジ確認
python -m pytest tests/test_*api*.py --cov=src/web_api --cov-report=html

# APIサーバーを起動してブラウザで確認
python src/web_api/main.py
# http://localhost:8000/docs にアクセス（Swagger UI）
```

#### 5.2 Swagger UIでの動作確認

FastAPIは自動的にAPIドキュメントを生成します：
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

#### 5.3 APIの改善

テストを通じて見つかった問題を修正：
- **エラーハンドリング**: 適切なHTTPステータスコード
- **バリデーション**: 入力値の検証
- **レスポンス形式**: 一貫したJSON形式

## 📝 完成チェックリスト

Phase 4 完了時に以下が実装されていることを確認してください：

### 基本API機能
- [ ] ルートエンドポイント（/）
- [ ] ヘルスチェックエンドポイント（/health）
- [ ] Swagger UIでAPIドキュメント確認可能

### ファイル操作API
- [ ] ログファイルアップロード（POST /api/logs/upload）
- [ ] ファイル一覧取得（GET /api/logs）
- [ ] ファイル削除（DELETE /api/logs/{file_id}）

### ログ解析API
- [ ] ログ解析結果取得（GET /api/analysis/logs/{file_id}）
- [ ] ログサマリー取得（GET /api/analysis/logs/{file_id}/summary）
- [ ] レベル・キーワードフィルタ対応

### 統計API
- [ ] 時間帯別統計（GET /api/statistics/logs/{file_id}/hourly）
- [ ] レスポンス時間統計（GET /api/statistics/logs/{file_id}/response-time）
- [ ] エラー統計（GET /api/statistics/logs/{file_id}/errors）

### レポートAPI
- [ ] 日次レポート（GET /api/reports/logs/{file_id}/daily）
- [ ] パフォーマンスレポート（GET /api/reports/logs/{file_id}/performance）

### TDD品質
- [ ] すべてのエンドポイントがテストファーストで実装
- [ ] 正常系・異常系のテストケース
- [ ] APIテストカバレッジ90%以上
- [ ] エラーハンドリングの適切な実装

## 🎉 Phase 4 完了後

### 学習の振り返り
- CLIアプリからWeb APIへの変換で何が変わりましたか？
- TDDでAPI開発することの利点を感じましたか？
- REST APIの設計で難しいと感じた点は？
- FastAPIの使いやすさはいかがでしたか？

### 身についたスキル
- **Web API設計と実装**
- **RESTful APIの概念**
- **FastAPIフレームワーク**
- **APIテストの手法**
- **TDDでのWeb開発**

次のPhase 5では、データベース接続、認証機能、CI/CDなどの応用技術を学習して、本格的なWebアプリケーションを完成させます！

## 💡 API開発のベストプラクティス

### 1. 適切なHTTPステータスコード
- **200**: 成功
- **201**: 作成成功
- **400**: クライアントエラー
- **404**: リソースが見つからない
- **500**: サーバーエラー

### 2. 一貫したエラーレスポンス
```json
{
  "error": {
    "code": "INVALID_FILE_FORMAT",
    "message": "アップロードされたファイルは有効なログファイルではありません",
    "details": {}
  }
}
```

### 3. APIバージョニング
- URLパスでバージョン管理: `/api/v1/logs`
- 将来の変更に対応

### 4. 適切なデータ検証
- Pydanticモデルでリクエスト・レスポンスを型安全に

### 5. セキュリティ考慮
- ファイルアップロードの制限
- 入力値のサニタイゼーション
- レート制限の実装