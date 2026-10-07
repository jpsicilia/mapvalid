# 0007. Scaling AOA to large rasters

- Status: Accepted
- Date: 2026-10-06

## Context
CAST's examples are small, but real use cases have rasters with millions of
pixels. The dissimilarity index needs, for every pixel, the distance in
(weighted, scaled) predictor space to its nearest training point. A naive
pixel-by-training-point distance matrix does not fit in memory.

## Decision
- Nearest-neighbour search uses a tree index through scikit-learn's
  `NearestNeighbors`. Only the nearest neighbour is needed (k = 1).
- The index is built once on the training data; the raster is processed in
  blocks (windows) so memory use stays bounded regardless of raster size.
- The search algorithm is a parameter. Tree indexes lose their advantage as
  the number of predictors grows, so the default lets scikit-learn choose and
  the user can force brute force. CAST exposes a similar choice
  (`algorithm` in `trainDI`).
- Results must match CAST on its examples regardless of the algorithm chosen.
