"""
メインのログ解析ツール

このファイルは Phase 1 のメイン成果物です。
ログファイルを読み込み、解析、フィルタリング、集計を行うツールです。

【課題3】
以下のクラスとメソッドを順番に実装してください：
1. LogAnalyzer クラスの各メソッド
2. コマンドライン機能
"""

import os
import csv
import logging
from datetime import datetime
from typing import List, Dict, Optional
import click


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


class LogAnalyzer:
    """ログファイルを解析するクラス"""
    
    def __init__(self):
        """初期化"""
        self.log_data: List[Dict] = []
        logger.info("LogAnalyzer が初期化されました")
    
    def read_log_file(self, file_path: str) -> bool:
        """
        ログファイルを読み込む
        
        Args:
            file_path: 読み込むログファイルのパス
            
        Returns:
            読み込み成功時はTrue、失敗時はFalse
        """
        try:
            logger.info(f"ログファイルを読み込み中: {file_path}")
            
            if not os.path.exists(file_path):
                logger.error(f"ファイルが見つかりません: {file_path}")
                return False
                
            self.log_data.clear()
            
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    parsed_data = self.parse_line(line)
                    if parsed_data:
                        parsed_data['line_number'] = line_num
                        self.log_data.append(parsed_data)
                    else:
                        logger.warning(f"行 {line_num} の解析に失敗: {line.strip()}")
            
            logger.info(f"読み込み完了: {len(self.log_data)}件のログを解析")
            return True
            
        except FileNotFoundError:
            logger.error(f"ファイルが見つかりません: {file_path}")
            return False
        except PermissionError:
            logger.error(f"ファイルの読み込み権限がありません: {file_path}")
            return False
        except Exception as e:
            logger.error(f"ファイル読み込み中にエラーが発生: {e}")
            return False
    
    def parse_line(self, line: str) -> Optional[Dict]:
        """
        ログ行を解析する
        
        Args:
            line: ログの1行
            
        Returns:
            解析したログデータの辞書、または解析に失敗した場合はNone
        """
        try:
            line = line.strip()
            if not line:
                return None
                
            # エラーログ形式をチェック
            if "[ERROR]" in line:
                return self._parse_error_log(line)
            else:
                return self._parse_access_log(line)
                
        except Exception as e:
            logger.warning(f"ログ行の解析に失敗: {e}")
            return None
    
    def _parse_access_log(self, line: str) -> Optional[Dict]:
        """アクセスログを解析"""
        parts = line.split()
        if len(parts) < 6:
            return None
            
        return {
            "date": parts[0],
            "time": parts[1],
            "datetime": f"{parts[0]} {parts[1]}",
            "level": parts[2],
            "method": parts[3],
            "endpoint": parts[4],
            "status_code": parts[5],
            "response_time": parts[6] if len(parts) > 6 else "0ms",
            "message": " ".join(parts[7:]) if len(parts) > 7 else "",
            "full_line": line,
            "log_type": "access"
        }
    
    def _parse_error_log(self, line: str) -> Optional[Dict]:
        """エラーログを解析"""
        parts = line.split("[ERROR]", 1)
        if len(parts) != 2:
            return None
            
        datetime_part = parts[0].strip()
        message_part = parts[1].strip()
        
        datetime_parts = datetime_part.split()
        if len(datetime_parts) < 2:
            return None
            
        # サービス名とメッセージを分離
        if ":" in message_part:
            service_parts = message_part.split(":", 1)
            service = service_parts[0].strip()
            error_message = service_parts[1].strip()
        else:
            service = "Unknown"
            error_message = message_part
            
        return {
            "date": datetime_parts[0],
            "time": datetime_parts[1],
            "datetime": f"{datetime_parts[0]} {datetime_parts[1]}",
            "level": "ERROR",
            "service": service,
            "message": error_message,
            "full_line": line,
            "log_type": "error"
        }
    
    def filter_by_level(self, level: str) -> List[Dict]:
        """
        ログレベルでフィルタリング
        
        Args:
            level: フィルタするログレベル（INFO, WARNING, ERROR等）
            
        Returns:
            フィルタされたログデータのリスト
        """
        level = level.upper()
        filtered_logs = [log for log in self.log_data if log.get('level', '').upper() == level]
        logger.info(f"レベル '{level}' でフィルタ: {len(filtered_logs)}件見つかりました")
        return filtered_logs
    
    def search_keyword(self, keyword: str) -> List[Dict]:
        """
        キーワードで検索
        
        Args:
            keyword: 検索するキーワード
            
        Returns:
            キーワードを含むログデータのリスト
        """
        keyword_lower = keyword.lower()
        matching_logs = []
        
        for log in self.log_data:
            # 全体のログ行で検索
            if keyword_lower in log.get('full_line', '').lower():
                matching_logs.append(log)
                continue
            # メッセージで検索
            if keyword_lower in log.get('message', '').lower():
                matching_logs.append(log)
                continue
            # エンドポイントで検索
            if keyword_lower in log.get('endpoint', '').lower():
                matching_logs.append(log)
                continue
        
        logger.info(f"キーワード '{keyword}' で検索: {len(matching_logs)}件見つかりました")
        return matching_logs
    
    def count_by_level(self) -> Dict[str, int]:
        """
        ログレベル別の件数を集計
        
        Returns:
            ログレベルをキー、件数を値とする辞書
        """
        level_counts = {}
        
        for log in self.log_data:
            level = log.get('level', 'UNKNOWN')
            level_counts[level] = level_counts.get(level, 0) + 1
        
        return level_counts
    
    def export_to_csv(self, results: List[Dict], output_path: str) -> bool:
        """
        結果をCSVファイルに出力
        
        Args:
            results: 出力するログデータのリスト
            output_path: 出力先CSVファイルのパス
            
        Returns:
            出力成功時はTrue、失敗時はFalse
        """
        try:
            if not results:
                logger.warning("出力するデータがありません")
                return False
            
            # CSVフィールド名を決定（最初のレコードから）
            fieldnames = list(results[0].keys())
            
            with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(results)
            
            logger.info(f"CSVファイルを出力しました: {output_path} ({len(results)}件)")
            return True
            
        except Exception as e:
            logger.error(f"CSV出力中にエラーが発生: {e}")
            return False
    
    def display_summary(self):
        """ログ解析の結果サマリーを表示"""
        if not self.log_data:
            print("ログデータがありません")
            return
        
        print("\n" + "=" * 50)
        print("ログ解析サマリー")
        print("=" * 50)
        
        # 総件数
        print(f"総ログ件数: {len(self.log_data)}件")
        
        # レベル別集計
        level_counts = self.count_by_level()
        print("\nログレベル別集計:")
        for level, count in sorted(level_counts.items()):
            print(f"  {level}: {count}件")
        
        # ステータスコード別集計（アクセスログのみ）
        status_counts = {}
        for log in self.log_data:
            if log.get('log_type') == 'access' and 'status_code' in log:
                status = log['status_code']
                status_counts[status] = status_counts.get(status, 0) + 1
        
        if status_counts:
            print("\nステータスコード別集計:")
            for status, count in sorted(status_counts.items()):
                print(f"  {status}: {count}件")
        
        # エラーサービス別集計
        service_counts = {}
        for log in self.log_data:
            if log.get('log_type') == 'error' and 'service' in log:
                service = log['service']
                service_counts[service] = service_counts.get(service, 0) + 1
        
        if service_counts:
            print("\nエラーサービス別集計:")
            for service, count in sorted(service_counts.items(), key=lambda x: x[1], reverse=True):
                print(f"  {service}: {count}件")
        
        print("=" * 50)


@click.command()
@click.argument('log_file', type=click.Path(exists=True))
@click.option('--level', help='フィルタするログレベル (INFO/WARNING/ERROR)')
@click.option('--keyword', help='検索するキーワード')
@click.option('--output', help='結果を保存するCSVファイル名')
@click.option('--summary', is_flag=True, help='サマリー情報を表示')
def analyze_log(log_file, level, keyword, output, summary):
    """
    ログファイルを解析するコマンドラインツール
    
    使用例:
        python log_analyzer.py data/sample_logs/access.log
        python log_analyzer.py data/sample_logs/access.log --level ERROR
        python log_analyzer.py data/sample_logs/access.log --keyword "Database"
        python log_analyzer.py data/sample_logs/access.log --output results.csv
    """
    analyzer = LogAnalyzer()
    
    # ログファイルを読み込み
    if not analyzer.read_log_file(log_file):
        click.echo(f"エラー: ログファイル '{log_file}' の読み込みに失敗しました", err=True)
        return
    
    results = analyzer.log_data
    
    # フィルタリング
    if level:
        results = analyzer.filter_by_level(level)
        if not results:
            click.echo(f"ログレベル '{level}' のログが見つかりませんでした")
            return
    
    if keyword:
        results = analyzer.search_keyword(keyword)
        if not results:
            click.echo(f"キーワード '{keyword}' を含むログが見つかりませんでした")
            return
    
    # 結果表示
    if summary:
        analyzer.display_summary()
    else:
        print(f"\n検索結果: {len(results)}件")
        print("-" * 50)
        for i, log in enumerate(results[:10], 1):  # 最初の10件のみ表示
            print(f"{i:2d}. [{log.get('level', 'N/A')}] {log.get('datetime', 'N/A')} - {log.get('full_line', 'N/A')[:100]}")
        
        if len(results) > 10:
            print(f"... その他 {len(results) - 10} 件")
    
    # CSV出力
    if output:
        if analyzer.export_to_csv(results, output):
            click.echo(f"結果をCSVファイルに保存しました: {output}")
        else:
            click.echo("CSV出力に失敗しました", err=True)


def main():
    """メイン関数（スタンドアロン実行用）"""
    print("ログ解析ツール - スタンドアロン実行")
    print("実際の使用は以下のコマンドで行ってください:")
    print("python log_analyzer.py [ログファイルパス] [オプション]")
    print()
    
    # デモ実行
    analyzer = LogAnalyzer()
    
    # サンプルファイルで動作確認
    if analyzer.read_log_file("data/sample_logs/access.log"):
        print("サンプルファイルの読み込み成功")
        analyzer.display_summary()
    else:
        print("サンプルファイルが見つかりません")


if __name__ == "__main__":
    # コマンドライン引数がある場合はClickコマンドを実行
    # ない場合はデモ実行
    import sys
    if len(sys.argv) > 1:
        analyze_log()
    else:
        main()