
#!/usr/bin/env python3
"""Simple feature: compute basic statistics for a list of numbers.

Usage:
	python Features/myfeature.py -n 1 2 3 4 5
	python Features/myfeature.py --numbers 3.5 2.1 7.8
"""
from __future__ import annotations
import argparse
import statistics
from typing import Iterable, List


def compute_stats(values: Iterable[float]) -> dict:
	nums: List[float] = list(values)
	if not nums:
		return {"count": 0}
	return {
		"count": len(nums),
		"min": min(nums),
		"max": max(nums),
		"mean": statistics.mean(nums),
		"median": statistics.median(nums),
		"stdev": statistics.pstdev(nums) if len(nums) > 1 else 0.0,
	}


def main() -> None:
	parser = argparse.ArgumentParser(description="Compute basic statistics for numbers")
	parser.add_argument("-n", "--numbers", nargs="+", type=float, help="List of numbers", required=True)
	args = parser.parse_args()
	stats = compute_stats(args.numbers)
	if stats.get("count", 0) == 0:
		print("No numbers provided.")
		return
	print("Statistics:")
	print(f"  Count : {stats['count']}")
	print(f"  Min   : {stats['min']}")
	print(f"  Max   : {stats['max']}")
	print(f"  Mean  : {stats['mean']:.4f}")
	print(f"  Median: {stats['median']}")
	print(f"  Stdev : {stats['stdev']:.4f}")


if __name__ == "__main__":
	main()
