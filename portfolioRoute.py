from app import db
from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify, request, session, Blueprint, make_response
from model.portfolioModel import Intro, About, Experience, Project, Contact
import cloudinary.uploader


port_bp = Blueprint ("port_bp", __name__)

#Getting endpont for intro
@port_bp.route('/api/portfolio/intros', methods=['GET'])
def get_intro():
    intros = Intro.query.all()
    result = [intro.to_dict() for intro in intros]
    return jsonify(result)



#posting endpoint for intro
@port_bp.route("/api/portfolio/intros", methods=["POST"])
def create_intro():
    try:
      
        data = request.get_json()

        welcomeText = data['welcomeText']
        firstName = data['firstName']
        lastName = data['lastName']
        caption = data['caption']
        description = data['description']

        
        new_intro = Intro(welcomeText=welcomeText, firstName=firstName, lastName=lastName, caption=caption, description=description)

        db.session.add(new_intro)
        db.session.commit()

        
        return jsonify({"message": "Intro created successfully!","data":new_intro.to_dict()}), 201 
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500



# updateing endpoint for into
# @port_bp.route("/api/portfolio/intros/", methods=['PUT'])
# def update_intro():
#     try:
#         intros = Intro.query.first() 
#         if intros is None:
#             return jsonify({"error":"Intro not found"}), 404

#         data = request.get_json()
        
#         intros.welcomeText = data.get("welcomeText", intros.welcomeText)
#         intros.firstName = data.get("firstName", intros.firstName)
#         intros.lastName = data.get("lastName", intros.lastName)
#         intros.caption = data.get("caption", intros.caption)
#         intros.description = data.get("description", intros.description)

#         db.session.commit()
#         return jsonify({"message": "Intro updated successfully", "data": intros.to_dict()})

#     except Exception as e:
#         db.session.rollback()
#         return jsonify({"error": str(e)}), 500

@port_bp.route("/api/portfolio/intros/", methods=['PUT'])
def update_intro():
    try:
        intros = Intro.query.first() 
        if intros is None:
            return jsonify({"error": "Intro not found"}), 404

        data = request.get_json()
        
        # Update fields only if they are present in the request
        if "welcomeText" in data:
            intros.welcomeText = data["welcomeText"]
        if "firstName" in data:
            intros.firstName = data["firstName"]
        if "lastName" in data:
            intros.lastName = data["lastName"]
        if "caption" in data:
            intros.caption = data["caption"]
        if "description" in data:
            intros.description = data["description"]

        db.session.add(intros)  # Explicitly add the object to the session
        db.session.commit()
        
        # Refresh the object to ensure we have the latest data
        db.session.refresh(intros)
        
        return jsonify({"message": "Intro updated successfully", "data": intros.to_dict()})

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500   

    

# Deleting endpoint for intro
@port_bp.route("/api/portfolio/intros/<int:intro_id>", methods=["DELETE"])
def deleteOne(intro_id):
    try:
        intro = Intro.query.get(intro_id)
        db.session.delete(intro)
        db.session.commit()
        return jsonify({"message": "Intro deleted successfully", "data": intro.to_dict()})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500





# Getting endpoint for about

@port_bp.route('/api/portfolio/abouts', methods=['GET'])
def get_about():
    about = About.query.all()
    result = [about.to_dict() for about in about]
    return jsonify(result)



#Posting endpoint for about
@port_bp.route("/api/portfolio/abouts", methods=["POST"])
def create_about():
    try:
       
        if request.is_json:
            data = request.json
            description1 = request.form.get("description1")
            description2 = request.form.get("description2")
            skills =  request.form.get("skills")
        else:
            description1 = request.form.get('description1')
            description2 = request.form.get('description2')
            skills =  request.form.get("skills")
        

        if 'lottieURL' not in request.files:
            return jsonify({"message": "No image found"}), 400
        
        file = request.files['lottieURL']
        if file.filename == '':
            return jsonify({"message": "No selected file"}), 400
        if file:
            upload_result = cloudinary.uploader.upload(file)
            image_url = upload_result.get("secure_url")
        new_about = About(lottieURL=image_url, description1=description1, description2=description2,skills=skills)
        db.session.add(new_about)
        db.session.commit()

        return jsonify({"message": "About created successfully!","data":new_about.to_dict()}), 201 
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500



# updateing endpoint for about

@port_bp.route("/api/portfolio/abouts", methods=["PUT"])
def update_about():
    try:
      
        about = About.query.first()
        if not about:
            return jsonify({"message": "About not found"}), 404
        description1 = request.form.get('description1', about.description1)
        description2 = request.form.get('description2', about.description2)
        skills = request.form.get('skills', about.skills)
        about.description1 = description1
        about.description2 = description2
        about.skills = skills

       
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                upload_result = cloudinary.uploader.upload(file)
                about.lottieURL = upload_result.get("secure_url")

        db.session.commit()
        return jsonify({"message": "About updated successfully!", "data": about.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

            


# Deleting endpoint for about
@port_bp.route("/api/portfolio/abouts/<int:about_id>", methods=["DELETE"])
def deleteOneAbout(about_id):
    try:
        about = About.query.get(about_id)
        db.session.delete(about)
        db.session.commit()
        return jsonify({"message": "About deleted successfully", "data": about.to_dict()})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500    
    


    # Experirnce endpoint starts from here
@port_bp.route("/api/portfolio/get-experience", methods=["GET"])
def get_experiences():
    try:
        experiences = Experience.query.all()
        return jsonify([experience.to_dict() for experience in experiences]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500    


#adding endpoint for experience
@port_bp.route("/api/portfolio/add-experience", methods=["POST"])
def create_experience():
    try:
        data = request.get_json()
        new_experience = Experience(
            title=data['title'],
            period=data['period'],
            company=data['company'],
            description=data['description']
        )
        db.session.add(new_experience)
        db.session.commit()
        return jsonify({"message": "Experience created successfully!", "data": new_experience.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    


# updateing endpoint for experience
@port_bp.route("/api/portfolio/update-experience/<id>", methods=["PUT"])
def update_experience(id):
    try:
        experience = Experience.query.get(id)
        if not experience:
            return jsonify({"error": "Experience not found"}), 404
        
        data = request.get_json()
        experience.title = data.get('title', experience.title)
        experience.period = data.get('period', experience.period)
        experience.company = data.get('company', experience.company)
        experience.description = data.get('description', experience.description)
        
        db.session.commit()
        return jsonify({"message": "Experience updated successfully!", "data": experience.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
#Delete endpoint for Experience
@port_bp.route("/api/portfolio/del-experience/<id>", methods=["DELETE"])
def delete_experience(id):
    try:
        experience = Experience.query.get(id)
        if not experience:
            return jsonify({"error": "Experience not found"}), 404
        
        db.session.delete(experience)
        db.session.commit()
        return jsonify({"message": "Experience deleted successfully!", "data": experience.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    


# Project endpoint starts here
@port_bp.route("/api/portfolio/get-project", methods=["GET"])
def get_projects():
    try:
        projects = Project.query.all()
        return jsonify([project.to_dict() for project in projects]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500  

    #adding endpoint for project
@port_bp.route("/api/portfolio/add-projects", methods=["POST"])
def add_project():
    try:
        title = request.form.get("title")
        description1 = request.form.get("description1")
        description2 = request.form.get("description2")
        img_url = None
        if 'img_url' in request.files:
            file = request.files['img_url']
            if file.filename != '':
                upload_result = cloudinary.uploader.upload(file)
                img_url = upload_result.get("secure_url")

        new_project = Project(
            title=title,
            description1=description1,
            description2=description2,
            img_url=img_url
        )

        db.session.add(new_project)
        db.session.commit()

        return jsonify({"message": "Project added successfully!", "data": new_project.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500



# updateing endpoint for project
@port_bp.route("/api/portfolio/update-projects/<int:id>", methods=["PUT"])
def update_project(id):
    try:
       
        project = Project.query.get_or_404(id)

       
        title = request.form.get("title", project.title)
        description1 = request.form.get("description1", project.description1)
        description2 = request.form.get("description2", project.description2)

        if 'img_url' in request.files:
            file = request.files['img_url']
            if file.filename != '':
                upload_result = cloudinary.uploader.upload(file)
                project.img_url = upload_result.get("secure_url")

    
        project.title = title
        project.description1 = description1
        project.description2 = description2
        db.session.commit()

        return jsonify({"message": "Project updated successfully!", "data": project.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# Deleting endpoint for project
@port_bp.route("/api/portfolio/delete-projects/<int:id>", methods=["DELETE"])
def deleteOneProject(id):
    try:
        project = Project.query.get_or_404(id)
        db.session.delete(project)
        db.session.commit()
        return jsonify({"message": "Project deleted successfully", "data": project.to_dict()})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

 
    
    # Contact endpoint starts here
@port_bp.route("/api/portfolio/get-contacts", methods=["GET"])
def get_contacts():
    try:
        contacts = Contact.query.all()
        return jsonify([contact.to_dict() for contact in contacts]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500 

    #adding endpoint for contacts
# @port_bp.route("/api/portfolio/contacts", methods=["POST"])
# def create_contact():
#     try:
#         # Get the request data
#         data = request.get_json()
        
#         # Extract the required fields
#         name = data['name']
#         email = data['email']
#         age = data['age']
#         gender = data['gender']
#         mobile = data['mobile']
#         address = data['address']
        

#         new_contact = Contact(name=name, email=email, age=age, gender=gender, mobile=mobile, address=address)

#         # Add the project to the database
#         db.session.add(new_contact)
#         db.session.commit()

#         # Return a success message
#         return jsonify({"message": "Contact created successfully!","data":new_contact.to_dict()}), 201 
#     except Exception as e:
#         # Roll back the database changes if an error occurs
#         db.session.rollback()
#         # Return an error message
#         return jsonify({"error": str(e)}), 500



# updateing endpoint for contact
@port_bp.route("/api/portfolio/update-contacts", methods=['PUT'])
def update_contact():
    try:
        contacts = Contact.query.first() 
        if contacts is None:
            return jsonify({"error":"Contact not found"}), 404

        data = request.get_json()
        
        contacts.name = data.get("name", contacts.name)
        contacts.email = data.get("email", contacts.email)
        contacts.age = data.get("age", contacts.age)
        contacts.gender = data.get("gender", contacts.gender)
        contacts.mobile = data.get("mobile", contacts.mobile)
        contacts.address = data.get("address", contacts.address)

        db.session.commit()
        return jsonify({"message": "Contact updated successfully", "data": contacts.to_dict()})

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500         


# Deleting endpoint for contact
@port_bp.route("/api/portfolio/contacts/<int:contact_id>", methods=["DELETE"])
def deleteOneContact(contact_id):
    try:
        contact = Contact.query.get(contact_id)
        db.session.delete(contact)
        db.session.commit()
        return jsonify({"message": "Contact deleted successfully", "data": contact.to_dict()})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500   