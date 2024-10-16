import sqlite3
from typing import List, Tuple, Optional

class TranslationMemory:
    def __init__(self, db_name: str):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS translations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    source_text TEXT NOT NULL,
                    target_text TEXT NOT NULL,
                    language_code TEXT NOT NULL,
                    context TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

    def add_translation(self, source_text: str, target_text: str, language_code: str, context: Optional[str] = None):
        with self.connection:
            self.connection.execute('''
                INSERT INTO translations (source_text, target_text, language_code, context)
                VALUES (?, ?, ?, ?)
            ''', (source_text, target_text, language_code, context))

    def get_translation(self, source_text: str, language_code: str) -> Optional[str]:
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT target_text FROM translations
            WHERE source_text = ? AND language_code = ?
        ''', (source_text, language_code))
        result = cursor.fetchone()
        return result[0] if result else None

    def get_all_translations(self, language_code: str) -> List[Tuple[str, str]]:
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT source_text, target_text FROM translations
            WHERE language_code = ?
        ''', (language_code,))
        return cursor.fetchall()

    def update_translation(self, source_text: str, new_target_text: str, language_code: str):
        with self.connection:
            self.connection.execute('''
                UPDATE translations
                SET target_text = ?
                WHERE source_text = ? AND language_code = ?
            ''', (new_target_text, source_text, language_code))

    def delete_translation(self, source_text: str, language_code: str):
        with self.connection:
            self.connection.execute('''
                DELETE FROM translations
                WHERE source_text = ? AND language_code = ?
            ''', (source_text, language_code))

    def close(self):
        self.connection.close()

# Example usage
if __name__ == "__main__":
    tm = TranslationMemory('translation_memory.db')

    # Adding translations
    tm.add_translation('Hello, traveler.', 'Greetings, traveler.', 'zyx', 'Common greeting in Zyloxian culture.')
    tm.add_translation('Goodbye, friend.', 'K\'tkt tk\'tk.', 'xhk', 'Farewell in Xhk\'kht language.')

    # Retrieving a translation
    translation = tm.get_translation('Hello, traveler.', 'zyx')
    print(f'Translation: {translation}')

    # Updating a translation
    tm.update_translation('Goodbye, friend.', 'K\'tkt tk\'tk!', 'xhk')

    # Retrieving all translations for a language
    translations = tm.get_all_translations('zyx')
    print('All Zyloxian Translations:')
    for source, target in translations:
        print(f'{source} -> {target}')

    # Deleting a translation
    tm.delete_translation('Goodbye, friend.', 'xhk')

    # Closing the database connection
    tm.close()
