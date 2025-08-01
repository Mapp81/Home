from app import db, app
from models import Post
from flask import url_for


with app.app_context():
     with app.test_request_context():
    # Crear un nuevo post
        new_post = Post(
            title="Transform Your Bathroom with Just a Few Essentials",
            frase1="Small changes can make a big impact in your bathroom space.",
            description="You don’t need a full renovation to give your bathroom a fresh new look. With just a few thoughtful additions—like compact organizers, simple shelving, or a soft rug—you can completely change the mood and functionality of the space. The right elements bring order, warmth, and a sense of calm, proving that minimal effort can lead to maximum transformation.",
            slug="bathroom",
            image1= url_for('static', filename='images/07bathroom.jpg'),  
            alttitle1="bathroom",
            image2=url_for('static', filename='images/07shelves1.jpg'),
            alttitle2="shelves",
            image3=url_for('static', filename='images/07shelves2.jpg'),
            alttitle3="shelves",
            link1='https://amzn.to/4l9Coph',
            label1="Bathroom Organizers",
            link2='https://amzn.to/3IUXBpC',
            label2="Bathroom Shelves",
            link3='https://amzn.to/4o7Xffg',
            label3="Bath Rug Mat",
            link4='https://amzn.to/3HeB06H',
            label4="Shower Curtain",
            frase2="As an Amazon Associate, I earn from qualifying purchases. If you use these affiliate links, you’ll be supporting this site at no additional cost to you — thank you!",
        )
        
        # Agregar y confirmar en la base de datos
        db.session.add(new_post)
        db.session.commit()
        
        print("Post agregado correctamente!")
