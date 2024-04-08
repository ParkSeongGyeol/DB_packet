import pymysql

# Connect to the database
conn = pymysql.connect(
    host="192.168.45.135",
    user="root",
    password="Q!w2e3r4",
    db="test",
    charset='utf8mb4'
)

try:
    with conn.cursor() as cursor:
        # Create table
        sql = """
        CREATE TABLE HealthData (
            id INT AUTO_INCREMENT,
            user_id INT,
            timestamp DATETIME,
            heart_rate INT,
            body_temp FLOAT,
            blood_pressure INT,
            steps INT,
            water_intake INT,
            sleep_duration INT,
            calorie_intake INT,
            calorie_burned INT,
            weight FLOAT,
            bmi FLOAT,
            ambient_temp FLOAT,
            humidity FLOAT,
            gps_location VARCHAR(255),
            PRIMARY KEY (id)
        );
        """
        cursor.execute(sql)

        # Insert data
        sql = """
        INSERT INTO HealthData (
            user_id, timestamp, heart_rate, body_temp, blood_pressure, steps, 
            water_intake, sleep_duration, calorie_intake, calorie_burned, weight, 
            bmi, ambient_temp, humidity, gps_location
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(sql, (1, "2023-01-01 00:00:00", 70, 36.5, 120, 10000, 2000, 8, 2000, 500, 70, 22, 25, 50, "37.5665,126.9780"))

    # Commit the transaction
    conn.commit()
finally:
    # Close the connection
    conn.close()
