import time

def format_seconds(seconds):
    minutes, secs = divmod(seconds, 60)
    return f"{int(minutes):02d}:{secs:05.2f}"

if __name__ == "__main__":
    main()