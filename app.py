import pandas as pd
import random

#file_path = r"C:\Users\Startklar\Documents\GitHub\DeutscheApp\wortschatz.csv"

# File paths for different levels
file_path_beginner = r"C:\Users\Startklar\Documents\GitHub\DeutscheApp\wortschatz_Beginner.csv"
file_path_intermediate = r"C:\Users\Startklar\Documents\GitHub\DeutscheApp\wortschatz_Intermediate.csv"
file_path_advanced = r"C:\Users\Startklar\Documents\GitHub\DeutscheApp\wortschatz_Advanced.csv"

# Function to load the vocabulary file based on level
def load_vocabulary(level):
    try:
        if level == "Beginner":
            vocab_df = pd.read_csv(file_path_beginner, encoding='iso-8859-1', sep=",")
        elif level == "Intermediate":
            vocab_df = pd.read_csv(file_path_intermediate, encoding='iso-8859-1', sep=",")
        elif level == "Advanced":
            vocab_df = pd.read_csv(file_path_advanced, encoding='iso-8859-1', sep=",")
        else:
            return None

        # Replace incorrect characters
        vocab_df.replace({"Ã¼": "ü", "Ã¤": "ä", "Ã¶": "ö", "ÃŸ": "ß"}, regex=True, inplace=True)
        vocab_df.columns = vocab_df.columns.str.strip()
        return vocab_df
    except Exception as e:
        print(f"Fehler beim Laden der Datei: {e}")
        return None

# Function to start the quiz
def start_quiz(vocab_df):
    print("\nWillkommen zum Wortschatz-Quiz!")
    print("Drücken Sie 5, um das Quiz jederzeit zu beenden.")
    print("Drücken Sie 4, um das Level zu ändern.\n")

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
        print("4. Level ändern")
        print("5. Beenden")

        # Get the user's answer
        try:
            user_choice = int(input("Wählen Sie die richtige Option (1, 2, 3, 4 oder 5): "))
            if user_choice == 5:
                print("Vielen Dank fürs Spielen! Auf Wiedersehen!")
                return "quit"  # Exit the quiz
            elif user_choice == 4:
                print("Level wechseln.\n")
                return "change_level"  # Return to level selection
            user_answer = options[user_choice - 1]
        except (ValueError, IndexError):
            print("Ungültige Eingabe. Bitte wählen Sie eine gültige Option.")
            continue

        # Check the answer
        if user_answer == correct_article:
            print(f"✅ Richtig! Der Artikel für '{word}' ist '{correct_article}'.")
        else:
            print(f"❌ Falsch! Der richtige Artikel für '{word}' ist '{correct_article}'.")

# Main function to handle level selection
def main():
    while True:
        print("\nWählen Sie ein Level:")
        print("1. Anfänger (Beginner)")
        print("2. Mittelstufe (Intermediate)")
        print("3. Fortgeschritten (Advanced)")
        print("4. Beenden")

        try:
            level_choice = int(input("Wählen Sie eine Option (1, 2, 3 oder 4): "))
            if level_choice == 4:
                print("Vielen Dank fürs Spielen! Auf Wiedersehen!")
                break

            if level_choice == 1:
                level = "Beginner"
            elif level_choice == 2:
                level = "Intermediate"
            elif level_choice == 3:
                level = "Advanced"
            else:
                print("Ungültige Eingabe. Bitte wählen Sie eine gültige Option.")
                continue

            # Load the vocabulary file for the selected level
            vocab_df = load_vocabulary(level)
            if vocab_df is None or vocab_df.empty:
                print(f"Es gibt keine Wörter für das Level '{level}'.")
                continue

            # Start the quiz for the selected level
            while True:
                result = start_quiz(vocab_df)
                if result == "quit":
                    print("Das Spiel wird beendet.")
                    return
                elif result == "change_level":
                    break  # Return to level selection
        except ValueError:
            print("Ungültige Eingabe. Bitte wählen Sie eine gültige Option.")

# Run the main function
main()