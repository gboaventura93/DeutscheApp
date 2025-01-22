import pandas as pd
import random

file_path = r"C:\Users\Startklar\Documents\GitHub\DeutscheApp\wortschatz.csv"


vocabulary_df = pd.read_csv(file_path, encoding='iso-8859-1', sep=",")

vocabulary_df.replace({"Ã¼": "ü", "Ã¤": "ä", "Ã¶": "ö", "ÃŸ": "ß"}, regex=True, inplace=True)
vocabulary_df.columns = vocabulary_df.columns.str.strip()


def start_quiz(vocab_df):
    print("Willkommen zum Wortschatz-Quiz!")
    print("Drücken Sie 5, um das Quiz jederzeit zu beenden.\n")
    while True:
        # Randomly select a row
        random_row = vocab_df.sample(n=1).iloc[0]
        word = random_row["Deutsch Wort"]  # Matches the "Deutsch Wort" column
        correct_article = random_row["Artikel"]  # Matches the "Artikel" column

        # Fixed options order
        options = ["das", "der", "die"]

        # Display the question
        print(f"\nWas ist der richtige Artikel für das Wort: {word}?")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        print("5. Beenden")

        # Get the user's answer
        try:
            user_choice = int(input("Wählen Sie die richtige Option (1, 2, 3 oder 5): "))
            if user_choice == 5:
                print("Vielen Dank fürs Spielen! Auf Wiedersehen!")
                break
            user_answer = options[user_choice - 1]
        except (ValueError, IndexError):
            print("Ungültige Eingabe. Bitte wählen Sie eine gültige Option.")
            continue

        # Check the answer
        if user_answer == correct_article:
            print(f"✅ Richtig! Der Artikel für '{word}' ist '{correct_article}'.")
        else:
            print(f"❌ Falsch! Der richtige Artikel für '{word}' ist '{correct_article}'.")

# Start the quiz with the loaded vocabulary data
start_quiz(vocabulary_df)
