"""
Practice 1: ファイル読み込みの練習

このファイルは Phase 1 の最初の練習用です。
ログファイルを読み込んで基本的な情報を表示する練習をします。

【課題1】
read_log_file関数を実装してください。
- ファイルを読み込んで行数を表示
- 最初の5行を表示  
- エラーハンドリングを含める
"""


def read_log_file(file_path: str) -> None:
    """
    ログファイルを読み込んで行数を数える
    
    Args:
        file_path: 読み込むファイルのパス
    """
    try:
        print(f"ファイルを読み込み中: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        print(f"総行数: {len(lines)}行")
        print("最初の5行:")
        print("-" * 50)
        
        for i, line in enumerate(lines[:5], 1):
            print(f"{i:2d}: {line.rstrip()}")
            
        print("-" * 50)
        
    except FileNotFoundError:
        print(f"エラー: ファイル '{file_path}' が見つかりません")
    except PermissionError:
        print(f"エラー: ファイル '{file_path}' の読み込み権限がありません")
    except UnicodeDecodeError:
        print(f"エラー: ファイル '{file_path}' の文字コードが正しくありません")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")


def main():
    """メイン関数 - 練習用のエントリーポイント"""
    print("=== Practice 1: ファイル読み込み ===")
    
    # サンプルログファイルを読み込み
    read_log_file("data/sample_logs/access.log")
    print()
    read_log_file("data/sample_logs/error.log")


if __name__ == "__main__":
    main()