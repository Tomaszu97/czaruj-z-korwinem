#! /usr/bin/env python3 
#dd
import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.pagelayout import PageLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

class MainController(PageLayout):
	atak_cyborga = SoundLoader.load('atak_cyborga.mp3')
	awaria_cybernetycznej_krtani = SoundLoader.load('awaria_cybernetycznej_krtani.mp3')
	informacja_dla_reptilianskich_zwierzchnikow = SoundLoader.load('informacja_dla_reptilianskich_zwierzchnikow.mp3')

	ladowanie_ataku_obszarowego = SoundLoader.load('ladowanie_ataku_obszarowego.mp3')
	ladowanie_mocy = SoundLoader.load('ladowanie_mocy.mp3')
	odblokowanie_5_czary = SoundLoader.load('odblokowanie_5_czary.mp3')

	okrzyk_plemienny = SoundLoader.load('okrzyk_plemienny.mp3')
	przemiana_w_jaszczura = SoundLoader.load('przemiana_w_jaszczura.mp3')
	przywolanie_bractwa_reptoidow = SoundLoader.load('przywolanie_bractwa_reptoidow.mp3')

	zaklecie_4_stron_swiata = SoundLoader.load('zaklecie_4_stron_swiata.mp3')
	zaklecie_7_kregu_magii = SoundLoader.load('zaklecie_7_kregu_magii.mp3')
	zaklecie_niewybaczalne = SoundLoader.load('zaklecie_niewybaczalne.mp3')

	yellow_submarine = SoundLoader.load('yellow_submarine.mp3')

class KorwinApp(App):
	def build(self):
		return MainController()


application = KorwinApp()
application.run()
