# UnlearningProbe — measured local run

Ridge-regression removal experiment. Parameter agreement and utility are not proof of forgetting or privacy.

## Results

```json
{
  "original": {
    "test_rmse": 0.061342806815101056,
    "removed_record_residual": 1.3142495171950852,
    "distance_from_retrain": 0.044882622799924984
  },
  "full_retrain": {
    "test_rmse": 0.05752453322876549,
    "removed_record_residual": 1.632485578920063,
    "distance_from_retrain": 0.0
  },
  "approximate_update": {
    "test_rmse": 0.05478853879557297,
    "removed_record_residual": 1.449520341977406,
    "distance_from_retrain": 0.02640156623795941
  },
  "checks": [
    "Removal changes fitted parameters",
    "Finite approximate update"
  ],
  "scope": "Ridge-regression removal experiment. Parameter agreement and utility are not proof of forgetting or privacy."
}
```

Local experiment assertions passed. This does not establish production readiness or performance on real customer data. Source fingerprints and dependency versions are in results.json.
