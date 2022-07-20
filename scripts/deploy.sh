#!/usr/bin/env sh

set -e

cd dist

git init

git config --local user.email "sinakhorrami94@gmail.com"
git config --local user.name "Sina"

git add --all
git commit -m 'auto deploy'

remote_repo="https://${GITHUB_ACTOR}:${ACCESS_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
git push -f "${remote_repo}" master
