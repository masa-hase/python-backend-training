# Phase 3: TDD実践

## 🎯 Phase 3 の目標

TDD（Test Driven Development）の Red-Green-Refactor サイクルを実践します。
ログ解析ツールに新機能をテスト駆動で追加し、TDDの習慣を身につけます。

## ⏰ 推定学習時間

- **総時間**: 10-12時間
- **TDD基礎理解**: 2-3時間
- **TDD実践（新機能開発）**: 8-9時間

## 📚 学習内容

### 1. TDDの基礎理解
- TDDサイクル（Red-Green-Refactor）
- TDDのメリットと注意点
- テストファーストの考え方

### 2. TDD実践
- 失敗するテストを書く（Red）
- テストを通す最小限のコード（Green）
- コードを改善する（Refactor）

### 3. 新機能をTDDで開発
- ログの統計分析機能
- レポート生成機能
- フィルタ機能の拡張

## 🔄 TDDサイクル詳解

### Red（レッド）: 失敗するテストを書く
1. **機能の仕様を明確にする**
2. **その機能をテストするコードを書く**
3. **テストを実行して失敗することを確認**

### Green（グリーン）: テストを通す
1. **テストを通すために最小限のコードを書く**
2. **美しさは気にしない、とにかく動かす**
3. **テストが通ることを確認**

### Refactor（リファクタ）: コードを改善
1. **テストを通したまま、コードを整理**
2. **重複の除去、命名の改善、構造の整理**
3. **テストが引き続き通ることを確認**

## 🚀 Phase 3で追加する新機能

### 1. 統計分析機能
- **時間帯別アクセス統計**
- **レスポンス時間の統計（平均、最大、最小）**
- **HTTPステータスコード別の統計**

### 2. レポート生成機能
- **日次サマリーレポート**
- **エラー詳細レポート**
- **パフォーマンスレポート**

### 3. 高度なフィルタリング
- **日付範囲指定**
- **レスポンス時間範囲指定**
- **複合条件でのフィルタリング**

## 📋 学習手順

### Step 1: TDD基礎理解（2-3時間）

#### 1.1 TDDの基本サイクル練習

まず簡単な例でTDDサイクルを体験します。

> **pytestの実行方法について**
> このプロジェクトでは必ず `uv run pytest` を使用してください。
> 詳細な実行方法とTDDでの活用法は [pytestガイド](../pytest-guide.md#tddサイクルでの活用) を参照してください。

**tests/test_tdd_practice.py**
```python
"""
TDD練習用ファイル

【練習1】計算機クラスをTDDで作成してください
"""

import pytest
from src.calculator import Calculator  # まだ存在しないクラス


class TestCalculator:
    """計算機のTDDテスト"""
    
    def test_add_two_numbers(self):
        """2つの数の足し算をテスト"""
        # Red: まず失敗するテストを書く
        calc = Calculator()
        result = calc.add(2, 3)
        assert result == 5
        
    def test_subtract_two_numbers(self):
        """2つの数の引き算をテスト"""
        # TODO: 引き算のテストを書いてください
        pass
```

**TDD手順**:
1. **Red**: 上記テストを実行 → インポートエラーで失敗
   ```bash
   uv run pytest tests/phase3/test_tdd_practice.py::TestCalculator::test_add_two_numbers -v
   ```
2. **Green**: `src/phase3/calculator.py` を作成して最小限の実装
3. **Refactor**: コードを整理

#### 1.2 実装例（学習者が参考にできるよう）

**src/calculator.py**
```python
"""
TDD練習用の計算機クラス

【課題1】TDDサイクルで実装してください
"""

class Calculator:
    """TDD練習用の計算機クラス"""
    
    def add(self, a: int, b: int) -> int:
        """足し算"""
        # TODO: テストを通すために実装してください
        pass
    
    def subtract(self, a: int, b: int) -> int:
        """引き算"""
        # TODO: TDDで実装してください
        pass
```

### Step 2: ログ解析ツールの新機能設計（1時間）

#### 2.1 機能仕様の明確化

**追加する機能の詳細仕様**:

1. **時間帯別統計機能**
   - 各時間（0-23時）のアクセス数
   - ピーク時間の特定
   - 時間帯別エラー率

2. **レスポンス時間統計**
   - 平均レスポンス時間
   - 最大・最小レスポンス時間
   - レスポンス時間の分布

3. **日付範囲フィルタ**
   - 開始日時・終了日時での絞り込み
   - 特定日付のログ抽出

### Step 3: TDDで統計分析機能を実装（3-4時間）

#### 3.1 時間帯別統計のTDD実装

**tests/test_log_statistics.py**
```python
"""
ログ統計機能のTDDテスト

【課題2】時間帯別統計機能をTDDで実装してください
"""

import pytest
from src.log_statistics import LogStatistics


class TestLogStatistics:
    """ログ統計のテストクラス"""
    
    @pytest.fixture
    def sample_logs(self):
        """テスト用のログデータ"""
        return [
            {
                'date': '2024-01-15',
                'time': '09:23:45',
                'level': 'INFO',
                'status': '200',
                'message': '45ms'
            },
            {
                'date': '2024-01-15', 
                'time': '09:45:30',
                'level': 'INFO',
                'status': '200',
                'message': '67ms'
            },
            {
                'date': '2024-01-15',
                'time': '14:12:15',
                'level': 'ERROR',
                'status': '500',
                'message': '234ms'
            }
        ]
    
    def test_count_by_hour(self, sample_logs):
        """時間帯別のアクセス数集計テスト"""
        # Red: 失敗するテストを先に書く
        stats = LogStatistics(sample_logs)
        result = stats.count_by_hour()
        
        expected = {
            '09': 2,  # 9時台に2件
            '14': 1   # 14時台に1件
        }
        assert result == expected
    
    def test_calculate_peak_hour(self, sample_logs):
        """ピーク時間の特定テスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_calculate_error_rate_by_hour(self, sample_logs):
        """時間帯別エラー率の計算テスト"""
        # TODO: TDDで実装してください
        pass
```

**TDD実装手順**:
1. **Red**: テストを実行 → LogStatisticsクラスが存在しないため失敗
2. **Green**: 最小限のLogStatisticsクラスを作成
3. **Refactor**: コードを整理

#### 3.2 レスポンス時間統計のTDD実装

**tests/test_response_time_stats.py**
```python
"""
レスポンス時間統計のTDDテスト

【課題3】レスポンス時間統計をTDDで実装してください
"""

import pytest
from src.log_statistics import LogStatistics


class TestResponseTimeStatistics:
    """レスポンス時間統計のテスト"""
    
    @pytest.fixture
    def response_time_logs(self):
        """レスポンス時間付きログデータ"""
        return [
            {'message': '45ms', 'status': '200'},
            {'message': '67ms', 'status': '200'},
            {'message': '234ms', 'status': '500'},
            {'message': '12ms', 'status': '200'},
            {'message': '456ms', 'status': '500'}
        ]
    
    def test_extract_response_times(self, response_time_logs):
        """レスポンス時間の抽出テスト"""
        stats = LogStatistics(response_time_logs)
        times = stats.extract_response_times()
        
        expected = [45, 67, 234, 12, 456]
        assert times == expected
    
    def test_calculate_average_response_time(self, response_time_logs):
        """平均レスポンス時間の計算テスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_calculate_response_time_percentiles(self, response_time_logs):
        """レスポンス時間のパーセンタイル計算テスト"""
        # TODO: TDDで実装してください
        pass
```

### Step 4: TDDで高度なフィルタリング機能を実装（3-4時間）

#### 4.1 日付範囲フィルタのTDD実装

**tests/test_advanced_filters.py**
```python
"""
高度なフィルタリング機能のTDDテスト

【課題4】日付範囲フィルタをTDDで実装してください
"""

import pytest
from datetime import datetime, date
from src.log_filters import AdvancedLogFilter


class TestAdvancedLogFilter:
    """高度なログフィルタのテスト"""
    
    @pytest.fixture
    def multi_date_logs(self):
        """複数日のログデータ"""
        return [
            {'date': '2024-01-15', 'time': '09:23:45', 'level': 'INFO'},
            {'date': '2024-01-16', 'time': '10:30:15', 'level': 'ERROR'},
            {'date': '2024-01-17', 'time': '14:45:30', 'level': 'WARNING'},
            {'date': '2024-01-18', 'time': '16:20:45', 'level': 'INFO'}
        ]
    
    def test_filter_by_date_range(self, multi_date_logs):
        """日付範囲でのフィルタリングテスト"""
        filter_obj = AdvancedLogFilter(multi_date_logs)
        
        start_date = date(2024, 1, 16)
        end_date = date(2024, 1, 17)
        
        result = filter_obj.filter_by_date_range(start_date, end_date)
        
        assert len(result) == 2
        assert result[0]['date'] == '2024-01-16'
        assert result[1]['date'] == '2024-01-17'
    
    def test_filter_by_response_time_range(self):
        """レスポンス時間範囲でのフィルタリングテスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_filter_by_multiple_conditions(self):
        """複合条件でのフィルタリングテスト"""
        # TODO: TDDで実装してください
        pass
```

### Step 5: TDDでレポート生成機能を実装（2-3時間）

#### 5.1 日次サマリーレポートのTDD

**tests/test_report_generator.py**
```python
"""
レポート生成機能のTDDテスト

【課題5】レポート生成機能をTDDで実装してください
"""

import pytest
from src.report_generator import ReportGenerator


class TestReportGenerator:
    """レポート生成のテスト"""
    
    def test_generate_daily_summary(self):
        """日次サマリーレポート生成テスト"""
        # TODO: TDDで実装してください
        pass
    
    def test_generate_error_report(self):
        """エラーレポート生成テスト"""  
        # TODO: TDDで実装してください
        pass
    
    def test_generate_performance_report(self):
        """パフォーマンスレポート生成テスト"""
        # TODO: TDDで実装してください
        pass
```

### Step 6: 実装ファイルの作成（スケルトン）

#### 6.1 統計分析クラス

**src/log_statistics.py**
```python
"""
ログ統計分析機能

【課題2-3】TDDで実装してください
"""

from typing import List, Dict, Any
from collections import defaultdict


class LogStatistics:
    """ログの統計分析を行うクラス"""
    
    def __init__(self, log_data: List[Dict[str, Any]]):
        """
        初期化
        
        Args:
            log_data: 解析対象のログデータ
        """
        self.log_data = log_data
    
    def count_by_hour(self) -> Dict[str, int]:
        """時間帯別のアクセス数を集計"""
        # TODO: TDDで実装してください
        pass
    
    def calculate_peak_hour(self) -> str:
        """最もアクセスが多い時間帯を特定"""
        # TODO: TDDで実装してください
        pass
    
    def calculate_error_rate_by_hour(self) -> Dict[str, float]:
        """時間帯別のエラー率を計算"""
        # TODO: TDDで実装してください
        pass
    
    def extract_response_times(self) -> List[int]:
        """レスポンス時間を抽出してリストで返す"""
        # TODO: TDDで実装してください
        pass
    
    def calculate_average_response_time(self) -> float:
        """平均レスポンス時間を計算"""
        # TODO: TDDで実装してください
        pass
    
    def calculate_response_time_percentiles(self) -> Dict[str, float]:
        """レスポンス時間のパーセンタイル（50%, 90%, 95%）を計算"""
        # TODO: TDDで実装してください
        pass
```

#### 6.2 高度なフィルタクラス

**src/log_filters.py**
```python
"""
高度なログフィルタリング機能

【課題4】TDDで実装してください
"""

from typing import List, Dict, Any, Optional
from datetime import date, datetime


class AdvancedLogFilter:
    """高度なログフィルタリングを行うクラス"""
    
    def __init__(self, log_data: List[Dict[str, Any]]):
        """
        初期化
        
        Args:
            log_data: フィルタ対象のログデータ
        """
        self.log_data = log_data
    
    def filter_by_date_range(self, start_date: date, end_date: date) -> List[Dict[str, Any]]:
        """日付範囲でフィルタリング"""
        # TODO: TDDで実装してください
        pass
    
    def filter_by_response_time_range(self, min_time: int, max_time: int) -> List[Dict[str, Any]]:
        """レスポンス時間範囲でフィルタリング"""
        # TODO: TDDで実装してください
        pass
    
    def filter_by_multiple_conditions(self, **conditions) -> List[Dict[str, Any]]:
        """複数条件でフィルタリング"""
        # TODO: TDDで実装してください
        pass
```

#### 6.3 レポート生成クラス

**src/report_generator.py**
```python
"""
レポート生成機能

【課題5】TDDで実装してください
"""

from typing import List, Dict, Any
from src.log_statistics import LogStatistics
from src.log_filters import AdvancedLogFilter


class ReportGenerator:
    """ログレポートを生成するクラス"""
    
    def __init__(self, log_data: List[Dict[str, Any]]):
        """
        初期化
        
        Args:
            log_data: レポート対象のログデータ
        """
        self.log_data = log_data
        self.statistics = LogStatistics(log_data)
    
    def generate_daily_summary(self, target_date: str) -> Dict[str, Any]:
        """日次サマリーレポートを生成"""
        # TODO: TDDで実装してください
        pass
    
    def generate_error_report(self) -> Dict[str, Any]:
        """エラーレポートを生成"""
        # TODO: TDDで実装してください
        pass
    
    def generate_performance_report(self) -> Dict[str, Any]:
        """パフォーマンスレポートを生成"""
        # TODO: TDDで実装してください
        pass
```

## 📝 TDD実践のポイント

### 1. 小さなステップで進む
- 一度に多くの機能を実装しない
- 1つのテストケースごとにRed-Green-Refactorを実行

### 2. テストファースト
- 実装コードを書く前に必ずテストを書く
- テストが失敗することを確認してから実装開始

### 3. 最小限の実装
- テストを通すために最小限のコードだけを書く
- 「将来使うかも」の機能は実装しない

### 4. リファクタリングを恐れない
- テストがあるので安心してコード改善可能
- 重複の除去、命名の改善を積極的に行う

## 📝 完成チェックリスト

Phase 3 完了時に以下が実装されていることを確認してください：

### TDD基礎
- [ ] 簡単な計算機クラスをTDDで実装した
- [ ] Red-Green-Refactorサイクルを体験した

### 統計分析機能（TDDで実装）
- [ ] 時間帯別アクセス数集計
- [ ] ピーク時間特定
- [ ] 時間帯別エラー率計算
- [ ] レスポンス時間統計（平均、最大、最小）
- [ ] レスポンス時間パーセンタイル

### フィルタリング機能（TDDで実装）
- [ ] 日付範囲指定フィルタ
- [ ] レスポンス時間範囲フィルタ
- [ ] 複合条件フィルタ

### レポート生成機能（TDDで実装）
- [ ] 日次サマリーレポート
- [ ] エラー詳細レポート
- [ ] パフォーマンスレポート

### TDD品質
- [ ] すべての新機能がテストファーストで実装されている
- [ ] テストカバレッジが90%以上
- [ ] リファクタリングが適切に行われている
- [ ] テストが独立して実行できる

## 🎉 Phase 3 完了後

### 学習の振り返り
- TDDで開発することの利点を実感できましたか？
- 最初にテストを書くことに慣れましたか？
- リファクタリング時の安心感はどうでしたか？
- Phase 2（後付けテスト）との違いを感じましたか？

### 身についたスキル
- **テストファーストの思考**
- **段階的な機能実装**
- **安全なリファクタリング**
- **仕様の明確化**

次のPhase 4では、これまでのCLIツールをWebアプリケーション化し、TDDでWeb API開発を学習します！

## 💡 TDD成功のコツ

### 1. テストを小さく保つ
- 1つのテストで1つの機能のみテスト
- 複雑なテストは分割する

### 2. 意味のあるテスト名
- テスト名を見ただけで何をテストしているか分かる
- 日本語でも英語でも構わない

### 3. Given-When-Then パターン
```python
def test_filter_logs_by_error_level():
    # Given（前提条件）
    logs = [sample_log_data]
    filter_obj = LogFilter(logs)
    
    # When（実行）
    result = filter_obj.filter_by_level('ERROR')
    
    # Then（検証）
    assert len(result) == expected_count
```

### 4. 継続的なリファクタリング
- テストが通る状態を保ちながら改善
- 重複コードの除去
- 可読性の向上

## 🛠️ TDD実践でのpytest活用

### 基本的な実行フロー

```bash
# 1. Red Phase: 新しいテストを書いて失敗を確認
uv run pytest tests/phase3/test_new_feature.py -v

# 2. 失敗の詳細を確認（変数の値など）
uv run pytest tests/phase3/test_new_feature.py -vv

# 3. Green Phase: 実装後、テストが通ることを確認
uv run pytest tests/phase3/test_new_feature.py -v

# 4. Refactor Phase: すべてのテストが通り続けることを確認
uv run pytest tests/phase3/ -v
```

### TDD実践での便利なオプション

```bash
# 最初の失敗で停止（Red Phaseで原因特定）
uv run pytest -x

# 前回失敗したテストのみ実行（効率的なGreen Phase）
uv run pytest --lf

# ファイル変更を監視して自動実行（pytest-watchプラグイン使用時）
uv run ptw tests/phase3/

# カバレッジを確認（実装の網羅性チェック）
uv run pytest tests/phase3/ --cov=src/phase3 --cov-report=html
```

### デバッグ支援

```bash
# pdbデバッガーを起動（実装が難しい時）
uv run pytest --pdb

# print文の出力を表示（デバッグ用）
uv run pytest -s
```

詳細は [pytestガイド](../pytest-guide.md) を参照してください。