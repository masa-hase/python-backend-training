# トラブルシューティングガイド

## 🚨 一般的な問題と解決方法

### 環境・セットアップ関連

#### 1. devcontainerが起動しない
**症状**: VS Code でdevcontainerが正常に開けない

**原因と解決方法**:
- **Docker未起動**: Dockerが起動していることを確認
- **メモリ不足**: Dockerに十分なメモリが割り当てられているか確認（最低4GB推奨）
- **ファイル権限**: プロジェクトフォルダへのアクセス権限を確認

```bash
# Docker の状態確認
docker --version
docker ps

# Dockerの再起動
# Windows: Docker Desktop を再起動
# Mac: Docker Desktop を再起動
```

#### 2. uvコマンドが見つからない
**症状**: `uv: command not found`

**解決方法**:
```bash
# devcontainer内でuvが使えるかチェック
which uv

# もしuvがない場合は再構築
# VS Code: Ctrl+Shift+P → "Dev Containers: Rebuild Container"
```

#### 3. Python パッケージがインストールされない
**症状**: `import click` などでModuleNotFoundError

**解決方法**:
```bash
# 依存関係を再インストール
uv sync

# 特定のパッケージを追加インストール
uv add click pandas rich

# 仮想環境の確認
uv venv --help
```

### Phase 1: ログ解析ツール関連

#### 4. ファイルが見つからないエラー
**症状**: `FileNotFoundError: [Errno 2] No such file or directory`

**原因と解決方法**:
```bash
# 現在のディレクトリを確認
pwd

# ファイルの存在確認
ls -la data/sample_logs/

# 正しいパスで実行
python src/log_analyzer.py data/sample_logs/access.log

# Windows の場合、パスの区切り文字に注意
python src/log_analyzer.py data\\sample_logs\\access.log
```

#### 5. 文字エンコーディングエラー
**症状**: `UnicodeDecodeError`

**解決方法**:
```python
# log_analyzer.py で明示的にエンコーディング指定
with open(file_path, 'r', encoding='utf-8') as file:
    # または
with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
```

#### 6. CSVファイルが正しく出力されない
**症状**: CSV出力時にエラーが発生、または文字化け

**解決方法**:
```python
# CSVファイルのエンコーディングを明示的に指定
with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
# Excel で開く場合はBOM付きUTF-8
with open(output_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
```

#### 7. ログ解析結果が期待通りでない
**症状**: フィルタリング結果が空、または期待と違う

**デバッグ方法**:
```python
# デバッグ用のprint文を追加
def parse_line(self, line):
    print(f"DEBUG: 解析中の行: {line.strip()}")
    result = self._parse_access_log_line(line)
    print(f"DEBUG: 解析結果: {result}")
    return result

# ログレベルの大文字小文字を確認
print(f"検索対象レベル: '{level.upper()}'")
for log in self.log_data[:5]:  # 最初の5件をチェック
    print(f"ログのレベル: '{log.get('level', '')}'")
```

### コマンドライン実行関連

#### 8. click のオプションが認識されない
**症状**: `No such option: --level`

**解決方法**:
```bash
# ヘルプを確認
python src/log_analyzer.py --help

# オプション名を正確に指定
python src/log_analyzer.py data/sample_logs/access.log --level ERROR

# クオートが必要な場合
python src/log_analyzer.py data/sample_logs/access.log --keyword "Database connection"
```

#### 9. 権限エラーでファイルが作成できない
**症状**: `PermissionError: [Errno 13] Permission denied`

**解決方法**:
```bash
# 現在の権限を確認
ls -la

# 出力ディレクトリの権限を確認
mkdir -p results
python src/log_analyzer.py data/sample_logs/access.log --output results/output.csv

# Windows の場合、管理者権限で実行するか、ユーザーディレクトリに出力
python src/log_analyzer.py data/sample_logs/access.log --output "%USERPROFILE%\\output.csv"
```

### Git・GitHub関連

#### 10. ブランチ作成でエラー
**症状**: ブランチが作成できない、または切り替えできない

**解決方法**:
```bash
# 現在のブランチ確認
git branch

# 新しいブランチを作成して切り替え
git checkout -b develop_[あなたの名前]

# リモートの最新情報を取得
git fetch origin

# mainブランチから作業ブランチを作成
git checkout main
git pull origin main
git checkout -b develop_[あなたの名前]
```

#### 11. コミット時のエラー
**症状**: コミットができない、またはpushできない

**解決方法**:
```bash
# ファイルの状態確認
git status

# ファイルをステージング
git add src/log_analyzer.py
git add data/sample_logs/

# コミット
git commit -m "Phase 1: ログ解析ツールの基本機能を実装"

# プッシュ（初回）
git push -u origin develop_[あなたの名前]
```

### パフォーマンス関連

#### 12. 大きなログファイルで処理が遅い
**症状**: 大容量ファイルの処理に時間がかかる

**改善方法**:
```python
# ファイルを一行ずつ処理（メモリ効率化）
def read_log_file_streaming(self, file_path: str) -> bool:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                if line_num % 10000 == 0:  # 進捗表示
                    print(f"処理中: {line_num}行目")
                
                parsed_data = self.parse_line(line)
                if parsed_data:
                    self.log_data.append(parsed_data)
        return True
    except Exception as e:
        logger.error(f"ファイル読み込みエラー: {e}")
        return False
```

### その他

#### 13. 学習の進捗が不安
**症状**: 理解できているか不安、進捗が遅いと感じる

**対処方法**:
- **小さな目標設定**: 1つの機能ずつ確実に実装
- **動作確認の徹底**: 各ステップで必ず動作確認
- **質問・相談**: 分からない点は積極的に質問
- **学習ログ**: 毎日の学習内容と気づきを記録

#### 14. コードが汚くて不安
**症状**: 書いたコードがきれいでない気がする

**改善方法**:
- **段階的改善**: まず動くものを作り、後で整理
- **関数分割**: 長い関数は小さな関数に分割
- **変数名**: 分かりやすい名前に変更
- **コメント**: 複雑な処理には説明を追加

```python
# 改善前
def process(data):
    result = []
    for d in data:
        if d[2] == "ERROR":
            result.append(d)
    return result

# 改善後
def filter_error_logs(log_data: List[Dict]) -> List[Dict]:
    """ERRORレベルのログのみを抽出する"""
    error_logs = []
    for log_entry in log_data:
        if log_entry.get('level') == 'ERROR':
            error_logs.append(log_entry)
    return error_logs
```

## 🆘 緊急時の連絡方法

1. **技術的な問題**: [メンター/サポート担当者の連絡先]
2. **環境問題**: [IT管理者の連絡先] 
3. **学習相談**: [学習サポート担当者の連絡先]

## 📋 問題報告テンプレート

問題が解決しない場合は、以下の情報と共に報告してください：

```
## 問題の概要
[何が起こったか簡潔に]

## 環境情報
- OS: [Windows/Mac/Linux]
- Python バージョン: `python --version`
- 作業中のPhase: Phase X

## 再現手順
1. [最初に何をしたか]
2. [次に何をしたか]  
3. [エラーが発生した操作]

## エラーメッセージ
```
[エラーメッセージをそのままコピペ]
```

## 期待する動作
[本来どうなるべきか]

## 試した解決方法
[既に試したことがあれば]
```

このガイドで解決しない問題があれば、上記テンプレートを使って報告してください！