import psycopg2

def get_by_min_height(min_height):
    # Connect to test database
    conn = psycopg2.connect("dbname=rnorwood user=rnorwood")
    cur = conn.cursor()

    cur.execute("""
    SELECT * FROM wave_data
    WHERE height_meters > %s
    """, [min_height])

    raw_data = cur.fetchall()

    clean_data = []
    for row in raw_data:
        clean_data.append( [float(x) for x in row[1:5] ] + [str(row[-1])] )
#    conn.commit()
    cur.close()
    conn.close()

    return clean_data

if __name__ == '__main__':
    print(get_by_min_height(1.0))
