import json
from pathlib import Path


class FileWriter:
    """Manages scoreboard state persistence.
    
    This class handles reading and writing the scoreboard state to a JSON file.
    The state is read by the HTML overlay to update OBS in real-time.
    """
    
    def __init__(self, info_path):
        """Initialize FileWriter with root path.
        
        Args:
            info_path (str): Root path where scoreboard_state.json is located
        """
        self._rootpath = Path(info_path)
        self._state_file = self._rootpath / "scoreboard_state.json"
        self._state = self._load_state()
    
    def _load_state(self) -> dict:
        """Load state from JSON file.
        
        Returns:
            dict: Current scoreboard state
        """
        try:
            if self._state_file.exists():
                with open(self._state_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading state: {e}")
        
        # Default state if file doesn't exist or is corrupted
        return {
            "local": {"name": "LOCAL", "color": "#E53935", "sets": [0, 0, 0]},
            "visitor": {"name": "VISITOR", "color": "#1E88E5", "sets": [0, 0, 0]},
            "style": "modern"
        }
    
    def _save_state(self) -> None:
        """Save current state to JSON file."""
        try:
            self._state_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self._state_file, 'w', encoding='utf-8') as f:
                json.dump(self._state, f, indent=2)
        except Exception as e:
            print(f"Error saving state: {e}")
    
    def change_set(self, set_number: int) -> None:
        """Change the current set number.
        
        Args:
            set_number (int): Set number (1-3)
        """
        # This method is now managed by the set score methods
        # Sets are now part of the sets array
        pass
    
    def set_local_set_score(self, set_number: int, points: int) -> None:
        """Update local team score for a specific set.
        
        Args:
            set_number (int): Set number (1-3, 0-indexed to 0-2 in array)
            points (int): New points value
        """
        if 1 <= set_number <= 3:
            self._state["local"]["sets"][set_number - 1] = points
            self._save_state()
    
    def set_visitor_set_score(self, set_number: int, points: int) -> None:
        """Update visitor team score for a specific set.
        
        Args:
            set_number (int): Set number (1-3, 0-indexed to 0-2 in array)
            points (int): New points value
        """
        if 1 <= set_number <= 3:
            self._state["visitor"]["sets"][set_number - 1] = points
            self._save_state()
    
    def set_local_value(self, set_number: int, points: int) -> None:
        """Update local team points (deprecated - use set_local_set_score).
        
        Args:
            set_number (int): Set number (1-3)
            points (int): New points value
        """
        # Backwards compatibility: sets the first set
        self.set_local_set_score(set_number, points)
    
    def set_visiting_value(self, set_number: int, points: int) -> None:
        """Update visitor team points (deprecated - use set_visitor_set_score).
        
        Args:
            set_number (int): Set number (1-3)
            points (int): New points value
        """
        # Backwards compatibility: sets the first set
        self.set_visitor_set_score(set_number, points)
    
    def set_local_color(self, color: str) -> None:
        """Update local team color.
        
        Args:
            color (str): Hex color code
        """
        self._state["local"]["color"] = color
        self._save_state()
    
    def set_visitor_color(self, color: str) -> None:
        """Update visitor team color.
        
        Args:
            color (str): Hex color code
        """
        self._state["visitor"]["color"] = color
        self._save_state()
    
    def set_style(self, style: str) -> None:
        """Update overlay style.
        
        Args:
            style (str): Style name ('modern' or 'classic')
        """
        self._state["style"] = style
        self._save_state()
    
    def get_state(self) -> dict:
        """Get current state.
        
        Returns:
            dict: Current scoreboard state
        """
        return self._state.copy()
    
    def set_local_name(self, name: str) -> None:
        """Update local team name.
        
        Args:
            name (str): Team name
        """
        if not name:
            name = "LOCAL"
        self._state["local"]["name"] = name
        self._save_state()
    
    def set_visitor_name(self, name: str) -> None:
        """Update visitor team name.
        
        Args:
            name (str): Team name
        """
        if not name:
            name = "VISITOR"
        self._state["visitor"]["name"] = name
        self._save_state()

    def get_local_set_score(self, set_number: int) -> int:
        """Get local team score for a specific set.
        
        Args:
            set_number (int): Set number (1-3)"""
        if 1 <= set_number <= 3:
            return self._state["local"]["sets"][set_number - 1]
        return 0
    
    def get_visitor_set_score(self, set_number: int) -> int:
        """Get visitor team score for a specific set.
        
        Args:
            set_number (int): Set number (1-3)
        """
        if 1 <= set_number <= 3:
            return self._state["visitor"]["sets"][set_number - 1]
        return 0
    
    def reset_scores(self, values="scores") -> None:
        """Reset all scores to zero."""
        if values == "all":
            self._state["local"]["name"] = "LOCAL"
            self._state["visitor"]["name"] = "VISITOR"
            self._state["local"]["color"] = "#E53935"
            self._state["visitor"]["color"] = "#1E88E5" 
        self._state["local"]["sets"] = [0, 0, 0]
        self._state["visitor"]["sets"] = [0, 0, 0]
        self._save_state()
