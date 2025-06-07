"""
Practice 2: 文字列操作・ログ解析の練習

このファイルは Phase 1 の文字列操作練習用です。
ログ行を解析して各要素を抽出する練習をします。

【課題2】
以下の関数を実装してください：
1. parse_log_line: アクセスログの解析
2. parse_error_log_line: エラーログの解析
"""

from typing import Dict, Optional


def parse_log_line(line: str) -> Optional[Dict[str, str]]:
    """
    ログ行を解析して各要素を抽出する
    
    Args:
        line: ログの1行（例: "2024-01-15 09:23:45 INFO GET /api/users 200 45ms"）
    
    Returns:
        解析したログデータの辞書、または解析に失敗した場合はNone
    """
    # TODO: ここに実装してください
    pass


def parse_error_log_line(line: str) -> Optional[Dict[str, str]]:
    """
    エラーログ専用の解析関数
    形式: "2024-01-15 09:23:45 [ERROR] UserService: Failed to validate user credentials"
    
    Args:
        line: エラーログの1行
    
    Returns:
        解析したログデータの辞書、または解析に失敗した場合はNone
    """
    # TODO: ここに実装してください
    pass


def analyze_sample_logs():
    """サンプルログを解析してみる"""
    print("=== アクセスログの解析例 ===")
    access_log_samples = [
        "2024-01-15 09:23:45 INFO GET /api/users 200 45ms",
        "2024-01-15 09:24:33 ERROR GET /api/data 500 234ms Database connection failed",
        "2024-01-15 09:25:15 WARNING GET /api/reports 404 12ms Resource not found",
    ]
    
    for line in access_log_samples:
        data = parse_log_line(line)
        if data:
            print(f"元の行: {line}")
            print(f"解析結果: {data}")
            print("-" * 50)
    
    print("\n=== エラーログの解析例 ===")
    error_log_samples = [
        "2024-01-15 09:23:45 [ERROR] UserService: Failed to validate user credentials",
        "2024-01-15 09:24:33 [ERROR] DatabaseService: Connection timeout after 30 seconds",
        "2024-01-15 10:15:22 [ERROR] AuthService: Invalid JWT token provided",
    ]
    
    for line in error_log_samples:
        data = parse_error_log_line(line)
        if data:
            print(f"元の行: {line}")
            print(f"解析結果: {data}")
            print("-" * 50)


def practice_file_parsing():
    """実際のログファイルを解析してみる"""
    print("\n=== 実際のファイルの解析 ===")
    
    try:
        with open("data/sample_logs/access.log", 'r', encoding='utf-8') as file:
            print("access.log の最初の3行を解析:")
            for i, line in enumerate(file):
                if i >= 3:  # 最初の3行のみ
                    break
                data = parse_log_line(line)
                if data:
                    print(f"行 {i+1}: {data}")
    except FileNotFoundError:
        print("access.log ファイルが見つかりません")
    
    try:
        with open("data/sample_logs/error.log", 'r', encoding='utf-8') as file:
            print("\nerror.log の最初の3行を解析:")
            for i, line in enumerate(file):
                if i >= 3:  # 最初の3行のみ
                    break
                data = parse_error_log_line(line)
                if data:
                    print(f"行 {i+1}: {data}")
    except FileNotFoundError:
        print("error.log ファイルが見つかりません")


def main():
    """メイン関数 - 練習用のエントリーポイント"""
    print("=== Practice 2: 文字列操作・ログ解析 ===")
    
    # サンプルデータでの練習
    analyze_sample_logs()
    
    # 実際のファイルでの練習
    practice_file_parsing()


if __name__ == "__main__":
    main()