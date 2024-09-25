from flask import render_template
from . import main_bp

@main_bp.route('/')
def index():
    return 'Hola pagina principal'

@main_bp.route('/modelo')
def modelo():
    return 'modelo'