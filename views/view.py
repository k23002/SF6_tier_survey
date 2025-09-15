class View:
    def get_user_name(self):
        return input("robota: 名前を教えてください。\n")
    
    def get_user_character(self, name):
        return input(f"robota: {name}さん、あなたの使用キャラクターを教えてください。\n")
    
    def show_character_error(self):
        return print(f"robota: 不明な入力です。キャラクターリストから選択してください。\n")
    
    def get_answer(self, name, user_char, opponent_char):
        return input(f"robota: {name}さん、{user_char}は{opponent_char}に対してどうですか？\n[有利/互角/不利]\n")
    
    def show_answer_error(self):
        return print(f"robota: 不明な入力です。[有利/互角/不利]から選択してください。\n")
    
    def finish_application(self, name):
        return print(f"robota: {name}さん、ありがとうございました。良い1日を！さようなら。\n")
    
