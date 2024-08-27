from app import db
import json



class Intro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    welcomeText = db.Column(db.String(1000), nullable=False)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    caption = db.Column(db.String(10000), nullable=False)
    description = db.Column(db.String(10000), nullable=False)

  
    def to_dict(self):
        return {
            'id': self.id,
            'welcomeText': self.welcomeText,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'caption': self.caption,
            'description': self.description
        }
    

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lottieURL = db.Column(db.String(1000), nullable=True)
    description1 = db.Column(db.String(1000), nullable=False) 
    description2 = db.Column(db.String(1000), nullable=False)
    skills = db.Column(db.String(1000), nullable=True)
    

    # def set_skills(self, skills_list):
    #     self.skills = json.dumps(skills_list)

    # def get_skills(self):
    #     return json.loads(self.skills)  if self.skills else []   

    def to_dict(self):
        return {    
            'id': self.id,
            'lottieURL': self.lottieURL,
            'description1': self.description1,
            'description2': self.description2,
            'skills': self.skills
        }
    

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    period = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)


    def to_dict(self):  
        return {
            'id': self.id,
            'title': self.title,
            'period': self.period,
            'company': self.company,
            'description': self.description
        }    




class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description1 = db.Column(db.String(1000), nullable=True)
    description2 = db.Column(db.String(1000), nullable=True)
    img_url = db.Column(db.String(1000), nullable=True)
    link = db.Column(db.String(1000), nullable=True)
    technologies = db.Column(db.String(5000), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description1': self.description1,
            'description2': self.description2,
            'img_url': self.img_url,
            'link': self.link,
            'technologies': self.technologies
        }
    


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)



    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'gender': self.gender,
            'mobile': self.mobile,
            'address': self.address
        }    