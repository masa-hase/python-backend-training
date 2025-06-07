# Phase 1: ログ解析ツール開発

## 🎯 Phase 1 の目標

Python基礎の復習を兼ねて、業務で実用的なログ解析ツールを作成します。
テストは書かずに、まずは動くものを作ることに集中しましょう。

## ⏰ 推定学習時間

- **総時間**: 12-15時間
- **環境慣れ・Python基礎復習**: 3-4時間
- **ツール開発**: 10-12時間

## 📚 学習内容

### 1. Python基礎復習
- ファイル読み書き
- 文字列操作
- リスト・辞書の操作
- 関数とクラスの基本

### 2. バックエンド要素
- ファイル入出力（テキスト、CSV）
- 例外処理・エラーハンドリング
- ログ出力
- 外部ライブラリの使用

### 3. 実装する機能
- ログファイルの読み込み
- キーワード・パターン検索
- 基本集計（行数カウント、時間別集計）
- 結果の出力（コンソール・CSV）

## 🛠 作成するツール仕様

### 基本機能
1. **ログファイル読み込み**
   - 単一ファイルの読み込み
   - 複数ファイルの一括処理

2. **検索・フィルタリング**
   - キーワード検索
   - ログレベル別フィルタ（ERROR、WARNING、INFO）
   - 日時範囲での絞り込み

3. **集計機能**
   - マッチした行数のカウント
   - ログレベル別の件数集計
   - 時間別の集計

4. **結果出力**
   - コンソールへの結果表示
   - CSV形式での保存

### 使用例
```bash
# エラーログだけを抽出
python src/log_analyzer.py data/sample_logs/access.log --level ERROR

# キーワード検索
python src/log_analyzer.py data/sample_logs/access.log --keyword "Database"

# 結果をCSVで保存
python src/log_analyzer.py data/sample_logs/access.log --output results.csv
```

## 📋 学習手順

### Step 1: 環境確認とPython基礎復習（3-4時間）

#### 1.1 開発環境の確認
```bash
# Python バージョン確認
python --version

# 依存関係のインストール
uv sync

# サンプルログファイルの確認
ls -la data/sample_logs/
cat data/sample_logs/access.log
```

#### 1.2 Python基礎復習
基本的なファイル操作から始めましょう。

**練習1: ファイル読み込み**
```python
# src/practice_file_read.py
def read_log_file(file_path):
    """ログファイルを読み込んで行数を数える"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(f"ファイル: {file_path}")
            print(f"総行数: {len(lines)}")
            
            # 最初の5行を表示
            print("最初の5行:")
            for i, line in enumerate(lines[:5]):
                print(f"{i+1}: {line.strip()}")
                
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    read_log_file("data/sample_logs/access.log")
```

**課題1**: 上記のコードを実装して実行し、動作を確認してください。

#### 1.3 文字列操作の復習

**練習2: ログ行の解析**
```python
# src/practice_string_parse.py
def parse_log_line(line):
    """ログ行を解析して各要素を抽出する"""
    # 例: "2024-01-15 09:23:45 INFO GET /api/users 200 45ms"
    parts = line.strip().split()
    
    if len(parts) >= 6:
        log_data = {
            'date': parts[0],
            'time': parts[1],
            'level': parts[2],
            'method': parts[3],
            'path': parts[4],
            'status': parts[5]
        }
        return log_data
    return None

def analyze_sample_logs():
    """サンプルログを解析してみる"""
    sample_lines = [
        "2024-01-15 09:23:45 INFO GET /api/users 200 45ms",
        "2024-01-15 09:24:33 ERROR GET /api/data 500 234ms Database connection failed",
    ]
    
    for line in sample_lines:
        data = parse_log_line(line)
        if data:
            print(f"解析結果: {data}")

if __name__ == "__main__":
    analyze_sample_logs()
```

**課題2**: 上記のコードを実装し、ログ行の解析ができることを確認してください。

### Step 2: 基本的なログ解析ツールの実装（5-6時間）

#### 2.1 基本クラスの設計

**src/log_analyzer.py**
```python
import os
import csv
from datetime import datetime
from typing import List, Dict, Optional

class LogAnalyzer:
    """ログファイルを解析するクラス"""
    
    def __init__(self):
        self.log_data: List[Dict] = []
    
    def read_log_file(self, file_path: str) -> bool:
        """ログファイルを読み込む"""
        # TODO: 実装してください
        pass
    
    def parse_line(self, line: str) -> Optional[Dict]:
        """ログ行を解析する"""
        # TODO: 実装してください
        pass
    
    def filter_by_level(self, level: str) -> List[Dict]:
        """ログレベルでフィルタリング"""
        # TODO: 実装してください
        pass
    
    def search_keyword(self, keyword: str) -> List[Dict]:
        """キーワードで検索"""
        # TODO: 実装してください
        pass
    
    def count_by_level(self) -> Dict[str, int]:
        """ログレベル別の件数を集計"""
        # TODO: 実装してください
        pass
    
    def export_to_csv(self, results: List[Dict], output_path: str):
        """結果をCSVファイルに出力"""
        # TODO: 実装してください
        pass

def main():
    """メイン関数"""
    analyzer = LogAnalyzer()
    
    # ファイル読み込み
    if analyzer.read_log_file("data/sample_logs/access.log"):
        print("ログファイルの読み込みが完了しました")
        
        # 基本統計の表示
        total_lines = len(analyzer.log_data)
        print(f"総ログ行数: {total_lines}")
        
        # レベル別集計
        level_counts = analyzer.count_by_level()
        print("ログレベル別件数:")
        for level, count in level_counts.items():
            print(f"  {level}: {count}件")

if __name__ == "__main__":
    main()
```

**課題3**: 上記のクラス構造を参考に、各メソッドを順番に実装してください。

#### 2.2 実装のヒント

**read_log_file メソッドの実装例**:
```python
def read_log_file(self, file_path: str) -> bool:
    """ログファイルを読み込む"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parsed_data = self.parse_line(line)
                if parsed_data:
                    self.log_data.append(parsed_data)
        return True
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
        return False
    except Exception as e:
        print(f"ファイル読み込みエラー: {e}")
        return False
```

### Step 3: 機能拡張と改善（4-5時間）

#### 3.1 コマンドライン対応
clickライブラリを使って、コマンドライン引数に対応します。

```python
import click

@click.command()
@click.argument('log_file', type=click.Path(exists=True))
@click.option('--level', help='フィルタするログレベル (INFO/WARNING/ERROR)')
@click.option('--keyword', help='検索するキーワード')
@click.option('--output', help='結果を保存するCSVファイル名')
def analyze_log(log_file, level, keyword, output):
    """ログファイルを解析するコマンドラインツール"""
    analyzer = LogAnalyzer()
    
    if not analyzer.read_log_file(log_file):
        return
    
    results = analyzer.log_data
    
    # フィルタリング
    if level:
        results = analyzer.filter_by_level(level)
        print(f"{level}レベルのログ: {len(results)}件")
    
    if keyword:
        results = analyzer.search_keyword(keyword)
        print(f"'{keyword}'を含むログ: {len(results)}件")
    
    # 結果表示
    for log_entry in results[:10]:  # 最初の10件のみ表示
        print(f"{log_entry['date']} {log_entry['time']} [{log_entry['level']}] {log_entry.get('message', '')}")
    
    # CSV出力
    if output:
        analyzer.export_to_csv(results, output)
        print(f"結果を {output} に保存しました")

if __name__ == "__main__":
    analyze_log()
```

#### 3.2 ログ出力機能の追加
Pythonの標準ライブラリを使ってログ出力機能を追加します。

```python
import logging

# ログ設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('log_analyzer.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
```

**課題4**: ログ出力機能を各メソッドに追加し、処理の状況が分かるようにしてください。

#### 3.3 エラーハンドリングの改善
各処理でより詳細なエラーハンドリングを実装します。

### Step 4: 動作確認とテスト（1-2時間）

#### 4.1 基本動作の確認
```bash
# 基本実行
python src/log_analyzer.py data/sample_logs/access.log

# ERRORレベルのみ表示
python src/log_analyzer.py data/sample_logs/access.log --level ERROR

# キーワード検索
python src/log_analyzer.py data/sample_logs/access.log --keyword "Database"

# 結果をCSVに保存
python src/log_analyzer.py data/sample_logs/access.log --output results.csv
```

#### 4.2 複数ファイル対応（発展課題）
時間に余裕があれば、複数のログファイルを一括で処理できる機能を追加してみましょう。

## 📝 完成チェックリスト

Phase 1 完了時に以下の機能が動作することを確認してください：

- [ ] ログファイルの読み込みができる
- [ ] ログレベル別のフィルタリングができる
- [ ] キーワード検索ができる
- [ ] ログレベル別の件数集計ができる
- [ ] 結果をCSVファイルに出力できる
- [ ] コマンドライン引数で動作する
- [ ] 適切なエラーハンドリングがされている
- [ ] ログ出力機能が動作する

## 🎉 Phase 1 完了後

このPhaseが完了したら：

1. 作業内容をcommitしてください
2. `develop_[あなたの名前]` ブランチでPull Requestを作成
3. PR作成時は以下をコメントに記載：
   - 実装した機能の一覧
   - 動作確認した内容
   - 困った点や学んだこと

次のPhase 2では、このツールにテストを追加していきます！

## 💡 ヒントとコツ

- **小さく始める**: 最初は最小限の機能から実装し、徐々に拡張していく
- **エラーハンドリング**: ファイルが存在しない場合など、様々なエラーケースを考慮する
- **デバッグ**: print文やloggerを活用して、プログラムの動作を確認しながら進める
- **リファクタリング**: 動くものができたら、コードを整理して読みやすくする

## 📚 参考資料

- [Pythonファイル操作の基本](https://docs.python.org/ja/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Click Documentation](https://click.palletsprojects.com/)
- [Python Logging HOWTO](https://docs.python.org/ja/3/howto/logging.html)