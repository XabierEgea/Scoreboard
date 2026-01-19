import json
from pathlib import Path
from typing import Optional


class LanguageManager:
    """Manager for application languages and translations."""
    
    def __init__(self, default_language: str = "es"):
        """Initialize the language manager.
        
        Args:
            default_language (str): Default language code (e.g., 'es', 'en')
        """
        self.current_language = default_language
        self.translations = {}
        self.available_languages = {}
        self._load_languages()
    
    def _load_languages(self):
        """Load all available language files from the translations directory."""
        translations_dir = Path(__file__).parent.parent / "translations"
        
        for lang_file in translations_dir.glob("*.json"):
            lang_code = lang_file.stem
            try:
                with open(lang_file, 'r', encoding='utf-8') as f:
                    self.translations[lang_code] = json.load(f)
                    self.available_languages[lang_code] = lang_file.stem.upper()
            except Exception as e:
                print(f"Error loading language file {lang_file}: {e}")
    
    def get(self, key: str, default: str = "") -> str:
        """Get a translation using dot notation.
        
        Example: "scoreboard.local" returns the value in the current language
        
        Args:
            key (str): Translation key using dot notation (e.g., 'category.key')
            default (str): Default value if translation is not found
            
        Returns:
            str: Translated text or default value
        """
        keys = key.split(".")
        value = self.translations.get(self.current_language, {})
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        
        return value if value else default
    
    def set_language(self, language_code: str) -> bool:
        """Change the current language.
        
        Args:
            language_code (str): Language code to switch to
            
        Returns:
            bool: True if language was changed successfully, False otherwise
        """
        if language_code in self.translations:
            self.current_language = language_code
            return True
        return False
    
    def get_available_languages(self) -> dict:
        """Get all available languages.
        
        Returns:
            dict: Dictionary mapping language codes to language names
        """
        return self.available_languages
    
    def translate_ui(self, ui_object) -> None:
        """Translate all UI elements using the 'translation_key' attribute.
        
        This allows setting translation keys in Qt Designer
        
        Args:
            ui_object: UI object to translate
        """
        self._translate_widget(ui_object)
    
    def _translate_widget(self, widget) -> None:
        """Recursively translate all widgets that have a translation_key attribute.
        
        Args:
            widget: Widget to translate (and its children)
        """
        if hasattr(widget, 'translation_key'):
            key = widget.translation_key
            translated_text = self.get(key)
            if hasattr(widget, 'setText'):
                widget.setText(translated_text)
            elif hasattr(widget, 'setTitle'):
                widget.setTitle(translated_text)
        
        # Recurse through children
        if hasattr(widget, 'children'):
            for child in widget.children():
                self._translate_widget(child)


# Global instance of the language manager
language_manager = LanguageManager(default_language="es")
