# GitHub Actions Free Compute Claim

This repository is a tiny proof that the `codewithx55` GitHub account can run free compute on standard GitHub-hosted runners through a public repository.

## What Is Secured

| Surface | Status | Notes |
|---|---:|---|
| ClickHouse service container | Claimed when workflow succeeds | The ClickHouse proof starts a `clickhouse/clickhouse-server:24.8-alpine` service container and runs analytical SQL on a hosted runner. |
| GitHub-hosted Ubuntu runner | Claimed when workflow succeeds | Public repositories can use standard runners for free under GitHub's current billing docs. |
| Memcached service container | Claimed when workflow succeeds | The Memcached proof starts a `memcached:1.6-alpine` service container and exercises the text protocol on a hosted runner. |
| Meilisearch service container | Claimed when workflow succeeds | The Meilisearch proof starts a `getmeili/meilisearch:v1.48.2` service container, indexes documents, and runs search queries on a hosted runner. |
| MySQL service container | Claimed when workflow succeeds | The MySQL proof starts a `mysql:8.0` service container and runs SQL inside it on a hosted runner. |
| MongoDB service container | Claimed when workflow succeeds | The MongoDB proof starts a `mongo:7.0` service container and runs document inserts plus aggregation on a hosted runner. |
| NATS service container | Claimed when workflow succeeds | The NATS proof starts a `nats:2-alpine` service container and verifies pub/sub messaging on a hosted runner. |
| Qdrant service container | Claimed when workflow succeeds | The Qdrant proof starts a `qdrant/qdrant:v1.18.2` service container, indexes vectors, and runs nearest-neighbor search on a hosted runner. |
| RabbitMQ service container | Claimed when workflow succeeds | The RabbitMQ proof starts a `rabbitmq:3-management-alpine` service container and verifies exchange/queue message routing on a hosted runner. |
| Payment method | Not used | This repo avoids paid/larger runners and does not configure billing. |
| Secrets | Not used | The smoke job intentionally avoids credentials. |

## Smoke Job

The workflow prints runner metadata, CPU information, memory, disk, Python version, and a small deterministic CPU benchmark.
