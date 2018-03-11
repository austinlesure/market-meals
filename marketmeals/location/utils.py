



from marketmeals import db
from marketmeals.location.models import Market



html = 'templates'


def urlify( label ):
	url = ''
	for char in label:
		if char.isalnum( ):
			if char.isupper( ):
				url += char.lower( )
			else:
				url += char
		elif char.isspace( ):
			url += '-'
	return url


def catalog( name, url, addresses ):
	street = ''
	city = ''
	state = ''
	zipcode = None
	for sub in addresses:
		for area in sub[ 'types' ]:
			if area == 'street_number':
				street = sub[ 'short_name' ] + ' '
			## Some markets don't have route strings provided
			elif area == 'route':
				street += sub[ 'short_name' ]
			elif area == 'locality':
				city = sub[ 'short_name' ]
			elif area == 'administrative_area_level_1':
				state = sub[ 'short_name' ]
			elif area == 'postal_code':
				zipcode = sub[ 'short_name' ]
	market = Market( name = name, url = url, address_1 = street, city = city, state = state, zip_code = zipcode )
	return market


