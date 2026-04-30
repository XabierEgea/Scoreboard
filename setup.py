import shutil
import subprocess
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent

proyect_folder = ROOT_DIR / "Scoreboard"
build_folder = ROOT_DIR / "build"
dist_folder = ROOT_DIR / "dist"

main_script = proyect_folder / "Scoreboard.py"
icon_file = proyect_folder / "assets" / "icon.ico"

app_name = "Scoreboard"
version = "1.0.0"
init = "__init__.py"

files_to_include = [
    "assets/icon.ico",
    "gui_files/ui_scoreboard.py",
    "gui_files/ui_color_selector.py",
    "overlay/index.html",
    "overlay/scoreboard_state.json",
    "overlay/js/overlay.js",
    "overlay/styles/modern.css",
    "overlay/styles/pelota.css",
    "secondary_windows/color_picker_dialog.py",
    "theme/colors/base_dark.py",
    "theme/colors/base_light.py",
    "theme/colors/roles.py",
    "theme/components/button.py",
    "theme/desing/button.py",
    "theme/desing/inputs.py",
    "theme/desing/text.py",
    "theme/qss/classic.qss",
    "theme/qss/modern.qss",
    f"theme/{init}",
    "theme/colors_dark.py",
    "theme/colors_light.py",
    "theme/dynamic_colors.py",
    "theme/language_manager.py",
    "theme/language_utils.py",
    "theme/state.py",
    "theme/theme.py",
    "theme/tokens.py",
    "translations/en.json",
    "translations/es.json",
    "filewriter.py",
    "folders.py",
    "scoreboard.py",
]

hidden_imports = [
    "PySide6",
    "PySide6_Addons",
    "PySide6_Essentials",
    "shiboken6"
]
# Delete previous build and dist folders
shutil.rmtree(build_folder, ignore_errors=True)
shutil.rmtree(dist_folder, ignore_errors=True)

# create new build and dist folders
shutil.os.makedirs(build_folder, exist_ok=True)
shutil.os.makedirs(dist_folder, exist_ok=True)

# copy include list to build folder
for file in files_to_include:
    file_path = proyect_folder / file
    new_file_path = build_folder / file
    new_file_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(str(file_path), str(new_file_path))

command = [
        "pyinstaller",
        "--noconfirm",
        "--onedir",
        "--icon", icon_file,
        "--windowed",
        "--name", app_name,
        "--workpath", str(build_folder),
        "--distpath", str(dist_folder), 
        str(main_script),
    ]

for hidden in hidden_imports:
    command.extend(["--hidden-import", hidden])

subprocess.run(command, check=True)