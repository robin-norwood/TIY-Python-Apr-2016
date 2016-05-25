import psycopg2
import json

wavedata = []

# Connect to test database
conn = psycopg2.connect("dbname=rnorwood user=rnorwood")
cur = conn.cursor()

cur.execute("""
SELECT height_meters,
        period,
        speed,
        temp_c,
        capture_date
 FROM wave_data ORDER BY capture_date
""")

data = cur.fetchall()

#print(data[0])
row = [float(x) for x in data[0][0:4]]
row.append(str(data[0][-1]))
print(row)
print(json.dumps(row))

conn.commit()
cur.close()
conn.close()
