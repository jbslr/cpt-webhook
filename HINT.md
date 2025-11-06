# Hint

That cargo you just stashed — go check whether it's actually in the hold,
or just on the manifest. `git lfs ls-files` and a peek at the file itself
will tell you fast. If the file just shows a pointer (starts with
`version https://git-lfs.github.com/spec/v1`), `git lfs pull` fetches the
real cargo from the LFS store.
