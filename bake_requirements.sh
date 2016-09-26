#!/bin/bash -e

for TARGET in 'base' 'local' 'test'; do
    pip-compile requirements/${TARGET}.in > requirements/${TARGET}.txt
done
