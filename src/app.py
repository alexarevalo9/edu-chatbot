from flask import Flask, request
import wolframalpha
from twilio.twiml.messaging_response import MessagingResponse

API_WOLFRAM_KEY = '{API_WOLFRAM_KEY}'

app = Flask(__name__)
client = wolframalpha.Client(API_WOLFRAM_KEY)


@app.route('/')
def main():
    return 'Hello from ChatBot'


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    appendres = ''

    # Wolfram API
    try:
        res = client.query(str(incoming_msg))

        if res['@success']:
            for pod in res.pods:
                if(pod.text):
                    appendres += pod.text + '\n'

        if(len(appendres) > 1600):
            msg.body('Resultado:'+'\n'+appendres[:1500])
        else:
            msg.body('Resultado:'+'\n'+appendres)

        appendres = ''

    except Exception:
        msg.body('Lo sentimos no logramos obtener un resultado intentelo de nuevo')
    except:
        msg.body("Algo ha salido mal en el servidor")

    return str(resp)


if __name__ == '__main__':
    app.run()
