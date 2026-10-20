# Checkpoint A - Neilouuu

- Student: Neil GHARBI TORCHOUNA (@Neilouuu)
- TD Group: G03 - Team: T10
- Repository: `esilv-marketpulse-g03-t10`

## Scope

Checkpoint Phase A: TD01 to TD04.

## Evidence

| File | Shows |
|---|---|
| `01_terminal_python.png` | Repository root (`pwd`), Python version, `python src/main.py` running |
| `02_git_status_log.png` | Clean `git status` and local history with `git log --oneline` |
| `03_branch_merge.png` | `feature/display-observation-dates` listed as merged, `main` containing the feature commit |

## What I did

- TD01: team repository, Codespaces, Linux navigation (`pwd`, `ls`, `cd`, `cat`, `head`, `grep`).
- TD02: loaded JSON and CSV, filtered AAPL and SP500, converted `close` to `float`, reusable summary function.
- TD03: local Git workflow (`status`, `diff`, `add`, `diff --staged`, `commit`, `log`, `show`).
- TD04: created `feature/display-observation-dates`, added `get_first_date` and `get_last_date`, committed on the branch, compared with `main`, merged into `main`.

## Merge explanation

The merge was a fast-forward: `main` had no new commit since the branch was created, so Git moved `main` to the feature commit without creating a merge commit. The graph stays linear and that is valid.

## Security

No password, token, email address or personal data appears in these files.
