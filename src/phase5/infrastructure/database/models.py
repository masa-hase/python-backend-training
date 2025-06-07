"""
SQLAlchemyモデル定義

【課題11】データベースモデルをTDDで実装してください

※注意: これらはインフラ層のデータモデルであり、ドメインエンティティとは分離します
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class UserModel(Base):
    """ユーザーテーブルモデル（インフラ層）"""
    __tablename__ = "users"
    
    # TODO: TDDで実装してください
    # - id: プライマリキー
    # - user_name: ユーザー名（ユニーク）
    # - email: メールアドレス（ユニーク）
    # - hashed_password: ハッシュ化されたパスワード
    # - is_active: アクティブフラグ
    # - created_at: 作成日時
    # - updated_at: 更新日時
    # - last_login_at: 最終ログイン日時
    pass
    
    def to_domain_entity(self):
        """ドメインエンティティに変換"""
        # TODO: TDDで実装してください
        # - UserModelからUserエンティティを作成
        # - バリューオブジェクトの復元
        pass
    
    @classmethod
    def from_domain_entity(cls, user_entity):
        """ドメインエンティティから作成"""
        # TODO: TDDで実装してください
        # - UserエンティティからUserModelを作成
        # - バリューオブジェクトの値を抽出
        pass


class LogFileModel(Base):
    """ログファイルテーブルモデル（インフラ層）"""
    __tablename__ = "log_files"
    
    # TODO: TDDで実装してください
    # - id: プライマリキー
    # - file_name: ファイル名
    # - file_size: ファイルサイズ
    # - uploaded_by: アップロードユーザーID（外部キー）
    # - uploaded_at: アップロード日時
    # - file_path: ファイル保存パス
    pass
    
    def to_domain_entity(self):
        """ドメインエンティティに変換"""
        # TODO: TDDで実装してください
        pass
    
    @classmethod
    def from_domain_entity(cls, log_file_entity):
        """ドメインエンティティから作成"""
        # TODO: TDDで実装してください
        pass


class LogEntryModel(Base):
    """ログエントリテーブルモデル（インフラ層）"""
    __tablename__ = "log_entries"
    
    # TODO: TDDで実装してください
    # - id: プライマリキー
    # - log_file_id: ログファイルID（外部キー）
    # - timestamp: ログ時刻
    # - level: ログレベル
    # - message: ログメッセージ
    # - source_ip: 送信元IP
    # - response_time: レスポンス時間
    pass