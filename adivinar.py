import sqlite3 as sql
import random
import sys

class TheGame:

    def __init__(self, conn):
        self.conn = conn
        self.conn.commit()
        self.conn.close()
        self.hello = "Hola usuario, bienvenido a este juego"

        self.create_table()
        self.message()
        self.game()
        self.insert_data(self.user_name, self.wins, self.loser)

    def create_table(self):
        self.conn = sql.connect("logs_players.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
          """CREATE TABLE IF NOT EXISTS logs(
           name TEXT,
           wins INTEGER,
           loser INTEGER
          )"""
)
        self.conn.commit()
        self.conn.close()

    def insert_data(self, player, wins, loser):
        self.conn = sql.connect("logs_players.db")
        self.cursor = self.conn.cursor()
        self.instruction = f"INSERT INTO logs VALUES('{player}', {wins}, {loser})"
        self.cursor.execute(self.instruction)
        self.conn.commit()
        self.conn.close()

    def see_data(self):
        self.conn = sql.connect("logs_players.db")
        self.cursor = self.conn.cursor()
        self.instruction = "SELECT * FROM logs;"
        self.cursor.execute(self.instruction)
        self.get_data = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()

        for i in self.get_data:
            self.list_players = i[0]
            self.list_wins = i[1]
            self.list_loser = i[2]
        print(f"""Jugadores que han jugado este juego: {self.list_players}
        Ganadores: {self.list_wins}
        Perdedores: {self.list_loser}""")

    def drop_data(self):
        self.conn = sql.connect("logs_players.db")
        self.cursor = self.conn.cursor()
        self.instruction = "DROP TABLE logs"
        self.cursor.execute(self.instruction)
        self.conn.commit()
        self.conn.close()

    def message(self):
        print(f"{self.hello}\n")
        self.user_name = input("¿Cómo te llamas?: ").title()

        print(f"\nMucho gusto {self.user_name}\n")

    def game(self):
        self.number = random.randint(1, 100)
        self.trys = 0
        self.wins = 0
        self.loser = 0
        while True:
            self.user_game = input(f"{self.user_name} adivina un número del 1 al 100: ")
            self.trys += 1

            if self.user_game == "salir" or self.user_game == "exit":
                print("Saliendo del juego\n")
                self.loser += 1
                sys.exit()

            elif self.user_game == "see":
                self.see_data()
            elif self.user_game == "drop":
                self.drop_data()
                self.create_table()

            try:
                self.integer = int(self.user_game)

                if self.integer > self.number:
                    print("Demasiado alto")
                elif self.integer < self.number:
                    print("Demasiado bajo")
                elif self.integer == self.number:
                    print(f"Felicidades has encontrado el número {self.number} en {self.trys} intentos")
                    self.wins += 1
                    break

            except ValueError:
                pass

            print("")

if __name__ == '__main__':
    conn = sql.connect("logs_players.db")
    app = TheGame(conn)
