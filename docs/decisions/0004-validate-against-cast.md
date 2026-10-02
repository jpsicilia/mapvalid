# 0004. Validate every method against CAST

- Status: Accepted
- Date: 2026-10-02

## Decision
Every method is tested against reference outputs produced by the R package
CAST on the same data, with a fixed seed and a documented numerical tolerance.
Any intentional difference from CAST is documented in its own decision record.
