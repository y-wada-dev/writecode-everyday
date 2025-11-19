import sqlite3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DB = Path("mini.db")

with sqlite3.connect(DB) as conn:
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sales(
        id INTEGER PRIMARY KEY,
        y INTEGER, m INTEGER, store TEXT, amount REAL
      )
    """)

    cur.execute("DELETE FROM sales")
    rows =[
        (2025, 7, "A", 120.0), (2025, 7, "B", 95.0),  (2025, 7, "C", 80.0),
        (2025, 8, "A", 130.0), (2025, 8, "B", 110.0), (2025, 8, "C", 90.0),
        (2025, 9, "A", 140.0), (2025, 9, "B", 105.0), (2025, 9, "C", 100.0),
    ]
    cur.executemany("INSERT INTO sales(y,m,store,amount) VALUES(?,?,?,?)", rows)
    conn.commit()

with sqlite3.connect(DB) as conn:
    df = pd.read_sql_query("""
      SELECT y, m, store, amount
      FROM sales
      ORDER BY y, m, store
    """, conn)

print(df)

pt = df.pivot_table(index=["y", "m"], columns="store", values="amount", aggfunc="sum")
ax = pt.plot(kind="bar", figsize=(7, 4))
ax.set_title("Monthly Sales by Store")
ax.set_xlabel("Year-Month")
ax.set_ylabel("Sales")
plt.tight_layout()
plt.show()
