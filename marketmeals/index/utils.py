



from datetime import datetime, timezone



html = 'templates'



def get_now( ):
	return lambda : datetime.now( timezone.utc )



