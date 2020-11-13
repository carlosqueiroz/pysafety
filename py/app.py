#! -*- encoding:utf-8 -*-
import cherrypy
import json
import matplotlib 
matplotlib.use('Agg')

import pydicom
import matplotlib.pyplot as plt
import urllib.request
import os.path
import numpy as np
import os
import json
from pprint import pprint
import collections
import cherrypy_cors
import subprocess
from Model.rx.rx import ProcessingRx

cherrypy_cors.install()

class Root:
    #INDEX - Página inicial
    @cherrypy.expose
    def index(self):
        return file("View/index.html")

    #URL/rx  para cálculo de informações referentes ao raios-x
    @cherrypy.expose
    def rx(self, data=None):
        if data:
            #Dados Recebidos via String jSON
            d = json.loads(data)
            #Instanciando Objeto
            rx  = ProcessingRx()
            #Informações Obrigatórias
            rx.file_path = d['file_path']
            rx.wadoURL = d['files']
            rx.fantoma = d['fantoma']
            rx.cliente_id = d['cliente_id']
            rx.equipamento_id = d['equipamento_id']
            #
            retorno = rx.calculate()
            print(retorno)

            return  json.dumps(retorno)

        else:
            return "Envie informações via POST HTTP"
       
        return file("View/index.html")


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0','cors.expose.on': True})
    cherrypy.quickstart(Root())
