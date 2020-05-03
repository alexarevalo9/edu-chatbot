# ChatBot :pencil::iphone:

Chatbot es un proyecto de apoyo didáctico para niños y adolescentes que permite realizar preguntas de matemáticas y de 
cultura general a través de WhatsApp para lo cual ChatBot está integrado con la API de mensajería de [Twilio](https://github.com/twilio/twilio-python) y el buscador de respuestas 
de [WolframAlpha](https://products.wolframalpha.com/api/)

<div>
<img src="https://user-images.githubusercontent.com/46785980/80919696-172d9a80-8d31-11ea-9386-5581c0dc9f23.jpg" width=380 height=550>
<img src="https://user-images.githubusercontent.com/46785980/80919794-97540000-8d31-11ea-97dd-2866a19629d3.jpg" width=380 height=550>
</div>

## Instalación 

Preparamos el entorno virtual, permitirá que la aplicación se ejecute aislada del entorno del servidor global:

```bash
$ pip install virtualenv
$ virtualenv --python=python3 ChatBot
$ cd /ChatBot
$ source bin/activate
```
Instalamos las dependencias que se encuentran en el archivo [requirements.txt](requirements.txt) 

```bash
$ pip install -r requirements.txt
```
Para hacer un test ejecutamos el siguiente comando:
```bash
$ python run.py
```
Para utilizar la API de [Twilio](https://github.com/twilio/twilio-python) se necesita una cuenta y configurar 
el Sandbox de Twilio que se encuentra en la [documentación](https://www.twilio.com/docs/autopilot/channels/whatsapp)

Finalmente, para utilizar los servicios de [WolframAlpha](https://products.wolframalpha.com/api/) necesitamos crear una cuenta y obtener
una [AppID](https://products.wolframalpha.com/short-answers-api/documentation/) la cual se deberá colocar en el archivo [__init.py__](app/__init__.py)

## Licencia
MIT License Copyright (c) 2020 Alex Arévalo. Es software libre y puede redistribuirse bajo los términos especificados en el archivo [LICENSE](LICENSE).
