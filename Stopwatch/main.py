import time

def format_seconds(seconds):
    minutes, secs = divmod(seconds, 60)
    return f"{int(minutes):02d}:{secs:05.2f}"


def main():
    print("=" * 40)
    print("   STOPWATCH")
    print("=" * 40)
    input("Press Enter to start...")

    start_time = time.time()
    last_lap_time = start_time
    laps = []

if __name__ == "__main__":
    main()