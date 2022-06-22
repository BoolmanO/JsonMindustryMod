import json # необходим для создания json
import time # нужен для подсчета времени
import os # необходим для создания архитектуры

from dataclasses import dataclass


def log(string,logType="error"):
	print("[{:} LOG AT {:.5f}], {:}".format(logType.upper(),time.time() - start, string))

class JsonAutoConfException:
	"""Errno 17 обозначает то, что файл уже был создан ранее"""

class JsonAutoConfVersion:
	"""Класс для хранения версии КОНФИГУРАТОРА архитектуры"""
	version = "1.1.0"
	def __str__(self): 
		return self.version

@dataclass
class JsonAutoConfData:
	"""
		Класс для хранения данных
		Это аннотация типов, то есть предполагаемый тип данных переменной
	"""
	name: str
	displayName: str
	author: str
	description: str
	version: str
	minGameVersion: str
	dependencies: list | None
	hiden: bool	

class JsonAutoConf(JsonAutoConfData):
	"""Этот класс создает архитектуру  моддинга"""
	
	#функция для более простого создания папки
	#принимает в аргументы имя папки, и булево значение которое определяет, спускаться в эту папку или нет
	@staticmethod
	def create_folder(name: str):
			try:
				os.makedirs(name, exist_ok=True)
				log(f"Создание папки {name}...","ok")
			except Exception as error:
				log(error)
	
	def setup(self):
		"""
			Создаёт все требуемые папки.
		"""
		self.create_projectFolder()
		self.create_modjson()
		self.create_mod_folders()
		self.create_mod_folders()

	def create_projectFolder(self):
		self.create_folder(self.name)
	
	def create_modjson(self):
		if self.dependencies is None:
			self.dependencies = []
		
		to_json = {
			"name": self.name,
			"displayName": self.displayName,
			"author": self.author,
			"description": self.description,
			"version": self.version,
			"minGameVersion": self.minGameVersion,
			"dependencies": self.dependencies,
			"hiden": self.hiden
		}
		
		try:
			with open(os.path.join(self.name, "mod.json"), "x") as file:
				file.write(json.dumps(to_json))
			log("Создание modjson...", "ok")
		except Exception as error:
			log(error)
				
					
	def create_mod_folders(self):
		for folder in (
			"maps", "bundles", "sounds", "schematics", "scripts", "sprites-override", "sprites", 
			"content/items", "content/blocks", "content/liquids", "content/units"
		):
			self.create_folder(os.path.join(self.name, folder))

												
def main():
	conf = JsonAutoConf("name","displayName","author","description","version","MinGameVersion",None,False) #предпоследнее - dependecies,последнее - hiden
	conf.setup()
	log(":З","end")
	print(JsonAutoConfVersion())
	print("Пожелания: discord: BoolmanO#3605, gmail: ponos585858@gmail.com")

if __name__ == "__main__":
	start = time.time()
	main()
