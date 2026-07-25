

#!/usr/bin/env python3
import argparse
from datetime import datetime

def main():
	parser = argparse.ArgumentParser(description="Simple demo script for Git practice")
	parser.add_argument("--name", "-n", default="World", help="Name to greet")
	args = parser.parse_args()
	now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	print(f"Hello, {args.name}! Current time: {now}")

if __name__ == "__main__":
	main()

