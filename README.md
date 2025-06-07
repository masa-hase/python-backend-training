# Python バックエンド開発トレーニング

エンジニア初学者向けのバックエンド技術力向上を目的としたトレーニングプロジェクトです。

## 🎯 学習目標

- TDD（テスト駆動開発）の習得
- バックエンド開発の基礎技術の理解
- 実践的な開発フローの体験

## 📋 前提条件

- Python基礎
- Git基本操作

## ⏰ おおよその学習スケジュール

- **期間**: 約3ヶ月
- **頻度**: 火〜金曜日
- **時間**: 1日1時間
- **総学習時間**: 約48時間

## 🏗 プロジェクト構成

```
python-backend-training/
├── .devcontainer/     # 開発環境設定
├── src/
│   ├── phase1/       # Phase 1: CLIアプリ
│   ├── phase2/       # Phase 2: テスト導入
│   ├── phase3/       # Phase 3: TDD実践
│   ├── phase4/       # Phase 4: Web API
│   └── phase5/       # Phase 5: 応用技術
├── tests/
│   ├── phase1/       # 各Phaseのテスト
│   ├── phase2/
│   ├── phase3/
│   ├── phase4/
│   └── phase5/
├── docs/             # 学習ドキュメント
│   ├── pytest-guide.md   # pytest実行ガイド
│   ├── phase-1/
│   ├── phase-2/
│   ├── phase-3/
│   ├── phase-4/
│   └── phase-5/
└── README.md         # このファイル
```

## 📚 学習フェーズ

### Phase 1: CLIアプリケーション開発（12-15時間）
**目標**: Python基礎とバックエンド要素の習得

**学習内容**:
- ファイル入出力（CSV、JSON）
- 例外処理・エラーハンドリング
- ログ出力
- 基本的なデータ構造
- 外部ライブラリの使用

**成果物**: コマンドライン版のツールアプリケーション

### Phase 2: テスト導入（8-10時間）
**目標**: テストの重要性を理解し、既存コードにテストを追加

**学習内容**:
- pytestの基本的な使い方
- 単体テストの書き方
- テストケースの設計
- 既存コードへのテスト後付け

**成果物**: Phase 1で作成したアプリにテストを追加

### Phase 3: TDD実践（10-12時間）
**目標**: テスト駆動開発の習得

**学習内容**:
- Red-Green-Refactorサイクル
- テストファーストでの開発
- 新機能をTDDで追加
- リファクタリングの実践

**成果物**: TDDで新機能を追加したアプリケーション

### Phase 4: Web API開発（12-15時間）
**目標**: WebアプリケーションとREST APIの基礎

**学習内容**:
- FastAPIの基本
- REST APIの設計
- HTTPメソッド（GET、POST、PUT、DELETE）
- JSONでのデータ交換
- APIテストの書き方

**成果物**: Phase 1のツールをWeb API化

### Phase 5: 応用技術（残り時間）
**目標**: 実践的なバックエンド技術の習得

**学習内容**:
- データベース接続（SQLite → PostgreSQL）
- 認証・認可（JWT）
- CI/CD（GitHub Actions）

**成果物**: 本格的なWebアプリケーション

## 🔄 開発フロー

### ブランチ戦略
1. `main`ブランチ: 学習前の初期状態を維持
2. `develop_[作業者名]`ブランチ: 個人の作業ブランチ
3. 各Phase完了時にPull Requestを作成
4. コードレビュー後、develop_result_作業者名にマージ

## 📖 学習リソース

### 各Phase共通
- 詳細な手順書（`docs/phase-X/README.md`）
- サンプルコード（コメント付き）
- 練習問題と解答例
- トラブルシューティングガイド

### 推奨ツール
- エディタ: VS Code（devcontainer使用）
- Python環境: uv
- テストフレームワーク: pytest（[実行ガイド](docs/pytest-guide.md)）
- Webフレームワーク: FastAPI

## 🚀 始め方

1. リポジトリをクローン
2. 作業ブランチを作成: `git checkout -b develop_[あなたの名前]`
3. devcontainerで開発環境を起動
4. 依存関係をインストール: `uv sync`
5. pytestの動作確認: `uv run pytest --version`
6. `docs/phase-1/README.md` を読んで Phase 1 を開始

### Phase毎の学習方法
- **Phase 1**: `src/phase1/`で CLI アプリ開発
- **Phase 2**: `tests/phase2/`でテスト作成
- **Phase 3**: `src/phase3/`でTDD実践
- **Phase 4**: `src/phase4/`でWeb API開発  
- **Phase 5**: `src/phase5/`で応用技術

## 📞 サポート

- 質問・相談: 随時受付
- 復習・補講: 必要に応じて実施
- コードレビュー: 各Phase完了時

## 📈 進捗確認

各Phaseの完了基準:
- [ ] 機能が正常に動作する
- [ ] 適切なテストが書かれている
- [ ] コードが整理されている
- [ ] ドキュメントが更新されている

---

このトレーニングを通じて、実践的なバックエンド開発スキルとTDDの習慣を身につけましょう！