# Scoreboard — Marcador para OBS Studio

Aplicación de marcador en tiempo real diseñada para emisiones en **OBS Studio**. Incluye una interfaz de escritorio para controlar la puntuación y un overlay HTML que se actualiza automáticamente en la retransmisión.

> **⚠️ Estado: Beta**
> El proyecto está en desarrollo activo. Actualmente solo está implementado para **pelota vasca** (3 sets, máximo 15 puntos por set). Faltan funcionalidades y puede haber cambios importantes en futuras versiones.

---

## ¿Cómo funciona?

El sistema tiene dos partes que trabajan juntas:

1. **Aplicación de escritorio** (`scoreboard.py`) — Panel de control para gestionar nombres de equipos, puntuaciones y colores.
2. **Overlay HTML** (`overlay/index.html`) — Tabla de puntuación transparente que se añade como fuente en OBS. Se actualiza sola cada 500 ms leyendo el estado que escribe la aplicación.

```
[Aplicación de escritorio]  →  overlay/scoreboard_state.json  →  [Overlay en OBS]
```

---

## Instalación

**Requisitos:** Python 3.10+

```bash
pip install -r requirements.txt
```

---

## Uso

### 1. Iniciar la aplicación de escritorio

```bash
python scoreboard.py
```

Desde el panel puedes:
- Escribir el nombre de cada equipo (local y visitante)
- Sumar o restar puntos con los botones `+` / `-`
- Avanzar o retroceder entre los 3 sets con **Siguiente set** / **Set anterior**
- Cambiar los colores de cada equipo desde el menú **Colors**
- Resetear todos los marcadores con el botón **Reset**

### 2. Añadir el overlay en OBS Studio

1. En OBS, en el panel **Fuentes**, haz clic en **+** y selecciona **Navegador**.
2. Marca la opción **Archivo local**.
3. Navega hasta la carpeta del proyecto y selecciona: `overlay/index.html`
4. Ajusta el **ancho** y el **alto** según tu escena (recomendado: 800 × 200).
5. Haz clic en **Aceptar**.

El overlay empezará a mostrar la puntuación en tiempo real. Cada vez que modifiques algo en la aplicación de escritorio, el overlay se actualizará automáticamente en pocos segundos.

> **Nota:** Tanto la aplicación de escritorio como OBS deben estar abiertos a la vez durante la retransmisión.

---

## Estructura del proyecto

```
Scoreboard/
├── scoreboard.py          # Aplicación de escritorio (punto de entrada)
├── filewriter.py          # Gestión del estado en JSON
├── overlay/
│   ├── index.html         # Overlay para OBS
│   ├── scoreboard_state.json  # Estado compartido (escrito por la app)
│   ├── js/overlay.js      # Lógica de actualización del overlay
│   └── styles/
│       └── pelota.css     # Estilos del overlay
├── theme/                 # Sistema de temas (modo claro/oscuro, estilos)
├── translations/          # Traducciones (es/en)
└── requirements.txt
```

---

## Deportes soportados

| Deporte | Sets | Puntos por set |
|---|---|---|
| Pelota vasca | 3 | 15 |

Se prevé añadir soporte para otros deportes en versiones futuras.
