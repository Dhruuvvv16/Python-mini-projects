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
if __name__ == "__main__":
    main()