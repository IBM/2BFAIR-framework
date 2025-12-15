# Copyright (C) 2025 IBM Corp.
# SPDX-License-Identifier: Apache-2.0

#!/bin/bash

set -e # Exit on error.

echo "travis_fold:start:Building angular application..."

echo ==================
echo == Creating app ==
echo ==================
mkdir -p spl-app
node main.js

echo =============================
echo == Installing dependencies ==
echo =============================
cd spl-app
npm install --legacy-peer-deps --cache=tmp

# FIXME(kcsys4sd/dwb-ide#112): Added this dependency due to build errors.
npm install @types/topojson-specification --legacy-peer-deps

echo ==========================
echo == Building application ==
echo ==========================
npm run build -- --configuration=production --progress=false

echo "travis_fold:end:Angular application built"
