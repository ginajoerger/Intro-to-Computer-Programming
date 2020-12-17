# Here is how you compute the time difference in seconds. 
#----------------------------------------------------------------
#----------------------------------------------------------------
from datetime import datetime

enter_t = input('Enter time (format YYYY-MM-DD HH:MM:SS): ')
exit_t = input('Enter time (format YYYY-MM-DD HH:MM:SS): ')

parking_t = datetime.strptime(exit_t, '%Y-%m-%d %H:%M:%S') - \
	datetime.strptime(enter_t, '%Y-%m-%d %H:%M:%S')
parking_t = int(parking_t.total_seconds())
#------------------- END of example -----------------------------
#----------------------------------------------------------------

