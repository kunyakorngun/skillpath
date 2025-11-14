import psycopg2

# --- 1. ตั้งค่าการเชื่อมต่อ Postgres ---
conn = psycopg2.connect(
    host="localhost",      # ถ้ารันใน docker-compose network ใช้ "postgres"
    port=5432,
    dbname="postgres",
    user="skillpath",
    password="skillpath123"
)
cur = conn.cursor()

# --- 2. สร้างตาราง applied_process ---
cur.execute("""
CREATE TABLE IF NOT EXISTS applied_process (
    id SERIAL PRIMARY KEY,
    position VARCHAR(100) NOT NULL,
    company VARCHAR(200) NOT NULL,
    location VARCHAR(100),
    date DATE,
    progress SMALLINT CHECK (progress BETWEEN 1 AND 5)
);
""")
conn.commit()

# --- 3. ใส่ข้อมูลตัวอย่าง ---
sample_data = [
    ("Data Scientist", "The Siam Cement Public Company Limited (SCG.)", "Bangkok", "2025-09-20", 1),
    ("Data Engineer", "The Siam Cement Public Company Limited (SCG.)", "Bangkok", "2025-09-20", 1)
]

cur.executemany(""" 
INSERT INTO applied_process (position, company, location, date, progress)
VALUES (%s, %s, %s, %s, %s);
""", sample_data)

conn.commit()
print("✅ Table created and data inserted successfully!")

cur.close()
conn.close()
