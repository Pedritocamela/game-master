import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT", 3306))
        )
        return connection
    except Error as e:
        print(f"Error conectando a MySQL: {e}")
        return None

def get_all_games():
    connection = get_connection()
    if not connection:
        return []
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM games ORDER BY id DESC")
        games = cursor.fetchall()
        return games
    finally:
        cursor.close()
        connection.close()

def get_game_by_id(game_id: int):
    connection = get_connection()
    if not connection:
        return None
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM games WHERE id = %s", (game_id,))
        game = cursor.fetchone()
        return game
    finally:
        cursor.close()
        connection.close()

def create_game(name: str, platform: str, price: float, discount: int, image_url: str):
    connection = get_connection()
    if not connection:
        return None
    try:
        cursor = connection.cursor()
        sql = """
            INSERT INTO games (name, platform, price, discount, image_url)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (name, platform, price, discount, image_url))
        connection.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        connection.close()

def update_game(game_id: int, name: str, platform: str, price: float, discount: int, image_url: str):
    connection = get_connection()
    if not connection:
        return False
    try:
        cursor = connection.cursor()
        sql = """
            UPDATE games 
            SET name = %s, platform = %s, price = %s, discount = %s, image_url = %s
            WHERE id = %s
        """
        cursor.execute(sql, (name, platform, price, discount, image_url, game_id))
        connection.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        connection.close()

def delete_game(game_id: int):
    connection = get_connection()
    if not connection:
        return False
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM games WHERE id = %s", (game_id,))
        connection.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        connection.close()
