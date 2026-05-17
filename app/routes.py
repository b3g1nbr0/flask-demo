from flask import Blueprint, render_template, redirect, url_for, flash, request
from .forms import PromptForm, ContactForm
from .promptgen import generate_prompt

main = Blueprint('main', __name__)

@main.app_errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/generator', methods=['GET', 'POST'])
def generator():
    form = PromptForm()
    prompt = None
    if form.validate_on_submit():
        prompt = generate_prompt(form)
        flash('Prompt berhasil dibuat!','success')
    return render_template('generator.html', form=form, prompt=prompt)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact', methods=['GET','POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Pesan Anda telah dikirim. Terima kasih!', 'success')
        return redirect(url_for('.contact'))
    return render_template('contact.html', form=form)

@main.route('/privacy')
def privacy():
    return render_template('privacy.html')

@main.route('/terms')
def terms():
    return render_template('terms.html')
