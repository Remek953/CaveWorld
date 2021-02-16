import unittest
import unittest.mock

from Character import create_name, Character

class TestName(unittest.TestCase):
	
	def test_valid_name(self):
		with unittest.mock.patch('builtins.input', return_value='Test'):
			self.assertEqual(create_name(), 'Test')


class TestsClassWarrior(unittest.TestCase):

	def setUp(self):
		self.hero = Character(	"Warrior", strength = 10, 
								agility = 10, dexterity = 10, 
								vitality = 10, defense = 10, 
								race = "None"
								)
		self.hero.warrior()

	def test_valid_warrior_strength(self):
		self.assertEqual(self.hero.strength, 11)

	def test_valid_warrior_defense(self):
		self.assertEqual(self.hero.defense, 11)

	def test_valid_warrior_get_attack(self):
		self.assertLessEqual(self.hero.get_attack(), (self.hero.base_attack + self.hero.strength)) and \
		self.assertGreaterEqual(self.hero.get_attack(), (self.hero.base_attack + self.hero.strength) / 2) 
		
	def test_valid_warrior_get_defense(self):
		self.assertEqual(self.hero.get_defense(), 2.2)

	def test_valid_get_hit_chance(self):
		assert 0 < self.hero.get_hit_chance() <= 10
	def test_100_get_hit_chance(self):
		self.hero.agility = 1000
		self.assertGreater(self.hero.get_hit_chance(), 10)
	def test_never_get_hit_chance(self):
		self.hero.agility = -1000
		self.assertLess(self.hero.get_hit_chance(), 10)

	def test_valid_get_evade_chance(self):
		assert 0 < self.hero.get_evade_chance() <= 10
	def test_100_get_evade_chance(self):
		self.hero.agility = 1000
		self.assertGreater(self.hero.get_evade_chance(), 10)
	def test_never_get_evade_chance(self):
		self.hero.agility = -1000
		self.assertLess(self.hero.get_evade_chance(), 10)

	def test_valid_get_critical_chance(self):
		assert 0 < self.hero.get_critical_chance() <= 10
	def test_100_get_critical_chance(self):
		self.hero.dexterity = 1000
		self.assertGreater(self.hero.get_critical_chance(), 10)
	def test_never_get_critical_chance(self):
		self.hero.dexterity = -1000
		self.assertLess(self.hero.get_critical_chance(), 10)

	def test_get_critical_dmg(self):
		self.assertLessEqual(self.hero.get_critical_dmg(), 2*(self.hero.base_attack + self.hero.strength)) and \
		self.assertGreaterEqual(self.hero.get_critical_dmg(), 2*(self.hero.base_attack + self.hero.strength) / 2) 
		


class TestsClassRogue(unittest.TestCase):

	def setUp(self):
		self.hero = Character(	"Rogue", strength = 10, 
								agility = 10, dexterity = 10, 
								vitality = 10, defense = 10, 
								race = "None"
								)
		self.hero.rogue()

	def test_valid_rogue_agility(self):
		self.assertEqual(self.hero.agility, 11)

	def test_valid_rogue_dexterity(self):
		self.assertEqual(self.hero.dexterity, 11)


class TestsClassMonk(unittest.TestCase):

	def setUp(self):
		self.hero = Character(	"Rogue", strength = 10, 
								agility = 10, dexterity = 10, 
								vitality = 10, defense = 10, 
								race = "None"
								)
		self.hero.rogue()

	def test_valid_monk_max_health(self):
		self.assertEqual(self.hero.max_health, 150)


if __name__ == "__main__":
	unittest.main()

