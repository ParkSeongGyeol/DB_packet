import pymysql

# Connect to the database
conn = pymysql.connect(
    host="192.168.45.135",
    user="root",
    password="Q!w2e3r4",
    charset='utf8mb4'
)

try:
    with conn.cursor() as cursor:
        # Create database
        sql = "CREATE DATABASE IF NOT EXISTS healthcare;"
        cursor.execute(sql)

        # Use the new database
        sql = "USE healthcare;"
        cursor.execute(sql)

        # Create table
        sql = """
        CREATE TABLE IF NOT EXISTS HealthData (
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

    # Commit the transaction
    conn.commit()
finally:
    # Close the connection
    conn.close()
