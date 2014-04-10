#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import fileinput 
import test

def exportTest():
	print ("exporting")

def importTest():
	print ("importing")
	with fileinput.input(files=("practiceTest.txt", "practiceTest1.txt")) as f:
		questions = False
		readingQuestion = False
		readMultiupleChoice = False
		question = ''
		multipleChoice = []
		header = ''
		questionList = []
		for line in f:
			if not questions:
				if line.startswith('1.'):
					questions = True
				else:
					#all of the header crap about the test
					header += line

			if questions:
				if line.startswith(' '):
					continue
				if line.startswith('a.'):
					readingQuestion = False
					readMultiupleChoice = True

				if line[0].isdigit():
					readingQuestion = True
					readMultiupleChoice = False

				if line.startswith('answer:'):
					readMultiupleChoice = False
					readingQuestion = False
					answer = line[7:]
					questionList.append(test.Question(question, answer, multipleChoice))
					question = ''
					answer = ''
					multipleChoice = []
					continue

				if readingQuestion:
					# strip the number off the begining 
					question += line[3:] #for single digit numbers this produces a space in front 

				if readMultiupleChoice:
					if not line.startswith('\n'):
						# strip the letter off of the multiple choice
						multipleChoice.append(line[3:])
						
		print (len(questionList))
		print ('questions list')
		for q in questionList:
			print (q.question,q.multipleChoice,q.answer)


def combineTests():
	print ("combineTests")


importTest()
