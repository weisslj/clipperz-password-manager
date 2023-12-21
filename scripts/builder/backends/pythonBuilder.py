#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from scriptLanguageBuilder import ScriptLanguageBuilder

class PythonBuilder(ScriptLanguageBuilder):
	
	def name(self):
		return "Python builder"

	
	def relativePath(self):
		return 'python'
