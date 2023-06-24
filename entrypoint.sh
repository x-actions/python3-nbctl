#!/bin/bash
set -e

export LOG_LEVEL=${LOG_LEVEL:-"DEBUG"}
export SCRIPT=${SCRIPT:-"`date`"}

echo $(pwd)
echo "## Check Package Version ##################"
bash --version
git version

echo "## Run nbctl ##################"

eval ${SCRIPT}
