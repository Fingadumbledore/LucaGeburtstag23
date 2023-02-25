""" Flask app for the application. """

import json
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
