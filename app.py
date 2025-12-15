from flask import Flask, render_template, abort, session, redirect, url_for, request
from data.controls import get_all_controls, get_control_by_id
from data.categories import get_all_categories, get_category_by_id

app = Flask(__name__)
app.secret_key = 'azure-security-benchmark-secret-key'

@app.before_request
def before_request():
    if 'lang' not in session:
        session['lang'] = 'nl'

@app.route('/set-language/<lang>')
def set_language(lang):
    if lang in ['nl', 'en']:
        session['lang'] = lang
    return redirect(request.referrer or url_for('home'))

@app.route('/')
def home():
    lang = session.get('lang', 'nl')
    categories = get_all_categories(lang)
    return render_template('home.html', categories=categories, lang=lang)

@app.route('/category/<category_id>')
def category_detail(category_id):
    lang = session.get('lang', 'nl')
    category = get_category_by_id(category_id, lang)
    if category is None:
        abort(404)
    controls = get_all_controls(category_id, lang)
    return render_template('index.html', category=category, controls=controls, lang=lang)

@app.route('/category/<category_id>/control/<control_id>')
def control_detail(category_id, control_id):
    lang = session.get('lang', 'nl')
    category = get_category_by_id(category_id, lang)
    control = get_control_by_id(category_id, control_id, lang)
    if control is None or category is None:
        abort(404)
    return render_template('control_detail.html', category=category, control=control, lang=lang)

@app.errorhandler(404)
def page_not_found(e):
    lang = session.get('lang', 'nl')
    error_msg = "Control niet gevonden" if lang == 'nl' else "Control not found"
    return render_template('base.html', error=error_msg, lang=lang), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
