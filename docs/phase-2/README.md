# Phase 2: テスト導入

## 🎯 Phase 2 の目標

Phase 1で作成したログ解析ツールにテストを後付けで追加します。
テストの重要性を体感し、pytestの基本的な使い方を学習します。

## ⏰ 推定学習時間

- **総時間**: 8-10時間
- **pytest基礎学習**: 2-3時間
- **既存コードへのテスト追加**: 6-7時間

## 📚 学習内容

### 1. テストの基礎理解
- テストを書く理由とメリット
- 単体テストの考え方
- pytestの基本概念

### 2. pytest基礎
- テスト関数の書き方
- アサーション（assert文）
- テストの実行方法
- テストレポートの読み方

### 3. 実践的なテスト作成
- 既存コードのテスト設計
- テストケースの考え方
- エッジケースの対応
- モック・フィクスチャの基本

## 🔍 なぜテストが重要なのか？

Phase 1では「とりあえず動くもの」を作りましたが、以下のような問題があります：

- **バグの発見が困難**: 修正後に既存機能が壊れても気づかない
- **リファクタリングが怖い**: コード改善時に何が壊れるかわからない
- **仕様の不明確さ**: 期待する動作が曖昧
- **品質の担保なし**: 正しく動いているかの客観的確認がない

テストを書くことで、これらの問題を解決できます。

## 📋 学習手順

### Step 1: pytest基礎学習（2-3時間）

#### 1.1 pytest のインストール確認
```bash
# pytest がインストール済みか確認
uv run pytest --version

# テストの実行
uv run pytest tests/ -v
```

> **重要**: このプロジェクトでは必ず `uv run pytest` を使用してください。
> 詳細な実行方法は [pytestガイド](../pytest-guide.md) を参照してください。

#### 1.2 最初のテスト作成

**tests/test_basic.py**
```python
def test_simple_addition():
    """最も基本的なテスト"""
    assert 1 + 1 == 2

def test_string_operations():
    """文字列操作のテスト"""
    text = "Hello, World!"
    assert len(text) == 13
    assert text.upper() == "HELLO, WORLD!"
    assert "World" in text
```

**練習1**: 上記のテストファイルを作成し、実行してみてください。

```bash
uv run pytest tests/phase2/test_basic.py -v
```

#### 1.3 アサーションの種類

**tests/test_assertions.py**
```python
def test_equality():
    """等価性のテスト"""
    assert 5 == 5
    assert "hello" == "hello"
    assert [1, 2, 3] == [1, 2, 3]

def test_truthiness():
    """真偽値のテスト"""
    assert True
    assert not False
    assert "non-empty string"  # 空でない文字列はTrue
    assert [1, 2, 3]  # 空でないリストはTrue

def test_comparisons():
    """比較のテスト"""
    assert 10 > 5
    assert 3 <= 3
    assert 2.5 >= 2.0

def test_membership():
    """包含関係のテスト"""
    assert "hello" in "hello world"
    assert 3 in [1, 2, 3, 4]
    assert "key" in {"key": "value"}

def test_types():
    """型チェックのテスト"""
    assert isinstance(42, int)
    assert isinstance("hello", str)
    assert isinstance([1, 2, 3], list)
```

**練習2**: アサーションの練習をしてください。

### Step 2: Phase 1 コードのテスト設計（1-2時間）

#### 2.1 テスト対象の分析

Phase 1で作成したログ解析ツールの各機能を分析し、テストが必要な部分を特定します。

**テスト対象の機能**:
1. `parse_log_line()` - ログ行の解析
2. `parse_error_log_line()` - エラーログの解析  
3. `read_log_file()` - ファイル読み込み
4. `filter_by_level()` - レベル別フィルタ
5. `search_keyword()` - キーワード検索
6. `count_by_level()` - レベル別集計
7. `export_to_csv()` - CSV出力

#### 2.2 テストケースの設計

各機能について、以下の観点でテストケースを考えます：

**正常系（Happy Path）**:
- 期待通りの入力で期待通りの出力が得られるか

**異常系（Edge Cases）**:
- 不正な入力や想定外の状況での動作

**境界値（Boundary Cases）**:
- 空文字、None、最大値・最小値での動作

### Step 3: 実際のテスト実装（4-5時間）

#### 3.1 ログ解析関数のテスト

**tests/test_log_parser.py**
```python
"""
ログ解析機能のテスト

【課題1】
以下のテストクラスを実装してください。
Phase 1で作成した関数をテストします。
"""

import pytest
from src.practice_string_parse import parse_log_line, parse_error_log_line


class TestLogParser:
    """ログ解析のテストクラス"""
    
    def test_parse_access_log_success(self):
        """正常なアクセスログの解析テスト"""
        # TODO: 実装してください
        pass
    
    def test_parse_access_log_with_message(self):
        """メッセージ付きアクセスログの解析テスト"""
        # TODO: 実装してください
        pass
    
    def test_parse_access_log_invalid_format(self):
        """不正な形式のログの解析テスト"""
        # TODO: 実装してください
        pass
    
    def test_parse_access_log_empty_line(self):
        """空行の解析テスト"""
        # TODO: 実装してください
        pass
    
    def test_parse_error_log_success(self):
        """正常なエラーログの解析テスト"""
        # TODO: 実装してください
        pass
    
    def test_parse_error_log_invalid_format(self):
        """不正な形式のエラーログの解析テスト"""
        # TODO: 実装してください
        pass
```

**実装例** (学習者が参考にできるよう、一部実装例を示す):
```python
def test_parse_access_log_success(self):
    """正常なアクセスログの解析テスト"""
    line = "2024-01-15 09:23:45 INFO GET /api/users 200 45ms"
    result = parse_log_line(line)
    
    expected = {
        'date': '2024-01-15',
        'time': '09:23:45',
        'level': 'INFO',
        'method': 'GET',
        'path': '/api/users',
        'status': '200',
        'message': '45ms'
    }
    
    assert result == expected
```

#### 3.2 LogAnalyzerクラスのテスト

**tests/test_log_analyzer.py**
```python
"""
LogAnalyzerクラスのテスト

【課題2】
LogAnalyzerクラスの各メソッドのテストを実装してください。
"""

import pytest
import tempfile
import os
from src.log_analyzer import LogAnalyzer


class TestLogAnalyzer:
    """LogAnalyzerクラスのテストクラス"""
    
    @pytest.fixture
    def analyzer(self):
        """テスト用のLogAnalyzerインスタンスを作成"""
        return LogAnalyzer()
    
    @pytest.fixture
    def sample_log_file(self):
        """テスト用の一時ログファイルを作成"""
        # TODO: 実装してください
        pass
    
    def test_read_log_file_success(self, analyzer, sample_log_file):
        """ログファイル読み込み成功のテスト"""
        # TODO: 実装してください
        pass
    
    def test_read_log_file_not_found(self, analyzer):
        """存在しないファイルの読み込みテスト"""
        # TODO: 実装してください
        pass
    
    def test_filter_by_level(self, analyzer):
        """ログレベルフィルタのテスト"""
        # TODO: 実装してください
        pass
    
    def test_search_keyword(self, analyzer):
        """キーワード検索のテスト"""
        # TODO: 実装してください
        pass
    
    def test_count_by_level(self, analyzer):
        """レベル別集計のテスト"""
        # TODO: 実装してください
        pass
    
    def test_export_to_csv(self, analyzer):
        """CSV出力のテスト"""
        # TODO: 実装してください
        pass
```

#### 3.3 pytest fixtures の活用

**tests/conftest.py**
```python
"""
pytest設定とフィクスチャ

共通的に使用するテストデータやセットアップを定義します。
"""

import pytest
import tempfile
import os
from typing import List, Dict


@pytest.fixture
def sample_log_data():
    """テスト用のサンプルログデータ"""
    return [
        {
            'date': '2024-01-15',
            'time': '09:23:45',
            'level': 'INFO',
            'method': 'GET',
            'path': '/api/users',
            'status': '200',
            'message': '45ms'
        },
        {
            'date': '2024-01-15',
            'time': '09:24:33',
            'level': 'ERROR',
            'method': 'GET',
            'path': '/api/data',
            'status': '500',
            'message': 'Database connection failed'
        },
        {
            'date': '2024-01-15',
            'time': '09:25:15',
            'level': 'WARNING',
            'method': 'GET',
            'path': '/api/reports',
            'status': '404',
            'message': 'Resource not found'
        }
    ]


@pytest.fixture
def temp_log_file():
    """一時的なログファイルを作成"""
    content = """2024-01-15 09:23:45 INFO GET /api/users 200 45ms
2024-01-15 09:24:33 ERROR GET /api/data 500 234ms Database connection failed
2024-01-15 09:25:15 WARNING GET /api/reports 404 12ms Resource not found"""
    
    # 一時ファイルを作成
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as f:
        f.write(content)
        temp_file_path = f.name
    
    yield temp_file_path
    
    # テスト後にファイルを削除
    os.unlink(temp_file_path)


@pytest.fixture
def temp_csv_file():
    """一時的なCSVファイルパスを提供"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
        temp_file_path = f.name
    
    yield temp_file_path
    
    # テスト後にファイルを削除
    if os.path.exists(temp_file_path):
        os.unlink(temp_file_path)
```

### Step 4: テストの実行と改善（1-2時間）

#### 4.1 テスト実行

```bash
# すべてのテストを実行
uv run pytest

# 詳細な出力で実行
uv run pytest -v

# 特定のテストファイルのみ実行
uv run pytest tests/phase2/test_log_parser.py -v

# カバレッジ付きで実行
uv run pytest --cov=src --cov-report=html
```

#### 4.2 テスト結果の分析

テスト実行後、以下を確認します：

- **失敗したテスト**: なぜ失敗したのか原因を調査
- **カバレッジ**: どの部分がテストされていないか
- **実行時間**: テストが遅すぎないか

#### 4.3 Phase 1 コードの改善

テストを書く過程で、Phase 1のコードに問題が見つかることがあります：

- **バグの発見**: テストによって隠れていたバグが見つかる
- **設計の問題**: テストしにくいコードは設計に問題がある場合が多い
- **エラーハンドリング不足**: 異常系のテストで不備が発覚

**リファクタリングの例**:
```python
# 改善前: テストしにくい
def process_log_file(file_path):
    # ファイル読み込み、解析、フィルタ、出力がすべて一つの関数
    pass

# 改善後: 各機能を分離してテストしやすく
def read_log_file(file_path):
    pass

def parse_logs(raw_data):
    pass

def filter_logs(logs, criteria):
    pass

def export_results(data, output_path):
    pass
```

## 📝 完成チェックリスト

Phase 2 完了時に以下のテストが実装されていることを確認してください：

### 基本的なテスト
- [ ] `parse_log_line()` の正常系テスト
- [ ] `parse_log_line()` の異常系テスト
- [ ] `parse_error_log_line()` の正常系・異常系テスト

### LogAnalyzerクラスのテスト
- [ ] ファイル読み込み機能のテスト
- [ ] ログレベルフィルタ機能のテスト
- [ ] キーワード検索機能のテスト
- [ ] レベル別集計機能のテスト
- [ ] CSV出力機能のテスト

### テスト品質
- [ ] 各テストが独立して実行できる
- [ ] テストデータを適切に準備・クリーンアップしている
- [ ] エラーケースも含めて網羅的にテストしている
- [ ] テストの実行時間が適切（全体で30秒以内）

### テスト実行
- [ ] `uv run pytest` でエラーなく実行できる
- [ ] カバレッジが70%以上ある
- [ ] 継続的にテストを実行する習慣ができている

## 🎉 Phase 2 完了後

### 学んだことの振り返り
- テストを書くことで見つかったバグや問題は何でしたか？
- テストを書く前と後で、コードに対する安心感はどう変わりましたか？
- どのテストが一番書きにくかったですか？その理由は？

### 次のPhase 3への準備
Phase 3では「テスト駆動開発（TDD）」を学習します：
- Red: 失敗するテストを書く
- Green: テストを通す最小限のコード
- Refactor: コードを改善

Phase 2で「後からテストを書く大変さ」を体験したので、Phase 3では「最初にテストを書く」アプローチを学習しましょう。

## 💡 テスト作成のコツ

### 1. 小さく始める
- 最初は簡単な関数から
- 複雑なテストは段階的に作成

### 2. 読みやすいテスト
- テスト名で何をテストしているか明確に
- Given-When-Then パターンの活用

### 3. 独立性の確保
- テスト間で状態を共有しない
- 実行順序に依存しない

### 4. 現実的なテストデータ
- 実際の使用場面に近いデータを使用
- エッジケースも忘れずに

## 📚 参考資料

- [プロジェクト内pytestガイド](../pytest-guide.md) - 本プロジェクト専用のpytest実行ガイド
- [pytest公式ドキュメント](https://docs.pytest.org/)
- [Python Testing 101](https://python-testing-101.readthedocs.io/)
- [Effective Python Testing](https://testdriven.io/)