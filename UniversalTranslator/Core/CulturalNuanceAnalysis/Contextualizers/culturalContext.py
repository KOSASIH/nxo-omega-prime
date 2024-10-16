import json
from typing import Dict, List, Any

class CulturalContext:
    def __init__(self):
        self.context_data = self.load_context_data()

    def load_context_data(self) -> Dict[str, Any]:
        """Load cultural context data from a JSON file."""
        try:
            with open('cultural_context.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Cultural context data file not found.")
            return {}

    def get_cultural_reference(self, species: str, term: str) -> str:
        """Retrieve cultural references for a specific term in a given species' context."""
        species_data = self.context_data.get(species, {})
        return species_data.get(term, "No cultural reference found.")

    def add_cultural_reference(self, species: str, term: str, reference: str) -> None:
        """Add a new cultural reference for a specific term."""
        if species not in self.context_data:
            self.context_data[species] = {}
        self.context_data[species][term] = reference
        self.save_context_data()

    def save_context_data(self) -> None:
        """Save the updated cultural context data back to the JSON file."""
        with open('cultural_context.json', 'w') as file:
            json.dump(self.context_data, file, indent=4)

    def translate_with_context(self, species: str, term: str) -> str:
        """Translate a term while considering cultural context."""
        translation = self.get_translation(term)  # Assume this method exists
        cultural_reference = self.get_cultural_reference(species, term)
        
        if cultural_reference != "No cultural reference found.":
            return f"{translation} (Cultural context: {cultural_reference})"
        return translation

    def get_translation(self, term: str) -> str:
        """Placeholder for the actual translation logic."""
        # This method should interface with the translation algorithms
        return f"Translated '{term}'"

# Example usage
if __name__ == "__main__":
    cultural_context = CulturalContext()
    cultural_context.add_cultural_reference("Zyloxians", "greeting", "A warm embrace with three arms.")
    print(cultural_context.translate_with_context("Zyloxians", "greeting"))
