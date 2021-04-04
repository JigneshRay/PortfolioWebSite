from flask import Blueprint, Flask, g, jsonify, render_template, request, Response, redirect, url_for, send_from_directory
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
#import helper
import os

# Configure application
app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    # default language for my website
    lang = 'en'

    return redirect(url_for('index_en',
                                 lang=lang))


@app.route('/en/index', methods=['POST', 'GET'])
@app.route('/en/', methods=['POST', 'GET'])
def index_en(lang=None):
    lang = 'en'
    title_text = 'Hi!! I enjoy working with computers and people to solve problem for business. Currently working with Medicare Products and learning to do analysis with Python.'
    #helper.get_title_content('index', lang)

    return render_template('index.html',
                                title_text=title_text,
                                title="User - Data - Analysis - Product",
                                id="index",
                                lang=lang)

@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():

    # default language if just portfolio is entered in url
    lang = 'en'

    return redirect(url_for('portfolio_en',
                                 lang=lang))


@app.route('/en/portfolio', methods=['POST', 'GET'])
def portfolio_en():
    lang ='en'


    # get all projects from the database
    #zipped = helper.get_portfolio_content(lang)

    # get the title content for the portfolio page
    #title_text = helper.get_title_content('portfolio', lang)

    return render_template('/portfolio.html',
                            title_text=title_text,
                            title="PROJECT PORTFOLIO",
                            id="portfolio",
                            projects=zipped,
                            lang=lang)


@app.route('/about', methods=['POST', 'GET'])
def about():

    # default language if user enters about without language preference in url
    lang = 'en'

    return redirect(url_for('about_en',
                             lang=lang))


@app.route('/en/about', methods=['POST', 'GET'])
def about_en():

    lang = 'en'

    title_text = 'I started my career as Software developer, progressing into Tech lead and Product Management now.'
    #helper.get_title_content('about', lang)

    skills = 'Skills'
    #helper.get_skill_content(lang)

    return render_template('/about.html',
                            title_text=title_text,
                            skills=skills,
                            title="Professional Journey",
                            id="about",
                            lang=lang)



@app.route('/jigneshray', methods=['POST', 'GET'])
def jigneshray():

    lang = 'en'

    return redirect(url_for('jigenshray_en',
                             lang=lang))


@app.route('/en/jigneshray', methods=['POST', 'GET'])
def jigenshray_en():

    lang = 'en'

    address_one, address_two, email = 'email jignesh'
    #helper.get_privacy_legal_notice()

    return render_template('/jigenshray.html',
                            title="",
                            address_one=address_one,
                            address_two=address_two,
                            email=email,
                            id="index",
                            lang=lang)



@app.route("/robots.txt")
def robots():
    '''
    Add robots.txt file to avoid google indexing
    '''

    return send_from_directory(app.static_folder, request.path[1:])