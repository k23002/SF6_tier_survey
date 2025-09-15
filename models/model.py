import json
import os

class Model:
    def __init__(self, filename="SF6_tier_data.json", char_filename="characters.json"):
        self.filename = filename
        self.char_filename = char_filename
        self.data = self._load_data()

    def _load_data(self):
        """
        jsonファイルを読み込んで、データを辞書としてロードする。
        """
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}
        else:
            print("ファイルが見つかりませんでした。")
        return {}
    
    def _save_data(self):
        """
        データをjsonファイルに保存する
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=2, ensure_ascii=False)

    def record_matchup(self, user_char, opponent_char, result_point):
        """
        有利不利のポイントを更新する
        """
        self.data[user_char][opponent_char] += result_point
        self.data[opponent_char][user_char] -= result_point

        self._save_data()

    def update(self, restaurant_name):
        """
        お店の名前の追加やおすすめ回数を更新する
        """
        if restaurant_name in self.data:
            self.data[restaurant_name] += 1
        else:
            self.data[restaurant_name] = 1
        self._save_data()

    def most_recomended(self):
        """
        最もお勧めされたレストランの名前を取得する。
        """
        if not self.data:
            return None
        return max(self.data, key=self.data.get)
    
    def get_all_characters(self):
        """
        キャラクターリストをファイルから読み込んで返す
        """
        if os.path.exists(self.char_filename):
            with open(self.char_filename, 'r', encoding='utf-8') as file:
                return json.load(file)
            
        return []