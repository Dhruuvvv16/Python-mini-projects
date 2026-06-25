import argparse
import sys
import time


def countdown(minutes, label):
    total_seconds = int(minutes * 60)
    print(f"\n{label} - {minutes} minute(s)")
    try:
        for remaining in range(total_seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            sys.stdout.write(f"\r  {mins:02d}:{secs:02d} remaining   ")
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nTimer interrupted. Stopping.")
        sys.exit(0)
    sys.stdout.write("\r  00:00 remaining   \n")
    print(f"{label} complete!\a")


def build_parser():
    parser = argparse.ArgumentParser(description="A simple Pomodoro timer.")
    parser.add_argument("--work", type=float, default=25, help="Work session length in minutes (default: 25)")
    parser.add_argument("--short-break", type=float, default=5, help="Short break length in minutes (default: 5)")
    parser.add_argument("--long-break", type=float, default=15, help="Long break length in minutes (default: 15)")
    parser.add_argument("--cycles", type=int, default=4, help="Work sessions before a long break (default: 4)")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    print("=" * 40)
    print("   POMODORO TIMER")
    print("=" * 40)
    print("Press Ctrl+C at any time to stop.\n")

    cycle = 1
    while True:
        countdown(args.work, f"Cycle {cycle}: Focus time")

        if cycle % args.cycles == 0:
            countdown(args.long_break, "Long break")
        else:
            countdown(args.short_break, "Short break")

        again = input("\nStart next cycle? (y/n): ").strip().lower()
        if again != "y":
            print("Great work today!")
            break
        cycle += 1


if __name__ == "__main__":
    main()