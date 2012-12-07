import sys
import string

users = ["faustine", "kevin cahyadi", "denny", "kevin sugi"]

def readFloat(prompt):
	# The float value read
	data = 0.0
	# Prompt whether the value is good
	confirm = ""
	print "\tEnter " + prompt + ": "
	while True:
		try:
			data = float(sys.stdin.readline())
			print str(data) + "? enter [ok] to continue"
			confirm = sys.stdin.readline()
			if (confirm != "ok\n"):
				print "Re-enter the value:"
				continue
			print "\n\t --- " + string.upper(prompt) + " = " + str(data) + " --- \n"
			return data
		except ValueError:
			print "Invalid input, try again :"
			

def main():
	shared_bill = 0.0
	individual_bill = {}
	total_bill = 0.0
	for user in users:
		individual_bill[user] = 0.0
		print "Entering data for " + string.upper(user)
		print "_______________________________"
		shared_bill += readFloat("Shared (CALL)")
		shared_bill += readFloat("Shared (TEXT)")
		individual_bill[user] += readFloat("Individual (DATA)")
		shared_bill += readFloat("Shared (TAX)")
		individual_bill[user] += readFloat("Individual (TAX)")
		#print value
	
	print "--- FINAL CHARGE ----"
	total_bill += shared_bill
	for user in users:
		total_bill += individual_bill[user]
		print string.upper(user) + " = " + str(individual_bill[user] + shared_bill / len(individual_bill))
	
	print "\nTotal Bill: " + str(total_bill)
	
main()