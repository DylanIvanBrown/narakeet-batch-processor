# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import csv
import requests

def process_csv_and_generate_voice(api_key, csv_file_path):
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")
        for row in csv_reader:
            game_id = row['game_id']
            text = row['text']
            character = row['character']
            use_narakeet_sample(api_key, game_id, text, character)

def save_voice_file(api_key, game_id, text, character):
    url = "https://api.narakeet.com/text-to-speech/mp3"

    headers = {
        "x-api-key": api_key
    }

    data = {
        "text": text,
        "voice": character
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        with open(f"{game_id}.mp3", "wb") as f:
            f.write(response.content)
            print(f"Voice file saved for game_id: {game_id}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

# def select_csv_file():
#     root = tk.Tk()
#     root.withdraw()
#     file_path = filedialog.askopenfilename()
#     return file_path

def use_narakeet_sample(apikey,game_id,text,voice):
    text = text
    url = f'https://api.narakeet.com/text-to-speech/mp3?voice={voice}'

    import requests

    options = {
        'headers': {
            'Accept': 'application/octet-stream',
            'Content-Type': 'text/plain',
            'x-api-key': apikey,
        },
        'data': text.encode('utf8')
    }

    with open(f'{game_id}.mp3', 'wb') as f:
        f.write(requests.post(url, **options).content)

if __name__ == '__main__':
    api_key = input("Please provide your API Key")
    print("Please select a CSV file with 'game_id, text, character' data.")
    csv_file_name = input("Please provide the file name in this directory for me to use for text to speech /n")
    #csv_file_path = select_csv_file()
    print(f"Processing {csv_file_name}.csv")
    process_csv_and_generate_voice(api_key, f"{csv_file_name}.csv")
    input("All done! Check your directory for the output files.")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
