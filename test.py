import brawlstats
from TOKEN import TOKEN
import sqlite3

with sqlite3.connect("database.db") as db:
	cursor = db.cursor()
	query = """CREATE TABLE IF NOT EXISTS users(
			id INTEGER PRIMARY KEY,
			teg VARCHAR(20),
			login VARCHAR
	)
	"""
	cursor.executescript(query)


client = brawlstats.Client(TOKEN)

def registration():
	teg = input("Введите свой тег: ")
	login = input("Введите свой логин: ")
	try:
		player = client.get_profile(teg)
		db = sqlite3.connect("database.db")
		cursor = db.cursor()

		cursor.execute("SELECT login FROM users WHERE login = ?",[login])
		if cursor.fetchone() is None:
			values = [teg, login]
				
			cursor.execute("INSERT INTO users(teg, login) VALUES(?,?)", values)
			db.commit()
		else:
			print("Такой логин уже существует")
			print("Еще раз:")
			registration()


	except sqlite3.Error as e:
		print("Error:",e)
	except brawlstats.errors.NotFoundError as err:
		print("Вы ввели не правильно свой тег:")
		registration()

	finally:
		cursor.close()
		db.close()

def profile_():
	login = input("Введите свой логин: ")

	try:
		db = sqlite3.connect("database.db")
		cursor = db.cursor()

		cursor.execute("SELECT login FROM users WHERE login = ?",[login])
		if cursor.fetchone() is None:
			print("Такого логина не существует")
			profile_()
		else:
			cursor.execute("SELECT teg FROM users WHERE login = ?", [login])

			TEG = cursor.fetchone()[0]
			player = client.get_profile(TEG)
			print(f"У вас {player.trophies} трофеев")
			db.commit()

	except sqlite3.Error as e:
		print("Error", e)
	finally:
		cursor.close()
		db.close()

def pro_change():
	login = input("Введите свой логин: ")
	new_teg = input("Введите свой новый тег: ")

	try:
		player = client.get_profile(new_teg)
		db = sqlite3.connect("database.db")
		cursor = db.cursor()

		cursor.execute("SELECT login FROM users WHERE login = ?",[login])
		if cursor.fetchone() is None:
			print("Такого логина не существует")
		else:
			cursor.execute("UPDATE users SET teg = ? WHERE login = ?", [new_teg,login])
			cursor.execute("SELECT teg FROM users WHERE login = ?", [login])

			TEG = cursor.fetchone()[0]
			player = client.get_profile(TEG)
			print(f"У вас {player.trophies} трофеев\n"
				"Это вы ?")
			db.commit()



	except sqlite3.Error as e:
		print("Error:",e)
	except brawlstats.errors.NotFoundError as err:
		print("Вы ввели не правильно свой тег:")

action = int(input("Что хотите делать?\n"
					"1 - За регистрироваться\n"
					"2 - За логинется\n"
					"3 - поменять свой тег\n"))
while True:
	if action == 1:
		registration()
	elif action == 2:
		profile_()
	elif action == 3:
		pro_change()
	action = int(input("Что хотите делать?\n"
					"1 - За регистрироваться\n"
					"2 - За логинется\n"
					"3 - поменять свой тег\n"))





# TEG = "28GQVQJQY"

# # "28GQVQJQY" - мой тег

# player = client.get_profile(TEG)
# print(player)



# print(f"У вас {player.trophies} трофеев")
# if club is not None:
# 	print(f"Вы в клубе: {club.name}")
# else:
# 	print("Вы не состоите в клубе")




# try:
# 	player = client.get_profile(TEG)
# 	print(f"У вас {player.trophies} трофеев")

# except brawlstats.errors.NotFoundError as e:
# 	print("Вы ввели не правильно свой тег") 
