# 0008. Folds for presence-background data

- Status: Proposed (to revisit after version 0.2.0)
- Date: 2026-10-06

## Context
In some problems only positive locations are known (for example mapped faults)
and the rest of the area is unlabelled background, not confirmed absences.
The R package blockCV handles this in `cv_knndm` with `presence_bg = TRUE`:
distance matching is computed on presences only, and each background point
inherits the fold of its nearest presence.

## Options
- Support the same behaviour in mapvalid's kNNDM splitter.
- Leave it out and document how to combine mapvalid with other tools.

## Reference
blockCV `cv_knndm` documentation:
https://rdrr.io/cran/blockCV/man/cv_knndm.html
