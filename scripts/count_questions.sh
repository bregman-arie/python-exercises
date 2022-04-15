#!/usr/bin/env bash

echo $(( $(grep -E "\[Exercise\]|</summary>" -c README.md )))
