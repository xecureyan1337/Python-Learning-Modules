import subprocess

# initialize the command
command = ['curl', 'https://httpbin.org']

#run the command
res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

#get the output and error msg (if any)
output = res.stdout
err = res.stderr

#validation
if res.returncode == 0:
    print("Success: ", end=" ")
    # print(output)
else:
    print("Error: ", end=" ")
    # print(err)