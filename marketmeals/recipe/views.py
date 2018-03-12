



from marketmeals.recipe.utils import html
from flask import Blueprint, render_template



recipe = Blueprint( 'recipe', __name__, template_folder = html )



@recipe.route( '/recipe', methods = [ 'GET' ] )
def cuisine( ):
	return render_template( 'recipe/recipe.html' )



