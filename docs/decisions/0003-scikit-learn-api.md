# 0003. scikit-learn compatible API

- Status: Accepted
- Date: 2026-10-02

## Decision
Cross-validation strategies are exposed as scikit-learn compatible splitters,
so they work directly with `cross_val_score`, `GridSearchCV` and other tools
that accept a scikit-learn splitter.
