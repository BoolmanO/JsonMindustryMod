

import json #необходим для создания json
import time #не необходим,нужен для подсчета времени
import os #необходим для создания архитектуры

from dataclasses import dataclass

#Функция для логирования
def log(string,logType="error"):
	print("[{:} LOG AT {:.5f}], {:}".format(logType.upper(),time.time()-start,string))
start = time.time()

class JsonAutoConfException:
	"""Errno 17 обозначает то, что файл уже был создан ранее"""

class JsonAutoConfVersion:
	"""Класс для хранения версии КОНФИГУРАТОРА архитектуры"""
	version = "1.0.0"
	def __str__(self): return self.version

@dataclass
class JsonAutoConfData:
	"""Класс для хранения данных"""
	name : str
	displayName : str
	author : str
	description : str
	version : str
	minGameVersion : str
	dependencies : list or None
	hiden : bool	
	"""Это аннотация типов, то есть предполагаемый тип данных переменной"""

class JsonAutoConf(JsonAutoConfData):
	"""Этот класс создает архитектуру  моддинга"""
	
	
	#функция для более простого создания папки
	#принимает в аргументы имя папки, и булево значение которое определяет, спускаться в эту папку или нет
	@staticmethod
	def create_folder(name : str,change_dir : bool =False):
			try:
				os.mkdir(name)
				log(f"Создание папки {name}...","ok")
			except Exception as error:
				log(error)
			if change_dir:
				os.chdir(name)
				log(f"Переход в папку {name}...","ok")
	
	
	def create_projectFolder(self):
		self.create_folder(self.name,True)
	
	#Создание modjson файла
	def create_modjson(self):
		
		if self.dependencies is None:
			self.dependencies = []
		
		to_json = {
		"name" : self.name,
		"displayName" : self.displayName,
		"author" : self.author,
		"description" : self.description,
		"version" : self.version,
		"minGameVersion" : self.minGameVersion,
		"dependencies" : self.dependencies,
		"hiden" : self.hiden
		}
		
		try:
			with open('mod.json',"x") as file:
				file.write(json.dumps(to_json))
				log("Создание modjson...","ok")
		except Exception as error:
			log(error)
				
					
	def create_mod_folders(self):
		to_create_1 = ["maps","bundles","sounds","schematics","scripts","sprites-override","sprites"]
		to_create_2 = ["items","blocks","liquids","units"]
		for folder in to_create_1:
			self.create_folder(folder)
			
		#создание папки content
		
		self.create_folder("content",True)
		
		for folder in to_create_2:
			self.create_folder(folder)

												
def main():
	conf = JsonAutoConf("name","displayName","author","description","version","MinGameVersion",None,False) #предпоследнее - dependecies,последнее - hiden
	
	#создание проектной папки
	conf.create_projectFolder()
	#создание mod.json
	conf.create_modjson()
	#создание папок с контентом
	conf.create_mod_folders()
	log(":З","end")
	print(JsonAutoConfVersion())
	print("Пожелания: discord: BoolmanO#3605, gmail: ponos585858@gmail.com")
if __name__ == "__main__":
	main()
	

