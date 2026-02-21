# Custom Add-ons

This folder stores custom Anki add-ons as git submodules under the `~/Repos/anki` fork.
Workspace path: `~/Repos/anki/addons/`

Each add-on has its own repository and history, while `~/Repos/anki` pins the exact
submodule commit used locally.

Runtime load path remains:
`~/Library/Application Support/Anki2/addons21/`

Use symlinks from the runtime add-ons directory to folders in this repo
for custom add-ons.
Keep AnkiWeb-managed add-ons (typically numeric IDs) in the runtime
directory unless explicitly migrated.
