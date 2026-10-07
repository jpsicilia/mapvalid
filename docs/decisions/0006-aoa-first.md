# 0006. AOA before NNDM and kNNDM

- Status: Accepted
- Date: 2026-10-06
- Supersedes the order in the original roadmap (NNDM first).

## Context
The first real use case of mapvalid is a geological fault prediction challenge
(GEMS Prize, GeoDAWN region, Nevada) with about eight weeks left. What that
project needs first is to know where the model's predictions can be trusted,
which is the AOA.

## Decision
Implement the dissimilarity index and the AOA first (until the end of November
2026). NNDM and kNNDM follow (December 2026 to February 2027). Version 0.1.0 is
released once all three are in place. In the meantime the AOA can be installed
directly from GitHub for real use.

## Why this is technically possible
The AOA threshold is computed from the dissimilarity index of the
cross-validated training data. CAST's `trainDI` accepts any fold assignment
(`CVtest`/`CVtrain`, as a list of indices or a vector of fold IDs), so the AOA
does not depend on NNDM. Until mapvalid's own splitters exist, folds can come
from existing tools, such as simple spatial blocks.
