import psycopg2

wavedata = []

# Connect to test database
conn = psycopg2.connect("dbname=rnorwood user=rnorwood")
cur = conn.cursor()

cur.execute("""
SELECT * FROM wave_data
WHERE height_meters > %s
""", [min_height])

#data = cur.fetchall()

# for row in data:
#     print("Height in meters: " + str(float(row[0])))
#
conn.commit()
cur.close()
conn.close()
