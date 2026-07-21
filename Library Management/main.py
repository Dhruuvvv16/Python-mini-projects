import argparse
import os
import sqlite3

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "library.db")


if __name__ == "__main__":
    main()