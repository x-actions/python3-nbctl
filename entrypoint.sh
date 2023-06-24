#!/bin/bash
set -e

export LOG_LEVEL=${INPUT_LOG:-"DEBUG"}
export INPUT_SCRIPT=${INPUT_SCRIPT:-"echo `date`"}

echo $(pwd)
echo "## Check Package Version ##################"
bash --version
git version

echo "env is:"
env

echo "## Run nbctl ##################"

eval ${INPUT_SCRIPT}
