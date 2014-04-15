def inportTest 
	puts "importing"

	File.open("practiceTest.txt", "r") do |file|

		questions = false 
		readingQuestion = false
		readMultipleChoice = false
		questionsList = []
		header = "" 
		question = ""
		while (line = file.gets)
			if !questions					
				if line.start_with?("1.")
					questions = true
				else
					header = header + line
				end
			end

			if questions
				if line.start_with?(" ")
					next
				end
				if line.start_with?("a.")
					readingQuestion = false
					readMultipleChoice = true
				end
				#puts "#{line[0,1]}"
				if line.start_with?("1.") 	#(line[0,1])					
					readingQuestion = true
					readMultipleChoice = false
				end
				if line.start_with?("answer:")		
					readMultipleChoice = false
					readingQuestion = false

					next
				end
				if readingQuestion
					question = question + line
				end

				# if readMultipleChoice
				# 	unless line.start_with?("\n")
						
			end

		end
	end
end


if __FILE__ == $0
	inportTest

end 