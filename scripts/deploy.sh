#!/usr/bin/env sh

set -e

cd dist

git init

git config --local user.email "sina_khorami@comp.iust.ac.ir"
git config --local user.name "Sina"

git add --all
git commit -m 'deploy'

remote_repo="https://${GITHUB_ACTOR}:${ACCESS_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
git push -f "${remote_repo}" master
