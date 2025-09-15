import random

class Controllers:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.characters = self.model.get_all_characters()
    
    def start_application(self):
        user_name = self.view.get_user_name()

        if user_name == "tier":
            while True:
                character = self.view.get_character_name(self.characters)
                if character in self.characters:
                    tier = self.model.get_all_tier()
                    for char, point in tier[character].items():
                        if point > 0:
                            matchup = "有利"
                        elif point < 0:
                            matchup = "不利"
                        else:
                            matchup = "互角"
                        print(char, point, matchup)
                    break
                else:
                    self.view.show_character_error()
            return

        while True:
            user_character = self.view.get_user_character(user_name, self.characters)
            if user_character in self.characters:
                break
            else:
                self.view.show_character_error()

        opponent_character = random.choice([c for c in self.characters if c != user_character])

        while True:
            answer = self.view.get_answer(user_name, user_character, opponent_character)
            if answer == "有利":
                result_point = 1
                break
            elif answer == "互角":
                result_point = 0
                break
            elif answer == "不利":
                result_point = -1
                break
            else:
                self.view.show_answer_error()
        
        self.model.record_matchup(user_character, opponent_character, result_point)

        self.view.finish_application(user_name)