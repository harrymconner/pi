#!/bin/bash

sudo apt-get update && sudo apt-get upgrade
mkdir code && cd code

# --- settings ---
git clone https://github.com/harrymconner/settings.git

# --- git ---
cp settings/.gitconfig $HOME/.gitconfig

# --- uv ---
curl -LsSf https://astral.sh/uv/install.sh | sh &&
source $HOME/.local/bin/env &&
uv python install

# --- docker ---
sudo apt-get install docker.io

# --- neovim ---
# cd $HOME

# sudo apt-get update && sudo apt-get upgrade &&

# # these are the dependencies for nvim and kickstart
# sudo apt-get install ninja-build gettext cmake unzip curl build-essential make gcc ripgrep xclip

# git clone https://github.com/neovim/neovim && cd neovim && git checkout stable && /
# make CMAKE_BUILD_TYPE=Release && /
# cd build && /
# cpack -G DEB && sudo dpkg -i nvim-linux64.deb

# cd $HOME && /
# sudo rm -rf neovim

# git clone https://github.com/harrymconner/kickstart.nvim.git "${XDG_CONFIG_HOME:-$HOME/.config}"/nvim
# cd .config/nvim && /
# git pull
