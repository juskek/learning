# Testing Stages

## Individual Ad-Hoc Testing
- Testing without planning or documentation
## Presubmit
- Executes tests known to be affected by edited code
  - "Affected" determined by
    - Project Definition: Configuration file maintained by teams 
- Presubmit must be run before a commit

### Efficacy Presubmit Service
- Selectively running tests which are predicted to fail with ML
- Advantages:
  - No need to run tests which will pass at Presubmit
- ML Model:
  - Paradigm: Supervised
  - Type: Binary Classification
  - Features:
    - Recent failure history
    - Distance metrics from source files to test
    - Test size and runtime data
  - Target: 
    - Pass/Fail
  - Performance Parameters:
    - Sensitivity
      - Failing tests which are executed
    - Specificity
      - Passing tests which are skipped
## Continuous Build/Integration (CB/CI)
- Continuous running of all tests on latest commit

## Notes
- Same test may run several times throughout the stages
  - Missed failure at presubmit is not critical since it will run again at CB

test