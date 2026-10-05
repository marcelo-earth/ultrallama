"""Baseline load profile scaffold for UltraLlama."""

import argparse
import time


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="UltraLlama load profile scaffold")
    parser.add_argument("--users", type=int, default=1)
    parser.add_argument("--requests", type=int, default=20)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    start = time.time()
    for _ in range(args.requests):
        # Placeholder for request call against vLLM endpoint.
        time.sleep(0.01)
    elapsed = time.time() - start
    rps = args.requests / elapsed if elapsed else 0.0
    print(f"users={args.users} requests={args.requests} elapsed={elapsed:.2f}s rps={rps:.2f}")


if __name__ == "__main__":
    main()
