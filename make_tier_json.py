import json

def create_initial_matchup_data(characters_file, output_file):
    try:
        with open(characters_file, 'r', encoding='utf-8') as file:
            characters = json.load(file)
    except json.JSONDecodeError:
        print(f"エラー: '{characters_file}'が見つかりません。")
        return
    
    matchup_data = {}

    for char1 in characters:
        matchup_data[char1] = {}
        for char2 in characters:
            if char1 != char2:
                matchup_data[char1][char2] = 0

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(matchup_data, file, indent=2, ensure_ascii=False)

        print(f"'{output_file}'を作成しました。")

if __name__ == "__main__":
    create_initial_matchup_data('characters.json', 'SF6_tier_data.json')