class cookie:

	def __init__(self, name, grade, level, skillname):
		self.name = name
		self.grade = grade
		self.level = level
		self.skillname = skillname

	def info(self):
		print(f'이름 :  {self.name}')
		print(f'등급 : {self.grade}')
		print(f'레벨 : {self.level}')
		print(f'스킬 이름 : {self.skillname}')
		print()


kingdom1 = cookie("용감한 쿠키", "COMMON", 18, "공격")
kingdom2 = cookie("당근맛 쿠키", "RARE", 35, "치명타 공격")
kingdom3 = cookie("라떼맛 쿠키", "EPIC", 44, "침묵")
kingdom4 = cookie("퓨어바닐라 쿠키", "ANCIENT", 56, "회복")

kingdom1.info()
kingdom2.info()
kingdom3.info()
kingdom4.info()





