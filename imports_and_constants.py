import os
from flask import Flask, redirect, url_for, request
from flask import render_template
from flask import session
from flask import jsonify
# import mysql.connector
from dotenv import load_dotenv
load_dotenv()

# Secret key setting from .env for Flask sessions
SECRET_KEY = os.environ.get('SECRET_KEY')