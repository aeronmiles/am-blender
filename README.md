# AMBlender

Blender tools, pie menus and scripts for technical artists. Focused on streamlining real-time / game-engine authoring workflows: tagging, shader tweaks, batch GLB/GLTF/USDZ export, collider setup, texture management and workspace navigation.

Tested with Blender 2.90+ (upper end compatible through Blender 5.1 — see recent commits).

## Contents

This repository bundles several Blender addons plus a shell installer that copies them into your Blender user scripts directory.

### `addons/am_blender` — main addon (v1.0.3)

Organised by domain. Each submodule registers a Pie menu bound to a `Ctrl + Alt + Shift + <key>` shortcut.

| Module | Shortcut | What it does |
| --- | --- | --- |
| `convert` | `Ctrl+Alt+Shift+C` | Convert to empty mesh, deselect non-mesh, parent-in-place, reset parent transform, instance active to others, pivots to active |
| `custom_prop` | `Ctrl+Alt+Shift+P` | Add/remove custom properties: `layer`, tags, hide tag, GL flags (alpha, depth pre-pass, culling, translucency, blend add/multiply, cast shadows), GL settings (alpha index, lightmap, render layer), sphere / mesh colliders |
| `data_util` | `Ctrl+Alt+Shift+E` | Set diffuse / normal / roughness-metallic-occlusion / emission image scale (4096 → 64), (un)pack images, copy textures to export dir, reset scaled images |
| `import_export` | `Ctrl+Alt+Shift+S` | Batch-export selected objects to GLB, GLTF (embedded/separate), USDZ; export to Google `<model-viewer>` HTML template |
| `modifiers` | `Ctrl+Alt+Shift+A` | Enable / disable all modifiers on selection |
| `nav` | `Ctrl+Alt+Shift+W` (workspaces), `Ctrl+Alt+Shift+Q` (properties tabs) | Jump to workspaces (Modeling, UV, Shading, Texture Paint, Sculpting, Assets, Geometry Nodes, Scripting) or Properties editor tabs |
| `object_prop` | `Ctrl+Alt+Shift+X` | Selectability, render visibility, ray visibility (camera / diffuse / glossy / transmission / volume scatter / shadow) |
| `shader_util` | `Ctrl+Alt+Shift+Z` | Backface culling on/off, opaque vs alpha blend, LOD material swap, rename UV maps / textures, add lightmap UV2s, remove unused/unassigned materials, dedupe duplicates to base material, disconnect normal / glTF occlusion maps |
| `view` | `Ctrl+Alt+Shift+1` | Show / hide colliders |
| `properties` | — | Custom `Material` property group |
| `std` | — | Internal library: `ops` (build, copy, data, geo, find, io, modifier, shader, transform, select), `types` (enums mirroring Blender enums + `FileFormat`, `Size`, `KeyCode`, `WorkSpaceId`, …), `ui`, `dec` decorators, `meta`, `log` (loguru), `fn` helpers |
| `util` | — | `Pip` helper used by `packages.py` to auto-install Python deps on addon load |

Runtime Python dependencies (`loguru`, `jsonpickle`, `toolz`) are installed automatically to the user site-packages the first time the addon loads (`packages.py`).

### `addons/heavypoly`

Vaughan Ling's HeavyPoly pie-menu / hotkey pack for hard-surface modeling, vendored as-is (MIT). See `addons/heavypoly/README.md` and `keymaps_shortcuts.txt` for shortcuts (Space = move, `V` = views pie, `Ctrl+B` = boolean pie, etc.).

### `addons/reload_addons`

Disables then re-enables every currently enabled addon so you can iterate without restarting Blender. Exposes `ReloadEnabledAddons` — searchable via Spacebar as "Reload Enabled Addons".

### `addons-extern/BlenderUSDZ` (git submodule)

Rob McRosby's [BlenderUSDZ](https://github.com/robmcrosby/BlenderUSDZ) — installed alongside the intern addons and used by `am_blender` for USDZ export.

### `.reference/fake-bpy-module` (git submodule)

[fake-bpy-module](https://github.com/nutti/fake-bpy-module) for editor autocomplete of the `bpy` API. Not copied into Blender — used only at dev time.

## Installation

Clone with submodules, then run the installer:

```bash
git clone --recurse-submodules <repo-url> am-blender
cd am-blender
./install.sh
```

`install.sh` prompts for:

1. **Blender version** (e.g. `3.6`, `4.2`) — used to locate the per-version user scripts folder.
2. **Username** (macOS only) — to build `/Users/<user>/Library/Application Support/Blender/<ver>`.

It detects the OS and resolves the correct Blender user path:

| OS | Path |
| --- | --- |
| macOS | `/Users/<user>/Library/Application Support/Blender/<ver>` |
| Linux | `$HOME/.config/blender/<ver>` |
| WSL / Windows | `$APPDATA/Blender Foundation/Blender/<ver>` |

Existing installs of `io_scene_usdz`, `heavypoly`, `reload_addons`, `am_blender` (and legacy `am-blender` / `reload-addons`) are removed first, then the current addons are copied into `scripts/addons`. Enable them from **Edit → Preferences → Add-ons** in Blender.

## Keymap cheat sheet

The full reference is in [`keymaps_shortcuts.txt`](keymaps_shortcuts.txt). Key am_blender shortcuts (registered in [`addons/am_blender/keymap.py`](addons/am_blender/keymap.py)):

```
Ctrl+Alt+Shift+W  Workspace pie
Ctrl+Alt+Shift+Q  Properties-tab pie
Ctrl+Alt+Shift+C  Convert pie
Ctrl+Alt+Shift+P  Custom Properties pie
Ctrl+Alt+Shift+X  Object Properties pie
Ctrl+Alt+Shift+Z  Shader Utils pie
Ctrl+Alt+Shift+E  Data Utils pie
Ctrl+Alt+Shift+B  Build pie
Ctrl+Alt+Shift+A  Modifiers pie
Ctrl+Alt+Shift+S  Import / Export pie
Ctrl+Alt+Shift+1  View pie
```

HeavyPoly adds its own global keymap (Space = move, `Q` = quick favorites, etc.) — see the HeavyPoly section of `keymaps_shortcuts.txt`.

## Project layout

```
am-blender/
├── install.sh                 # installer (macOS / Linux / WSL / Windows)
├── keymaps_shortcuts.txt      # full keymap reference
├── am-blender.code-workspace  # VS Code workspace (Python autocomplete paths)
├── addons/
│   ├── am_blender/            # main addon (this repo)
│   ├── heavypoly/             # vendored HeavyPoly (MIT, Vaughan Ling)
│   └── reload_addons/         # reload-enabled-addons operator
├── addons-extern/
│   └── BlenderUSDZ/           # submodule — USDZ importer/exporter
├── assets/shaders/
└── .reference/
    └── fake-bpy-module/       # submodule — bpy stubs for editor autocomplete
```

## Development

`am-blender.code-workspace` wires up Python autocomplete paths for the VS Code Python extension, and includes the Blender user scripts folder as a second workspace root so you can edit live-installed files directly.

After editing, either:

- use **Reload Enabled Addons** (from the `reload_addons` addon) via Spacebar search, or
- re-run `./install.sh` to copy updated sources into the Blender user scripts directory.

## Credits / licenses

- `am_blender`, `reload_addons`, installer — Aeron Miles.
- `heavypoly` — © Vaughan Ling, MIT (see `addons/heavypoly/LICENSE.md`).
- `BlenderUSDZ` — Rob McRosby, see upstream repo.
- `fake-bpy-module` — nutti, see upstream repo.
