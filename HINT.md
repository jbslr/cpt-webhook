# Hint

Same story as the other crew's cargo — check the manifest against what's
actually in the hold. `git lfs ls-files` first, then look at the raw file.
A pointer instead of real content? `git lfs pull` will fetch it from the
LFS store.
