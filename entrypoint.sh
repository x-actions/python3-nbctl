#!/bin/bash
set -e

export LOG_LEVEL=${LOG_LEVEL:-"DEBUG"}
export SCRIPT=${SCRIPT:-"echo `date`"}

echo $(pwd)
echo "## Check Package Version ##################"
bash --version
git version

echo "env is:"
env

echo "## Run nbctl ##################"

eval ${SCRIPT}
