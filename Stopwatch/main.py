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

    print("Stopwatch started! Press Enter for a lap, or type 'q' then Enter to stop.\n")

    while True:
        raw = input()
        now = time.time()

        if raw.strip().lower() == "q":
            break

        elapsed_lap = now - last_lap_time
        elapsed_total = now - start_time
        laps.append(elapsed_lap)
        last_lap_time = now
        print(f"Lap {len(laps)}: {format_seconds(elapsed_lap)}   "
if __name__ == "__main__":
    main()