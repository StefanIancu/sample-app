"""A tiny script for testing orkestr Jobs (one-shot tasks).

A Job runs a command inside this project's deployed image and to completion.
Point a Job at this project/environment with the command:

    python job.py

It prints a clear banner with run metadata so you can confirm in the Job's run
logs that it executed, that the app's own code is present in the image, and that
the environment's env vars were injected. It exits 0 on success.

To test the failure path, set JOB_SHOULD_FAIL=true (as an env var on the
project's environment) and run the Job again - it will exit 3.
"""
import os
import platform
import socket
import sys
from datetime import datetime, timezone


def main() -> int:
    print("=" * 56)
    print("  orkestr Job - sample-app/job.py")
    print("=" * 56)
    print(f"  time (UTC):  {datetime.now(timezone.utc).isoformat()}")
    print(f"  hostname:    {socket.gethostname()}")
    print(f"  python:      {platform.python_version()}")
    print(f"  cwd:         {os.getcwd()}")

    # Prove the app's own code shipped in this image (a Job runs the same image
    # the web service was built from).
    try:
        import main  # noqa: F401

        print("  import main: ok (app code is present in the image)")
    except Exception as exc:  # pragma: no cover - diagnostic only
        print(f"  import main: FAILED ({exc})")

    # Prove the environment's env vars were injected. Set JOB_MESSAGE on the
    # project's environment to see it echoed here.
    print(f"  JOB_MESSAGE: {os.getenv('JOB_MESSAGE', '(not set)')}")
    non_orkestr = [k for k in os.environ if not k.startswith("ORKESTR_")]
    print(f"  env vars:    {len(non_orkestr)} present")

    if os.getenv("JOB_SHOULD_FAIL") == "true":
        print("  JOB_SHOULD_FAIL=true -> exiting 3 to test the failure path")
        return 3

    print("  job completed successfully")
    return 0


if __name__ == "__main__":
    sys.exit(main())
