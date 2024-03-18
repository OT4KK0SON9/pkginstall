import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""_____

1.kecil
2.sedang
3.full
4.backup
- selamat puasa -
____""")
		pilih=int(input('Otak Kosong > '))
		if pilih == 1:
			import src.kecil
		elif pilih == 2:
			import src.sedang
		elif pilih == 3:
			import src.full
	        elif pilih == 4:
			import src.backup
		else: print("[!] Ngasal Jir(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] -->')
except Exception as F:
	print('Err: %s'%(F))
