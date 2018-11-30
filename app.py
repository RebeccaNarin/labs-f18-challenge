import requests
>>> import pykemon
>>> client = pykemon.V1Client()
>>> p = client.get_pokemon(uid=1)
[<Pokemon - Bulbasaur>]

#using json
#Get parameters for the //
response = 
request.get("http://pokeapi.co/api/v2/pokemon/", response)

response.data


@app.route('/', methods=['GET'])

@app.route('/pokemon'
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
