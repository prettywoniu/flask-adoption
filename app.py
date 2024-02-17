from flask import Flask, request, render_template, redirect, flash
#from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "123456"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug = True
#debug = DebugToolbarExtension(app)

connect_db(app)

# with app.app_context():
#     db.drop_all()
#     db.create_all()

#     pet1 = Pet(name='Woofly', species='dog', age=3, photo_url="http://www.fillster.com/images/pictures/185f.jpg", notes='sensitive')
#     pet2 = Pet(name='Porchetta',species='porcupine', age=1, notes='sharp spines')
#     pet3 = Pet(name='Snargle', species='cat', photo_url="http://www.fillster.com/images/pictures/276u.jpg", age=1, notes='like people')

#     db.session.add(pet1)
#     db.session.add(pet2)
#     db.session.add(pet3)

#     db.session.commit()


@app.route('/')
def list_pets():
    """Show all the pets"""
    pets = Pet.query.all()

    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        with app.app_context():
            db.session.add(pet)
            db.session.commit()

        flash(f"Added a {species} {name}")
        return redirect('/')
    else:
        return render_template("add.html", form=form)
    
@app.route('/<int:pid>')
def show_pet_detail(pid):
    pet = Pet.query.get_or_404(pid)
    return render_template('info.html', pet=pet)

@app.route('/<int:pid>/edit', methods=["GET", "POST"])
def edit_pet(pid):
    """Show pet edit form and handle edit"""

    pet = Pet.query.get_or_404(pid)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        with app.app_context():
            db.session.commit()
        flash(f"Added a {pet.species} {pet.name}")
        return redirect(f"/{pid}")
    else:
        return render_template("edit.html", form=form, name=pet.name)