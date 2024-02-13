# Pre-commit git hooks

Git hooks to integrate with [pre-commit](http://pre-commit.com). Based on https://github.com/jphppd/pre-commit-hooks. Nice guy!

## Table of contents

* [Configure pre-commit](#configure-pre-commit)
* [Two ways to invoke pre-commit](#two-ways-to-invoke-pre-commit)

## Configure pre-commit

Add to `.pre-commit-config.yaml` in your git repo:

```yaml
---
# https://pre-commit.com/
# Install pre-commit for your current user:
#   pip3 install --user pre-commit
#
# and then, in the git repo:
#   pre-commit install

repos:
  - repo: https://github.com/ra2f/pre-commit-hooks
    rev: a.b.c  # Use the ref you want to point at
    hooks:
      - id: git-check-mailmap
      - id: git-forbid-binary
      - id: git-check
      - id: git-dirty
      - id: git-check-added-large-files
        args: ['--maxkb=100']
      - id: git-check-merge-conflict
      - id: git-commit-msg
      - id: generic-check-byte-order-marker
      - id: generic-check-case-conflict
      - id: generic-check-executables-have-shebangs
      - id: generic-check-symlinks
      - id: generic-check-vcs-permalinks
      - id: generic-detect-private-key
      - id: generic-end-of-file-fixer
      - id: generic-trailing-whitespace-fixer
      - id: generic-crlf-forbid
      - id: generic-crlf-remove
      - id: generic-tabs-forbid
      - id: generic-tabs-remove
      - id: generic-nbsp-forbid
      - id: generic-nbsp-remove
      - id: generic-en-dashes-forbid
      - id: generic-en-dashes-remove
      - id: json-check-syntax
      - id: json-pretty-format
      - id: shell-check-syntax
      - id: shell-check
      - id: shell-script-must-have-extension
      - id: shell-script-must-not-have-extension
      - id: shell-bashate
      - id: shell-beautysh
      - id: toml-check-syntax
      - id: xml-check-syntax
      - id: yaml-check-syntax
      - id: yaml-yamllint
      - id: cmake-format
      - id: cmake-lint
      - id: python-check-ast
      - id: python-check-docstring-first
      - id: python-debug-statements
      - id: python-double-quote-string-fixer
      - id: python-fix-encoding-pragma
      - id: python-requirements-txt-fixer
      - id: python-safetydb
      - id: python-isort-config
      - id: python-isort-seed-config
      - id: python-isort
      - id: python-black
      - id: python-pylint-config
      - id: python-pylint
      - id: python-setup-cfg-fmt
      - id: docker-lint

```

## Two ways to invoke pre-commit

If you want to invoke the checks as a git pre-commit hook, run:

```
    pre-commit install
```

If you want to run the checks on-demand (outside of git hooks), run:

```
    pre-commit run --all-files --verbose
```
