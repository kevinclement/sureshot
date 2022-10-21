#!/bin/bash
find config modes -type f -name "*.yaml" -exec mpf format "{}" --yes \;