# Noctyra Meta Package

The **Noctyra Meta Package** is the easiest way to install the complete Noctyra environment on Arch Linux. It acts as a single entry point to install all necessary components, including dotfiles, the CLI tool, and essential applications.

## What's Included?

Installing this package will automatically pull in the following dependencies:

### Core Components
- **`noctyra-dotfiles`** (or `noctyra-dotfiles-git`): The complete configuration files (stow packages).
- **`noctyra-cli`** (or `noctyra-cli-git`): The `noctyra` command-line tool for managing the environment.

### Applications
- **`kitty`**: Use as the default terminal emulator.
- **`dolphin`**: The file manager.
- **`gpu-screen-recorder`**: For screen recording.

## Installation

### From AUR (recommended)

If the package is published on the AUR, you can install it using your favorite AUR helper (e.g., `yay` or `paru`):

```bash
# Stable version
yay -S noctyra-meta

# Git version (latest commits)
yay -S noctyra-meta-git
```

This will automatically resolve and install all dependencies.

### Manual Installation

You can also build and install the package manually using `makepkg`.

1. Clone this repository:
   ```bash
   git clone https://github.com/noctyra-dots/meta.git noctyra-meta
   cd noctyra-meta
   ```

2. Build and install:
   ```bash
   # For stable version
   makepkg -si

   # For git version
   makepkg -p PKGBUILD-git -si
   ```

## Usage

Once installed, you can use the `noctyra` CLI to set up your environment:

```bash
# Install/Link dotfiles
noctyra install
```
