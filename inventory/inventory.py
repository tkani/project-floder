# SWAMI KARUPPASWAMI THUNNAI
from flask import send_file
from datetime import date, timedelta
import hashlib
from flask import request, redirect, url_for, session,flash
from flask import render_template
from flask import Blueprint
import jwt
import random
import string
import os
from io import BytesIO
from database.get_connection import get_connection
from inventory.token_validator import get_inventory_token, inventory_token

#salt
salt='jeeva$kani*vichu&69'
salt=hashlib.sha512(salt.encode("utf-8")).hexdigest()
#===============================================================================# Starts #========================================  


inventory = Blueprint("inventory", __name__, url_prefix="/")

today=date.today()

@inventory.route("/")
def render_login():

	return render_template("inventory/addsite.html")