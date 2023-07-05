# -*- coding: utf-8 -*-
"""
Created on Tue May 03 13:12:18 2016

@author: tih
@changed at 30-06-2020-Urmia Lake Basin: ahowlia@gmail.com
"""

import SEBAL

inputExcel =  r"D:\MPySEB_Ex\Owlia-Developed.xlsx"

RunLineStart = 2   #Run number owlia
RunLineEnd = 2

for number in range(RunLineStart+1,RunLineEnd+2):
	
		SEBAL.pySEBAL.pySEBAL_code.main(number,inputExcel)
		#print('%s'%startline,' out of %s'%endline, 'completed')


