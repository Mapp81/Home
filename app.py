from flask import Flask, render_template, url_for, redirect, request, flash
import os
import json
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models import db, Post, Task
from flask_migrate import Migrate
from form import Formulario  # Asegúrate de tener un archivo forms.py con la clase Formulario definida
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()



app = Flask(__name__)
app.secret_key = 'clave-secreta'  # Necesaria para usar flash

app.config['SECRET_KEY'] = 'Isabella13'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form.get('full-name')
        email = request.form.get('email')

        archivo = 'subs.json'

        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                subs = json.load(f)
        else:
            subs = []

        subs.append({'name': nombre, 'email': email})

        with open(archivo, 'w') as f:
            json.dump(subs, f, indent=2)

        flash('¡Gracias por suscribirte, {}!'.format(nombre))
        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/about')
def about():
        return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
        task = Task.query.all()
        return render_template('contact.html', formulario=Formulario(), task=task, send=url_for('send'))

@app.route('/send', methods=['POST'])
def send():
        formulario = Formulario()
        if formulario.validate_on_submit():
            try:
                t = Task(name=formulario.name.data, email=formulario.email.data, message=formulario.message.data)
                db.session.add(t)
                db.session.commit()
                print("Contact saved successfully!")
            except Exception as e:
                db.session.rollback()
                print(f"Error saving contact: {e}")
        else:
            if request.method == 'POST':
                print("Form validation failed:")
        
        return redirect(url_for('contact'))
            
@app.route('/admin', methods=['GET'])
def admin():
        codigo = request.args.get('codigo')
        if codigo != "isabella13":
            return render_template('error.html', message="Unauthorized access")
        try:
            task = Task.query.all()
        except Exception as e:
            print(f"Error al obtener tareas: {e}")
            task = []
        return render_template('admin.html', tasks=task, delete_task=url_for('delete_task', id=0))


@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
                try:
                    task = Task.query.get_or_404(id)  # Obtiene la tarea por ID o devuelve 404 si no existe

                    db.session.delete(task)  # Elimina la tarea de la sesión
                    db.session.commit()  # Guarda los cambios en la base de datos
                    message = ('Task deleted successfully', 'success')

                except Exception as e:
                    db.session.rollback()
                    message = (f'Error: {e}', 'error')
                    print(f"Error: {e}")

                return render_template('admin.html', tasks=Task.query.all(), delete_task=url_for('delete_task', id=0), message=message)


@app.route('/blog')
def blog():
            posts = Post.query.all()
            return render_template('blog.html', posts=posts)


@app.route('/blog/<slug>')
def posts_by_slug(slug):
            posts = Post.query.filter_by(slug=slug).all()
            return render_template('blog.html', posts=posts, slug=slug)


@app.route('/post/<int:id>', methods=['GET'])
def view_post(id):
        try:
            post = Post.query.get_or_404(id)
            return render_template('post.html', post=post)
        except Exception as e:
            print(f"Error retrieving post: {e}")
            return render_template('error.html', message="Post not found")


@app.route('/subscribers')
def subscribers():
    archivo = 'subs.json'
    subs = []

    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            subs = json.load(f)

    return render_template('subscribers.html', subs=subs)


if __name__ == "__main__":
     with app.app_context():
        db.create_all()
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port, debug=False)