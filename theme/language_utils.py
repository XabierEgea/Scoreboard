from theme.language_manager import language_manager


def set_language_and_update_ui(language_code: str, main_window_ui):
    """Change the language and update the entire UI.
    
    Args:
        language_code (str): Language code (e.g., 'es', 'en')
        main_window_ui: Main window UI object
        
    Returns:
        bool: True if language was changed, False otherwise
    """
    if language_manager.set_language(language_code):
        # Retranslate main window
        main_window_ui.retranslateUi(main_window_ui.__dict__.get('_main_window'))
        return True
    return False


def get_available_languages():
    """Get dictionary of available languages.
    
    Returns:
        dict: Dictionary mapping language codes to language names
    """
    return language_manager.get_available_languages()


def get_current_language():
    """Get the current language code.
    
    Returns:
        str: Current language code
    """
    return language_manager.current_language
