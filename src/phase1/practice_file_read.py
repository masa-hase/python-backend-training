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
    # TODO: ここに実装してください
    pass


def main():
    """メイン関数 - 練習用のエントリーポイント"""
    print("=== Practice 1: ファイル読み込み ===")
    
    # サンプルログファイルを読み込み
    read_log_file("data/sample_logs/access.log")
    print()
    read_log_file("data/sample_logs/error.log")


if __name__ == "__main__":
    main()