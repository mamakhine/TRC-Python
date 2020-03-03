import sys
import time

f = None
try:
	f = open("poem.txt")

	#Our usual file reading idiom

	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print(line, end='')
		sys.stdout.flush()
		print("press ctrl+c now")

		# to make sure it runs for a while

		time.sleep(2)

except IOError:

		print('Could not find file open.txt')

except KeyboardInterrupt:
		print("!! You cancelled the reaading from the file.")

finally:
		if f:
			f.close()
		print('(Cleaning up. Close the file)')