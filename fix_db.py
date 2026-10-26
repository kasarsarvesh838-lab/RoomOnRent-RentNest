import sqlite3

# Connect to existing database
con = sqlite3.connect("app.db")
cur = con.cursor()

# Add missing columns if they don't exist
try:
    cur.execute("ALTER TABLE users ADD COLUMN email TEXT DEFAULT ''")
    print("✅ email column added")
except sqlite3.OperationalError:
    print("⚠ email column already exists")

try:
    cur.execute("ALTER TABLE users ADD COLUMN phone TEXT DEFAULT ''")
    print("✅ phone column added")
except sqlite3.OperationalError:
    print("⚠ phone column already exists")

try:
    cur.execute("ALTER TABLE users ADD COLUMN upi_id TEXT DEFAULT ''")
    print("✅ upi_id column added")
except sqlite3.OperationalError:
    print("⚠ upi_id column already exists")

con.commit()
con.close()
print("🎉 Done! Database updated successfully.")
