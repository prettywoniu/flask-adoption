from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet name", 
                       validators=[InputRequired(message="Name cannot be blank")])
    species = StringField("Species", 
                          validators=[InputRequired(message="Species cannot be blank"), 
                                      AnyOf(values=['dog','cat','porcupine'])])
    photo_url = StringField("Photo URL", 
                            validators=[Optional(), URL()])
    age = IntegerField("Age", 
                      validators=[NumberRange(min=0, max=30)])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """Form for editing a pet"""

    photo_url = StringField("Photo URL", 
                            validators=[Optional(), URL()])
    age = IntegerField("Age", 
                      validators=[NumberRange(min=0, max=30)])
    notes = StringField("Notes")