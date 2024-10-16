import json
from typing import Dict, List, Any

class GalacticGrammar:
    def __init__(self):
        self.grammar_rules = self.load_grammar_rules()

    def load_grammar_rules(self) -> Dict[str, Any]:
        """Load grammar rules from a JSON file."""
        try:
            with open('grammar_rules.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Grammar rules file not found.")
            return {}

    def get_grammar_rules(self, species: str) -> Dict[str, Any]:
        """Retrieve grammar rules for a specific species."""
        return self.grammar_rules.get(species, {})

    def add_grammar_rule(self, species: str, rule_name: str, rule: Dict[str, Any]) -> None:
        """Add a new grammar rule for a specific species."""
        if species not in self.grammar_rules:
            self.grammar_rules[species] = {}
        self.grammar_rules[species][rule_name] = rule
        self.save_grammar_rules()

    def save_grammar_rules(self) -> None:
        """Save the updated grammar rules back to the JSON file."""
        with open('grammar_rules.json', 'w') as file:
            json.dump(self.grammar_rules, file, indent=4)

    def apply_grammar_rules(self, species: str, sentence: str) -> str:
        """Apply grammar rules to a given sentence based on the species."""
        rules = self.get_grammar_rules(species)
        for rule_name, rule in rules.items():
            if rule['type'] == 'reorder':
                sentence = self.reorder_sentence(sentence, rule['pattern'])
            elif rule['type'] == 'modify':
                sentence = self.modify_sentence(sentence, rule['modification'])
        return sentence

    def reorder_sentence(self, sentence: str, pattern: List[str]) -> str:
        """Reorder the words in a sentence based on a specified pattern."""
        words = sentence.split()
        reordered = [words[i] for i in pattern if i < len(words)]
        return ' '.join(reordered)

    def modify_sentence(self, sentence: str, modification: Dict[str, str]) -> str:
        """Modify a sentence based on specified modifications."""
        for target, replacement in modification.items():
            sentence = sentence.replace(target, replacement)
        return sentence

    def translate_with_grammar(self, species: str, sentence: str) -> str:
        """Translate a sentence while applying the appropriate grammar rules."""
        translation = self.get_translation(sentence)  # Assume this method exists
        grammar_applied = self.apply_grammar_rules(species, translation)
        return grammar_applied

    def get_translation(self, sentence: str) -> str:
        """Placeholder for the actual translation logic."""
        # This method should interface with the translation algorithms
        return f"Translated '{sentence}'"

# Example usage
if __name__ == "__main__":
    galactic_grammar = GalacticGrammar()
    galactic_grammar.add_grammar_rule("Zyloxians", "sentence_structure", {
        "type": "reorder",
        "pattern": [1, 0]  # Example pattern to reorder words
    })
    print(galactic_grammar.translate_with_grammar("Zyloxians", "hello world"))
