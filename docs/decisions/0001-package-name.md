# 0001. Package name: mapvalid

- Status: Accepted
- Date: 2026-10-02

## Context
The package needs a short, searchable name that covers both parts of its scope:
how accurate a map is (spatial cross-validation) and where it can be trusted
(area of applicability).

## Decision
`mapvalid`. "Map validation" is the term used in the methods' own literature.
The name was free on PyPI and had no conflicting projects on GitHub on
2026-10-02.

## Alternatives considered
- `castpy`: suggests an official port of CAST.
- `geovalid`: commonly associated with validating geometries.
- `spatialcv`, `geocv`: "CV" is often read as computer vision in Earth observation.
- `geoaoa`: names only half of the scope.
