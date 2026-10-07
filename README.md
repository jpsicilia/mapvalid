# mapvalid

[![tests](https://github.com/jpsicilia/mapvalid/actions/workflows/tests.yml/badge.svg)](https://github.com/jpsicilia/mapvalid/actions/workflows/tests.yml)

**Spatial validation and area of applicability for machine-learning maps, in Python.**

> **Status: early development.** There is nothing to install yet. Follow the
> roadmap below.

## Why

Maps produced with machine learning are usually trained on field samples that
are clustered in space. Random cross-validation then tends to overestimate the
accuracy of the map, and the model may be applied to areas that look nothing
like its training data.

mapvalid brings to Python two families of methods that address these problems:

- **NNDM and kNNDM cross-validation**, to estimate how accurate a map really is.
- **Area of applicability (AOA)**, to show where a map can be trusted.

These methods are available in R through the
[CAST](https://github.com/HannaMeyer/CAST) package by Hanna Meyer and colleagues.
mapvalid is an independent Python implementation, tested against CAST's outputs.
It is not affiliated with the CAST authors.

## Roadmap

| Version | Content |
|---------|---------|
| 0.1.0 | Dissimilarity index and AOA (block-wise processing of large rasters), NNDM, kNNDM (scikit-learn compatible splitters), distance diagnostics |
| 0.2.0 | Local data point density (LPD) |

The AOA is implemented first; NNDM and kNNDM follow before the 0.1.0 release.

## Development

```bash
git clone https://github.com/jpsicilia/mapvalid.git
cd mapvalid
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pre-commit install
pytest
```

Design decisions are documented in [`docs/decisions/`](docs/decisions/).
Contributions are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md).

## References

- Meyer, H., & Pebesma, E. (2021). Estimating the area of applicability of spatial
  prediction models. *Methods in Ecology and Evolution*, 12(9), 1620-1633.
  https://doi.org/10.1111/2041-210X.13650
- Milà, C., Mateu, J., Pebesma, E., & Meyer, H. (2022). Nearest neighbour distance
  matching leave-one-out cross-validation for map validation. *Methods in Ecology
  and Evolution*, 13(6), 1304-1316. https://doi.org/10.1111/2041-210X.13851
- Linnenbrink, J., Milà, C., Ludwig, M., & Meyer, H. (2024). kNNDM CV: k-fold
  nearest-neighbour distance matching cross-validation for map accuracy
  estimation. *Geoscientific Model Development*, 17(15), 5897-5912.
  https://doi.org/10.5194/gmd-17-5897-2024

## License

GPL-3.0-or-later. See [LICENSE](LICENSE).

## Citation

See [CITATION.cff](CITATION.cff).
