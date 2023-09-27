from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(40), nullable=False)
    lastName = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(400), unique=False, nullable=False)
    img = db.Column(db.String(400), nullable=False)
    role = db.Column(db.String(15), nullable=False)
    teacher = db.Column(db.String(280), nullable=True)
    teacher_id = db.Column(db.String(80), nullable=True)
    # module_progress = db.relationship('ModuleProgress', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "img": self.img,
            "role": self.role,
            # No serializar la contraseña, es un problema de seguridad
        }

class Teacher(db.Model):
    __tablename__ = 'Teacher'
    id=db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(40), nullable=False)
    lastName = db.Column(db.String(40), nullable=False)
    students = db.Column(db.String(50000), nullable=True)
    email = db.Column(db.String(250), nullable=False)
    role= db.Column(db.String(250), nullable=False)


    def __repr__(self):
        return f'<Teacher {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "students": self.students,
            "role": self.role
        }



class TokenBlockedList(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    token=db.Column(db.String(1000), unique=True, nullable=False)
    created_at=db.Column(db.DateTime, nullable=False)


class Exercise(db.Model):
    __tablename__ = 'exercise'
    id = db.Column(db.Integer, primary_key=True)
    module = db.Column(db.String(50))
    type = db.Column(db.String(40))
    question = db.Column(db.String(250))
    info_blog = db.Column(db.String(250))
    info_youtube = db.Column(db.String(250))
    

    def __repr__(self):
        return f'<Exercise {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "module": self.module,
            "type": self.type,
            "question": self.question,
            "info_blog": self.info_blog,
            "info_youtube":self.info_youtube
        }

class Answers(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    module = db.Column(db.String(50))
    type = db.Column(db.String(40))
    answers = db.Column(db.String(250))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    isCorrect = db.Column(db.Boolean, default=False)
    
    
    def __repr__(self):
        return f'<ExerciseAnswer {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "answers": self.answers,
            "isCorrect": self.isCorrect,
            "type": self.type,
            "exercise_id": self.exercise_id
        }





# class Module(db.Model):
#     __tablename__ = 'module'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     description = db.Column(db.String(250))
#     type = db.Column(db.String(50))

#     def __repr__(self):
#         return f'<Module {self.id}>'

#     def serialize(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "description": self.description,
#             "type": self.type
#         }

#class ModuleProgress(db.Model):
#    __tablename__ = 'module_progress'
#      id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     module_id = db.Column(db.Integer, db.ForeignKey('module.id'))
#      progress = db.Column(db.Integer)

#     def __repr__(self):
#         return f'<ModuleProgress {self.id}>'

#     def serialize(self):
#         return {
#             "id": self.id,
#             "user_id": self.user_id,
#             "module_id": self.module_id,
#             "progress": self.progress
#         }