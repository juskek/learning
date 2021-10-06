# Flaky Tests
- Non-deterministic tests
  - Produces different results with the same code

## Causes
- Concurrency
- Non-deterministic/undefined behaviours
- Flaky third party code
- infrastructre problems
  


## Mitigation
- Automatically re-run failing tests during presubmit
  - Report failure if it fails 3 times in a row
  - Disadv.: 
    - Long integration tests (e.g., 15 min) will only be reported as failure after 45 mins
- Monitoring flakiness level
  - Quarantine if test is too flaky
    - Removes test from critical path and files bug to remove flakiness
- Monitoring change in flakiness level
  - Identifies change in test which caused change in flakiness
