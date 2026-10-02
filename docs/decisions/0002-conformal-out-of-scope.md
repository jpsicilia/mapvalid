# 0002. Conformal prediction is out of scope

- Status: Accepted
- Date: 2026-10-02

## Context
Calibrated prediction intervals are closely related to map validation.

## Decision
mapvalid does not implement conformal prediction. Mature Python packages
already cover it (for example MAPIE and geoconformal). mapvalid's splitters
should work together with them instead.
