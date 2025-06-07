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
    try:
        line = line.strip()
        if not line:
            return None
            
        parts = line.split()
        if len(parts) < 6:
            return None
            
        # 基本形式: "2024-01-15 09:23:45 INFO GET /api/users 200 45ms"
        date = parts[0]
        time = parts[1]
        level = parts[2]
        method = parts[3]
        endpoint = parts[4]
        status_code = parts[5]
        response_time = parts[6] if len(parts) > 6 else "0ms"
        
        # メッセージ部分（エラーメッセージなど）
        message = " ".join(parts[7:]) if len(parts) > 7 else ""
        
        return {
            "date": date,
            "time": time,
            "datetime": f"{date} {time}",
            "level": level,
            "method": method,
            "endpoint": endpoint,
            "status_code": status_code,
            "response_time": response_time,
            "message": message,
            "full_line": line
        }
        
    except (IndexError, ValueError):
        return None


def parse_error_log_line(line: str) -> Optional[Dict[str, str]]:
    """
    エラーログ専用の解析関数
    形式: "2024-01-15 09:23:45 [ERROR] UserService: Failed to validate user credentials"
    
    Args:
        line: エラーログの1行
    
    Returns:
        解析したログデータの辞書、または解析に失敗した場合はNone
    """
    try:
        line = line.strip()
        if not line:
            return None
            
        # [ERROR]の位置を探す
        if "[ERROR]" not in line:
            return None
            
        # 日時部分とメッセージ部分を分離
        parts = line.split("[ERROR]", 1)
        if len(parts) != 2:
            return None
            
        datetime_part = parts[0].strip()
        message_part = parts[1].strip()
        
        # 日時を分離
        datetime_parts = datetime_part.split()
        if len(datetime_parts) < 2:
            return None
            
        date = datetime_parts[0]
        time = datetime_parts[1]
        
        # サービス名とエラーメッセージを分離
        if ":" in message_part:
            service_and_message = message_part.split(":", 1)
            service = service_and_message[0].strip()
            error_message = service_and_message[1].strip()
        else:
            service = "Unknown"
            error_message = message_part
        
        return {
            "date": date,
            "time": time,
            "datetime": f"{date} {time}",
            "level": "ERROR",
            "service": service,
            "message": error_message,
            "full_line": line
        }
        
    except (IndexError, ValueError):
        return None


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