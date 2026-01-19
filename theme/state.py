from theme.colors.roles import RoleColors


class ThemeState:
    """Global state manager for theme and colors."""
    
    mode = "dark"
    style = "modern"

    local_color = "#E53935"      # Red
    visitor_color = "#1E88E5"    # Blue
    set_color = "#2DFB4F"        # Green
    reset_color = "#B71C1C"      # Dark Red

    # Dynamic colors (user)
    role_colors = {
        "local": RoleColors.LOCAL,
        "visitor": RoleColors.VISITOR,
        "set": RoleColors.SET,
        "danger": RoleColors.RESET,
    }
