from flask import Flask, render_template, redirect
from modulos.DockerModulo import DockerModulo

app = Flask(__name__)

docker = DockerModulo()

@app.route('/')
def index():
    global docker
    containers = []

    for container in docker.getContainers():
        print type(container.get('Names'))
        containers.append({
            'id': container.get('Id')[:7],
            'nome': container.get('Names')[0].replace('/', '').title(),
            'status': container.get('Status')
        })

    return render_template('index.html', containers=containers)

@app.route('/container/start/<id>')
def container_start(id):
    global docker
    docker.startContainer(id)
    return redirect('/')

@app.route('/container/stop/<id>')
def container_stop(id):
    global docker
    docker.stopContainer(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)