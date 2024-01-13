#!/bin/bash
if [[ ! -d "$HOME/.local/bin" ]]; then
    mkdir "$HOME/.local/bin"
fi


cp -r "../pyinit" "$HOME/.local/bin/"