# pytest実行ガイド - TDD学習のための完全マニュアル

このドキュメントは、python-backend-trainingプロジェクトでTDD（テスト駆動開発）を学習する際に必要なpytestの使い方をまとめたものです。

## 目次

1. [pytestの基本](#pytestの基本)
2. [テストの実行方法](#テストの実行方法)
3. [テストの書き方](#テストの書き方)
4. [TDDサイクルでの活用](#tddサイクルでの活用)
5. [便利な機能とオプション](#便利な機能とオプション)
6. [トラブルシューティング](#トラブルシューティング)

## pytestの基本

### pytestとは

pytestは、Pythonの最も人気のあるテストフレームワークです。シンプルで強力、そして拡張性があります。

### なぜpytestを使うのか

- **シンプルな文法**: `assert`文だけでテストが書ける
- **自動検出**: テストファイルとテスト関数を自動的に見つける
- **詳細なエラー情報**: テスト失敗時に分かりやすい情報を表示
- **豊富な機能**: フィクスチャ、パラメトリックテスト、プラグインなど

## テストの実行方法

### 基本的な実行コマンド

```bash
# プロジェクトでは必ずuvを使って実行
uv run pytest

# 特定のファイルをテスト
uv run pytest tests/phase3/test_tdd_practice.py

# 特定のクラスをテスト
uv run pytest tests/phase3/test_tdd_practice.py::TestCalculator

# 特定のテストメソッドをテスト
uv run pytest tests/phase3/test_tdd_practice.py::TestCalculator::test_add_two_numbers

# 詳細表示（推奨）
uv run pytest -v

# 失敗したテストで停止
uv run pytest -x

# 失敗したテストの詳細を表示
uv run pytest -vv
```

### TDD実践での実行フロー

```bash
# 1. Red Phase: テストが失敗することを確認
uv run pytest tests/phase3/test_tdd_practice.py -v

# 2. Green Phase: 実装後、テストが通ることを確認
uv run pytest tests/phase3/test_tdd_practice.py -v

# 3. Refactor Phase: リファクタリング後もテストが通ることを確認
uv run pytest tests/phase3/test_tdd_practice.py -v
```

### 便利な実行オプション

```bash
# キーワードでテストを絞り込み
uv run pytest -k "add"  # "add"を含むテストのみ実行

# 前回失敗したテストのみ実行
uv run pytest --lf

# カバレッジレポート付きで実行
uv run pytest --cov=src tests/

# 実行時間の遅いテストを表示
uv run pytest --durations=10

# print文の出力を表示
uv run pytest -s
```

## テストの書き方

### 基本的なテストの構造

```python
# tests/test_example.py

def test_should_add_two_numbers():
    """テスト関数の名前は必ず test_ で始める"""
    # Given: 準備
    a = 2
    b = 3
    
    # When: 実行
    result = a + b
    
    # Then: 検証
    assert result == 5
```

### クラスベースのテスト

```python
# tests/phase3/test_calculator.py

class TestCalculator:
    """テストクラスの名前は必ず Test で始める"""
    
    def test_add_positive_numbers(self):
        """正の数の足し算をテスト"""
        calc = Calculator()
        assert calc.add(2, 3) == 5
    
    def test_add_negative_numbers(self):
        """負の数の足し算をテスト"""
        calc = Calculator()
        assert calc.add(-1, -2) == -3
```

### アサーション（検証）の書き方

```python
# 基本的な等価性チェック
assert result == expected_value

# 真偽値のチェック
assert is_valid is True
assert has_error is False

# 包含関係のチェック
assert "error" in message
assert item in collection

# 型のチェック
assert isinstance(result, int)

# 例外のチェック
import pytest

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)

# カスタムメッセージ付きアサーション
assert result == 5, f"Expected 5, but got {result}"
```

### フィクスチャの使い方

```python
import pytest

@pytest.fixture
def sample_log_data():
    """テスト用のサンプルデータを提供"""
    return [
        {'level': 'INFO', 'message': 'Start processing'},
        {'level': 'ERROR', 'message': 'Connection failed'},
    ]

def test_filter_by_level(sample_log_data):
    """フィクスチャを引数として受け取る"""
    analyzer = LogAnalyzer()
    analyzer.log_data = sample_log_data
    
    errors = analyzer.filter_by_level('ERROR')
    assert len(errors) == 1
    assert errors[0]['message'] == 'Connection failed'
```

### パラメトリックテスト

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (1, 1, 2),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_various_numbers(a, b, expected):
    """複数のテストケースを一度に実行"""
    calc = Calculator()
    assert calc.add(a, b) == expected
```

## TDDサイクルでの活用

### 1. Red Phase（失敗するテストを書く）

```python
# tests/test_new_feature.py
def test_calculate_average():
    """まだ実装していない機能のテスト"""
    stats = Statistics([1, 2, 3, 4, 5])
    assert stats.calculate_average() == 3.0
```

実行:
```bash
uv run pytest tests/test_new_feature.py -v
# FAILED（AttributeError: 'Statistics' object has no attribute 'calculate_average'）
```

### 2. Green Phase（最小限の実装）

```python
# src/statistics.py
class Statistics:
    def __init__(self, data):
        self.data = data
    
    def calculate_average(self):
        return sum(self.data) / len(self.data)
```

実行:
```bash
uv run pytest tests/test_new_feature.py -v
# PASSED
```

### 3. Refactor Phase（コードの改善）

```python
# src/statistics.py
class Statistics:
    def __init__(self, data):
        self.data = data
    
    def calculate_average(self):
        """平均値を計算（空リストの処理を追加）"""
        if not self.data:
            return 0.0
        return sum(self.data) / len(self.data)
```

## 便利な機能とオプション

### テスト出力のカスタマイズ

```bash
# 成功したテストも詳細表示
uv run pytest -v

# より詳細な情報（変数の値など）
uv run pytest -vv

# プログレスバーなし
uv run pytest -q

# カラー出力を無効化
uv run pytest --color=no
```

### テストの選択的実行

```bash
# マーカーでフィルタ
uv run pytest -m "slow"

# 特定のディレクトリのみ
uv run pytest tests/phase3/

# ファイル名パターンでフィルタ
uv run pytest tests/test_*.py
```

### デバッグ支援

```bash
# 最初の失敗で停止
uv run pytest -x

# pdbデバッガーを起動
uv run pytest --pdb

# 失敗時のローカル変数を表示
uv run pytest -l

# トレースバックを短く表示
uv run pytest --tb=short
```

## プロジェクト固有の設定

このプロジェクトの`pyproject.toml`には以下の設定があります：

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]              # テストディレクトリ
python_files = "test_*.py"         # テストファイルパターン
python_classes = "Test*"           # テストクラスパターン
python_functions = "test_*"        # テスト関数パターン
addopts = "-v --tb=short"          # デフォルトオプション
```

これにより、`uv run pytest`を実行するだけで適切な設定でテストが実行されます。

## トラブルシューティング

### よくある問題と解決方法

#### 1. ImportError: モジュールが見つからない

```bash
# プロジェクトルートから実行しているか確認
pwd

# 正しいディレクトリに移動
cd /path/to/python-backend-training

# uvで実行しているか確認
uv run pytest  # ○
pytest        # × （グローバルのpytestを使ってしまう）
```

#### 2. テストが検出されない

```python
# × 間違い：test_で始まっていない
def calculate_test():
    pass

# ○ 正しい：test_で始まる
def test_calculate():
    pass
```

#### 3. フィクスチャが見つからない

```python
# conftest.pyに共通フィクスチャを定義
# tests/conftest.py
import pytest

@pytest.fixture
def common_fixture():
    return "shared data"
```

#### 4. 相対インポートエラー

```python
# × 間違い：相対インポート
from ..src.calculator import Calculator

# ○ 正しい：絶対インポート
from src.calculator import Calculator
```

## Phase別の実行例

### Phase 2: 既存コードにテストを追加

```bash
# 基本的なテストの練習
uv run pytest tests/phase2/test_basic.py -v

# アサーションの練習
uv run pytest tests/phase2/test_assertions.py -v

# 実際のコードのテスト
uv run pytest tests/phase2/test_log_analyzer.py -v
```

### Phase 3: TDD実践

```bash
# Step 1: 全てのテストが失敗することを確認（Red）
uv run pytest tests/phase3/ -v

# Step 2: 一つずつ実装してテストを通す（Green）
uv run pytest tests/phase3/test_tdd_practice.py::TestCalculator::test_add_two_numbers -v

# Step 3: 全体のテストを実行
uv run pytest tests/phase3/ -v

# カバレッジも確認
uv run pytest tests/phase3/ --cov=src/phase3 --cov-report=html
```

### Phase 4: Web API開発でのテスト

```bash
# APIのテスト
uv run pytest tests/phase4/test_api_basic.py -v

# DDDのテスト
uv run pytest tests/phase4/test_ddd_entities.py -v
```

## まとめ

pytestを使ったTDDの基本的な流れ：

1. **テストを書く**（Red）
   - `test_`で始まる関数名
   - 明確なテスト名
   - Given-When-Thenパターン

2. **実装する**（Green）
   - 最小限の実装
   - テストが通ることを確認

3. **改善する**（Refactor）
   - コードの品質向上
   - テストが通り続けることを確認

4. **繰り返す**
   - 小さなステップで進む
   - 常にテストを実行

このガイドを参考に、TDDでの開発を実践してください！