# Sistema de Traducción - Scoreboard

## Cómo funciona

El sistema de traducción utiliza archivos JSON en la carpeta `translations/` para almacenar todas las cadenas de texto de la aplicación.

## Estructura de archivos

```
gui_files/
├── ui_scoreboard.py           # Generado por Qt Designer (NO modificar)
├── ui_color_selector.py       # Generado por Qt Designer (NO modificar)
├── scoreboard_wrapper.py       # Wrapper - Aquí va la lógica de traducciones
└── color_selector_wrapper.py   # Wrapper - Aquí va la lógica de traducciones
```

## ⚠️ IMPORTANTE

Los archivos `ui_*.py` son generados automáticamente por Qt Designer. **NO deben ser modificados manualmente**, ya que se sobrescriben cada vez que regeneras el UI.

Para agregar traducciones o lógica personalizada, usa siempre los archivos `*_wrapper.py`:
- `scoreboard_wrapper.py` → Traducciones para la ventana principal
- `color_selector_wrapper.py` → Traducciones para el diálogo de colores

## Agregar un nuevo idioma

### Paso 1: Crear un nuevo archivo de traducción

Crea un archivo JSON en `translations/` con el código del idioma (ej: `fr.json` para francés):

```json
{
  "menu": {
    "options": "Votre texto aquí",
    "mode": "Modo",
    ...
  },
  "scoreboard": {
    "local": "LOCAL",
    ...
  },
  "color_picker": {
    "title": "Configurar Colores",
    ...
  }
}
```

### Paso 2: Usar el idioma en la aplicación

Desde el código Python, puedes cambiar el idioma así:

```python
from theme.language_manager import language_manager

# Cambiar al idioma
language_manager.set_language("fr")

# Obtener una traducción
texto = language_manager.get("scoreboard.local", "LOCAL")
```

### Paso 3: En la ventana principal

Si necesitas actualizar la UI completa cuando cambies idioma:

```python
window.set_language("fr")
```

## Estructura de las claves de traducción

Las claves siguen este patrón: `categoría.clave`

**Categorías existentes:**
- `menu` - Elementos del menú
- `scoreboard` - Elementos principales del marcador
- `color_picker` - Diálogo de selección de colores

## Idiomas disponibles

- **es.json** - Español
- **en.json** - Inglés

## Agregar más idiomas

Simplemente copia uno de los archivos JSON existentes y traduce todos los valores (no las claves):

```
translations/
├── es.json      # Español
├── en.json      # Inglés
├── fr.json      # Francés (agregar)
├── de.json      # Alemán (agregar)
└── ...
```

Cada vez que agregues un nuevo idioma, reinicia la aplicación para que lo cargue.

## Flujo de traducción

```
Qt Designer crea/modifica UI
       ↓
ui_*.py (Generado automáticamente)
       ↓
*_wrapper.py (Hereda de ui_*.py)
       ↓
Aplica traducciones desde JSON
       ↓
Resultado final en la UI
```

## Notas

- Siempre proporciona valores por defecto en inglés en el código en caso de que una traducción no exista
- El idioma por defecto al iniciar es español ("es")
- Las claves de traducción son case-sensitive
- Los wrappers pueden regenerarse sin perder cambios - la lógica está separada de los archivos generados

