#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from scriptLanguageBuilder import ScriptLanguageBuilder

class PhpBuilder(ScriptLanguageBuilder):
	
	def name(self):
		return "PHP builder"

	
	def relativePath(self):
		return 'php'
