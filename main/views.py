#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

view = Blueprint('main', __name__)

@view.route('/', methods=['GET'])
def home():
  return render_template('home.html')

@view.route('/error/access/<code>', methods=['GET'])
def error_access(code):
  # lang = session_language(session)
  # locals_dic = { }
  # return render_template('demo/index.html', locals=locals_dic)
  return 'Recurso no encontrado', code
