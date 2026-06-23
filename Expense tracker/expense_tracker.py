import argparse
import csv
import os
from datetime import datetime
from collections import defaultdict

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.csv")
FIELDS = ["date", "amount", "category", "note"]
