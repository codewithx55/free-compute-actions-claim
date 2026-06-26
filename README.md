# GitHub Actions Free Compute Claim

This repository is a tiny proof that the `codewithx55` GitHub account can run free compute on standard GitHub-hosted runners through a public repository.

## What Is Secured

| Surface | Status | Notes |
|---|---:|---|
| GitHub-hosted Ubuntu runner | Claimed when workflow succeeds | Public repositories can use standard runners for free under GitHub's current billing docs. |
| MySQL service container | Claimed when workflow succeeds | The MySQL proof starts a `mysql:8.0` service container and runs SQL inside it on a hosted runner. |
| Payment method | Not used | This repo avoids paid/larger runners and does not configure billing. |
| Secrets | Not used | The smoke job intentionally avoids credentials. |

## Smoke Job

The workflow prints runner metadata, CPU information, memory, disk, Python version, and a small deterministic CPU benchmark.
