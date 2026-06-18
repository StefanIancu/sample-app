# sample-app

[![Deployed on orkestr](https://api.orkestr.eu/badge/definitely-production-ready.svg)](https://definitely-production-ready.orkestr.run)

[![Deploy to orkestr](https://orkestr.eu/deploy-button.svg)](https://orkestr.eu/new?repo=https%3A%2F%2Fgithub.com%2FStefanIancu%2Fdefinitely-production-ready)

A tiny FastAPI app used to test orkestr deployments.

- `GET /` - greeting
- `GET /health` - health probe
- Set `FORCE_CRASH=true` to make startup fail on purpose (deploy-failure testing).

## Deploy as a project

Connect this repo in orkestr and deploy. It builds from the included
`Dockerfile` and serves on port 8000.

## Test a Job

`job.py` is a one-shot script meant to be run by an orkestr Job. Create a Job
against this project/environment with the command:

```
python job.py
```

It prints run metadata and exits 0. To test the failure path, set
`JOB_SHOULD_FAIL=true` on the environment and run it again (exits 3). Set
`JOB_MESSAGE` to confirm env vars are injected into the Job.

<!-- orkestr pr_opened reaction smoke test -->
