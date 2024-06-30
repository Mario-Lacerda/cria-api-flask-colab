# Desafio Dio - **Criando uma API com Flask no Ambiente COLAB**



Neste projeto, criaremos uma API RESTful simples usando Flask no Ambiente COLAB. A API permitirá que os usuários gerenciem tarefas, incluindo criar, ler, atualizar e excluir tarefas.



### **Pré-requisitos**

- Conta do Google
- Acesso ao Google COLAB
- Conhecimento básico de Python



### **Passos**



### **1. Criar um Novo Notebook do COLAB**



- Acesse o Google COLAB em https://colab.research.google.com/.
- Clique em "Novo Notebook".



### **2. Instalar o Flask**



- No notebook, execute o seguinte comando para instalar o Flask:

plaintext



```plaintext
!pip install Flask
```



### **3. Importar o Flask**



- Importe o Flask no seu notebook:

python



```python
from flask import Flask, request, jsonify
```



### **4. Criar o Aplicativo Flask**



- Crie uma instância do aplicativo Flask:

python



```python
app = Flask(__name__)
```



### **5. Definir Rotas**

- Defina as rotas para os métodos CRUD (Criar, Ler, Atualizar, Excluir) da API:

python



```python
# Rota para criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = Task(data['title'], data['description'])
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Tarefa criada com sucesso'}), 201

# Rota para obter todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify({'tasks': [task.to_dict() for task in tasks]})

# Rota para obter uma tarefa específica
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message': 'Tarefa não encontrada'}), 404
    return jsonify(task.to_dict())

# Rota para atualizar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message': 'Tarefa não encontrada'}), 404
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Tarefa atualizada com sucesso'})

# Rota para excluir uma tarefa
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message': 'Tarefa não encontrada'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Tarefa excluída com sucesso'})
```



### **6. Executar o Aplicativo**

- Execute o aplicativo Flask no Ambiente COLAB:

plaintext



```plaintext
app.run()
```



### **Teste da API**

- Use ferramentas como Postman ou cURL para testar a API:
- **Criar uma tarefa:**

plaintext



```plaintext
curl -X POST -H "Content-Type: application/json" -d '{"title": "Tarefa 1", "description": "Descrição da Tarefa 1"}' http://localhost:5000/tasks
```



- **Obter todas as tarefas:**

plaintext



```plaintext
curl http://localhost:5000/tasks
```



- **Obter uma tarefa específica:**

plaintext



```plaintext
curl http://localhost:5000/tasks/1
```



- **Atualizar uma tarefa:**

plaintext



```plaintext
curl -X PUT -H "Content-Type: application/json" -d '{"title": "Tarefa 1 Atualizada", "description": "Descrição da Tarefa 1 Atualizada"}' http://localhost:5000/tasks/1
```



- **Excluir uma tarefa:**

plaintext



```plaintext
curl -X DELETE http://localhost:5000/tasks/1
```



### **Conclusão**



Neste projeto, criamos uma API RESTful simples com Flask no Ambiente COLAB. A API permite que os usuários gerenciem tarefas usando os métodos CRUD. Isso demonstra o poder e a facilidade de uso do Flask para criar APIs no Ambiente COLAB.

