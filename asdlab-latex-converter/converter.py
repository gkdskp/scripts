import sys
import re

no_of_qstns = sys.argv[2]
question_num = sys.argv[3]

with open(sys.argv[1], 'r') as sql_file:
	s = sql_file.readlines()

questions = []
answers = []

i = 0
if s[0] == "/*\n":
	while(s[i] != "*/\n"):
		questions.append(s[i])
		i += 1
answers = s[i+1:]

questions = " ".join(questions).replace("\n", "newlinechar")
questions_list = []

for i in range(1, int(no_of_qstns)+1):
	reg = re.compile(rf'(?<={i}\.\s)(.*?)(?={i+1}\.)') if i < int(no_of_qstns) else re.compile(rf'(?<={i}\.\s)(.*)')
	mo = reg.search(questions)
	if(mo):
		questions_list.append(mo.group(0).replace("newlinechar", "\n"))
	else:
		print(f"Pattern does not match for {i}th question")
		if i != no_of_qstns:
			print(
				"Please check that the question is present in the format" \
				f"{i}.[space] and there exists a {i+1}."
			)
		else:
			print(f"Please check whether question exist in the format {i}.[space]")

answers_list = []
temp_string = ""
for i in answers:
	if i == "\n":
		if temp_string:
			answers_list.append(temp_string)
		temp_string = ""
		continue
	else:
		temp_string += i

if(temp_string):
	answers_list.append(temp_string)

if(len(answers_list) != int(no_of_qstns)):
	print("Answers List: ")
	for i in range(0, len(answers_list)):
		print(f"Answer {i+1}:\n{answers_list[i]}")
	
	print("Mismatch between question number and answer number")
	print("All the detected answers are printed above")
	print("If the missing answer is for last question try adding two empty lines after")
	exit(0)

for i in range(int(no_of_qstns)):
	print(f"""
\item
{questions_list[i]}
Syntax:
\\begin{{verbatim}}
{answers_list[i]}
\\end{{verbatim}}
\\includegraphics[]{{img/p{question_num}/ss{i+1}.png}}
""")