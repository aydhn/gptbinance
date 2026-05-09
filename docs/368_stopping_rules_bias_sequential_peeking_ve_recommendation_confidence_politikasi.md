# Stopping Rules, Bias, Sequential Peeking, and Recommendation Confidence Policy

## Stopping Rules
Experiments must have clearly defined rules to stop for harm, incomparability, or drift.

## Continue/Pause/Stop/Rollback/Promote-Input Recommendations
The output of an experiment is a typed recommendation, not an automatic change.

## Sequential Peeking
Stopping an experiment manually just when it looks good violates the statistical validity. This must be logged as a bias finding.

## Bias Patterns
Selective window choice, survivorship selection, unequal stopping, contaminated baseline.

## Recommendation Confidence Classes
High, Medium, Low based on the trust verdict of the experiment.

## Why Result != Recommendation
A positive result with low trust (due to drift or imbalance) should not lead to a "Promote" recommendation.
