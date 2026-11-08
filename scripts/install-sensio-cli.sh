#!/usr/bin/env bash
# ==============================================================================
# Sensio CLI Installer
# Automatically installs the headless `sensio` CLI tool suite on Linux systems.
# Usage: curl -fsSL https://raw.githubusercontent.com/BIG-FullFill/sensio-hub/main/scripts/install-sensio-cli.sh | bash
# ==============================================================================
set -euo pipefail

REPO="BIG-FullFill/Sensio-IoT-New"
BINARY_NAME="sensio"
INSTALL_DIR="/usr/local/bin"

# Check operating system
OS="$(uname -s | tr '[:upper:]' '[:lower:]')"
if [ "$OS" != "linux" ]; then
    echo "Error: Only Linux is supported currently by this installer (detected: $OS)." >&2
    exit 1
fi

# Check architecture
ARCH="$(uname -m)"
case "$ARCH" in
    x86_64|amd64)
        TARGET_ARCH="x86_64"
        ;;
    aarch64|arm64)
        TARGET_ARCH="aarch64"
        ;;
    *)
        echo "Error: Unsupported CPU architecture ($ARCH). Sensio CLI currently supports x86_64 and aarch64." >&2
        exit 1
        ;;
esac

echo "==> Detected system: Linux ($TARGET_ARCH)"

# Determine installation directory permissions
if [ ! -w "$INSTALL_DIR" ]; then
    if command -v sudo >/dev/null 2>&1; then
        SUDO="sudo"
    else
        INSTALL_DIR="$HOME/.local/bin"
        mkdir -p "$INSTALL_DIR"
        SUDO=""
    fi
else
    SUDO=""
fi

echo "==> Installation target: $INSTALL_DIR/$BINARY_NAME"

# Fetch latest release info
echo "==> Fetching latest release information from GitHub..."
LATEST_TAG=$(curl -s "https://api.github.com/repos/$REPO/releases" | grep '"tag_name":' | head -n 1 | cut -d '"' -f 4 || true)

if [ -z "$LATEST_TAG" ]; then
    LATEST_TAG="latest"
fi

echo "==> Found release tag: $LATEST_TAG"

# Download binary
TEMP_DIR=$(mktemp -d)
trap 'rm -rf "$TEMP_DIR"' EXIT

DOWNLOAD_URL="https://github.com/$REPO/releases/download/$LATEST_TAG/${BINARY_NAME}-${TARGET_ARCH}-unknown-linux-gnu"

echo "==> Downloading $BINARY_NAME from $DOWNLOAD_URL ..."
if curl --fail --location --silent --show-error --output "$TEMP_DIR/$BINARY_NAME" "$DOWNLOAD_URL"; then
    chmod +x "$TEMP_DIR/$BINARY_NAME"
    $SUDO cp "$TEMP_DIR/$BINARY_NAME" "$INSTALL_DIR/$BINARY_NAME"
    echo "==> Successfully installed $BINARY_NAME to $INSTALL_DIR/$BINARY_NAME"
else
    echo "==> Direct precompiled asset not available for this tag. Alternatively, run via Docker:"
    echo "    docker exec -it sensio-iot-new sensio --help"
    echo "    or install via cargo: cargo install --path . --bin sensio"
    exit 0
fi

# Verify installation
if command -v "$BINARY_NAME" >/dev/null 2>&1; then
    echo "==> Installation verified: $($BINARY_NAME --version 2>/dev/null || echo "$BINARY_NAME installed")"
    echo "==> Run 'sensio --help' or 'sensio auth login' to get started!"
fi
