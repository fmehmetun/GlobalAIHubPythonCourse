# 1 - Login system

# User records in dict
users_dict = {
	"fmehmetun": "verysimplepassword",
	"user42": "notsosimplepassword",
	"anon": "y0uc4nN0tpWnTh!s"
}

print("[*] Type 'exit' for exiting..")

while True:
	# Get username
	username = input("[*] Username: ")

	if username == "exit":
		print("[*] Exiting..")
		break

	# Check if user exists
	if username in users_dict:
		# Get&check password for user
		password = input("[*] Password: ")
		if password == users_dict[username]:
			print("[+] Login successful, welcome %s." % (username))
			break
		else:
			print("[x] Invalid password for user %s.\n" % (username))
	else:
		print("[x] User %s doesn't exist.\n" % (username))
