



def extract_relevant_parts(line):
	"""
	This fucntion takes in a line and extracts the
	year, country, income, percentage, region
	The it returns them to the client[calling code]
	"""

	# country - 50, income - 6, per - 3, region 25, year - 4

	# Afghanistan          WB_LI   11 Eastern Mediterranean     1980



	# 1.get year- find space begining from the right
	year_part = line[line.rfind(" ")+1:].strip()

	# according to the rules in the project - country takes
	# first 50 characters - 0, 51 [sice 51 will be ignored]

	# 2. country part
	country_part = line[:51]

	#  WB_LI   11 Eastern Mediterranean
	l_w_c_y = line[51:line.rfind(year_part)].strip()

	# 3. got the income level using the line-without-country and year line
	income_level_part = l_w_c_y[:l_w_c_y.find(" ")].strip()

	# get the percentage
	# part:   11 Eastern Mediterranean
	contains_percentage = l_w_c_y[l_w_c_y.find(" ")+1:].strip()

	# 4. percentage
	percentage_part = contains_percentage[:contains_percentage.find(" ")].strip()

	# 11 Eastern Mediterranean
	# find a space from the left then slice from there up to the end
	# get perfect region by striping [remove space on either sides]

	# 5. get region
	region_part = contains_percentage[contains_percentage.find(" ")+1:].strip()

	# return the parts to the client
	return year_part, country_part, income_level_part, percentage_part, region_part


def file_processor(lookup_string, output_file):
	if lookup_string == "all":
		with open("measles.txt", "r") as measles_handle:

			with open(output_file, 'w+') as user_handle:

				# get each line in measles handle
				for line in measles_handle.readlines():

					# write the line
					user_handle.write(line)
					user_handle.write("\n")

	else:
		# with closes the file automatically
		with open("measles.txt", "r") as measles_handle:

			measles_data = measles_handle.read()

			#print(repr(measles_data))

			broken_lines = measles_data.splitlines()

			with open(output_file, "w+") as user_handle:

				# loop through all lines
				for line in broken_lines:
					year_, country_, income_, percentage_, region_ = extract_relevant_parts(line)

					# check if the year part contains the year string
					if lookup_string in year_:

						# we copy it and write it in the user file
						user_handle.write(line)

						user_handle.write("\n")

					else:
						pass


def main_function():
	valid_year = None

	# this will tell the loop that the year is valid
	year_validity = False;


	while year_validity == False:
		# get year from the user
		year_ = input("Enter year:")

		# check if year contains digits
		if year_.isdigit():

			# check if its length is 4 or less
			if len(year_) <= 4:

				# set the valid year to that yea
				valid_year = year_

				year_validity = True

			else:

				print('Error, use ["", all, ALL, or [any digits in the year] \n\n')

		else:
			if (year_ == "" or year_ == "all" or year_ == "ALL"):

				valid_year = "all"

	# get the output file

	valid_file = None

	file_validity = False

	while file_validity == False:
		# get filename
		file_name = input("Enter filename:")

		# check if it ends with .txt
		if len(file_name) > 4 and file_name.endswith(".txt"):
			valid_file = file_name

			file_validity = True

		else:
			print("Error, Filename length should 1 or more \nAnd file must end with [.txt]\n\n")

	# pass the data to the fileprocessor
	file_processor(valid_year, valid_file)



# call the main function
main_function()