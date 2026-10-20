# Checkpoint A - timeo-b

Team: G03 - T10
Repository: esilv-marketpulse-g03-t10

## TD04 - Branches + Merge

### What I did

- Started from a clean `main` branch.
- Created a feature branch and implemented `get_first_date` and `get_last_date` to display the first and last observation dates for the instrument and the benchmark.
- Committed the feature on the branch: `cf9c481 feat: display first and last observation dates`.
- Compared the branch with `main` using `git diff main..<branch>` and `git log --oneline --graph --decorate --all`.
- Switched back to `main` and merged the branch: Git performed a fast-forward.
- Captured `03_branch_merge.png`, then deleted the merged branch with `git branch -d`.

### What I understood

- A branch isolates work: before the merge, `main` did not display the dates.
- Fast-forward: `main` had not moved since the branch was created, so Git only moved the `main` pointer to my commit, without a merge commit.
- Deleting a merged branch removes the label only; the commit stays in the history of `main`.
- A merge conflict happens when two branches change the same lines; a human must choose the final content, remove the markers, then `git add` and commit.