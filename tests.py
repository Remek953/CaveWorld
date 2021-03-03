from unittest import TestCase, mock

import unittest
import unittest.mock
from mock import Mock

from Character import create_name, Character, choose_race
from Enemy import Orc, Skeleton, Bat, Ant, Scorpion


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
		self.assertLess(self.hero.get_hit_chance(), 1)

	def test_valid_get_evade_chance(self):
		assert 0 < self.hero.get_evade_chance() <= 10
	def test_100_get_evade_chance(self):
		self.hero.agility = 1000
		self.assertGreater(self.hero.get_evade_chance(), 10)
	def test_never_get_evade_chance(self):
		self.hero.agility = -1000
		self.assertLess(self.hero.get_evade_chance(), 1)

	def test_valid_get_critical_chance(self):
		assert 0 < self.hero.get_critical_chance() <= 10
	def test_100_get_critical_chance(self):
		self.hero.dexterity = 1000
		self.assertGreater(self.hero.get_critical_chance(), 10)
	def test_never_get_critical_chance(self):
		self.hero.dexterity = -1000
		self.assertLess(self.hero.get_critical_chance(), 1)

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
		self.hero.monk()

	def test_valid_monk_max_health(self):
		self.assertEqual(self.hero.max_health, 180)


class TestsRaceStats(unittest.TestCase):

	def setUp(self):
		self.human = {'strength': 20, 'agility': 15, 
					'dexterity': 15, 'vitality': 15, 
					'defense': 15, 'race': 'human'}

		self.orc = {'strength': 30, 'agility': 10, 
					'dexterity': 10, 'vitality': 20, 
					'defense': 20, 'race': 'orc'}

		self.elf= { 'strength': 10, 'agility': 30, 
					'dexterity': 10, 'vitality': 25, 
					'defense': 15, 'race': 'elf'}

		self.fairy = {  'strength': 10, 'agility': 20, 
						'dexterity': 30, 'vitality': 20, 
						'defense': 10, 'race': 'fairy'}

	def test_human_stats(self):
		with unittest.mock.patch('builtins.input', return_value='human'):
			self.assertEqual(choose_race(), self.human)

	def test_orc_stats(self):
		with unittest.mock.patch('builtins.input', return_value='orc'):
			self.assertEqual(choose_race(), self.orc)

	def test_elf_stats(self):
		with unittest.mock.patch('builtins.input', return_value='elf'):
			self.assertEqual(choose_race(), self.elf)

	def test_fairy_stats(self):
		with unittest.mock.patch('builtins.input', return_value='fairy'):
			self.assertEqual(choose_race(), self.fairy)

class TestsMonster(unittest.TestCase):

	def setUp(self):
		self.orc = {'name': 'orc', 'base_attack': 50, 'defense': 25, 
		'max_health': 250, 'health': 250,  'critical_chance': 6, 
		'hit_chance': 9, 'evade': 3, 'points':10}

		self.bat = {'name': 'bat', 'base_attack': 20, 'defense': 5, 
		'max_health': 100, 'health': 100,  'critical_chance': 4, 
		'hit_chance': 9, 'evade': 5, 'points':2}

		self.skeleton = {'name': 'skeleton', 'base_attack': 35, 'defense': 10, 
		'max_health': 200, 'health': 200,  'critical_chance': 5, 
		'hit_chance': 9, 'evade': 2, 'points':5}

		self.ant = {'name': 'giant ant', 'base_attack': 40, 'defense': 25, 
		'max_health': 350, 'health': 350,  'critical_chance': 4, 
		'hit_chance': 9, 'evade': 4, 'points':8}

		self.scorpion = {'name': 'deadly scorpion', 'base_attack': 70, 'defense': 5, 
		'max_health': 100, 'health': 100,  'critical_chance': 7, 
		'hit_chance': 9, 'evade': 8, 'points':6}

	def test_orc_stats(self):
		self.assertEqual(vars(Orc()), self.orc)

	def test_bat_stats(self):
		self.assertEqual(vars(Bat()), self.bat)

	def test_skeleton_stats(self):
		self.assertEqual(vars(Skeleton()), self.skeleton) 

	def test_ant_stats(self):
		self.assertEqual(vars(Ant()), self.ant)

	def test_scorpion_stats(self):
		self.assertEqual(vars(Scorpion()), self.scorpion) 


if __name__ == "__main__":
	unittest.main()

