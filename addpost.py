from app import db, app
from models import Post
from flask import url_for


with app.app_context():
     with app.test_request_context():
    # Crear un nuevo post
        new_post = Post(
            title="Enchant Your Evenings with Garden Glow",
            frase1="Transform your garden into a path of light and calm.",
            description="These LED solar woven sphere lights and stakes not only illuminate, but add a charming touch to any garden, patio or terrace. Easy to install, waterproof and rechargeable with solar energy, they are the perfect option to create cozy outdoor environments without cables or complications. Ideal for special nights, outdoor dinners or simply enjoying the landscape from your window. Available on Amazon for immediate shipping!",
            slug="garden",
            image1= url_for('static', filename='images/06gardenlights.png'),  
            alttitle1="iluminated garden",
            image2=url_for('static', filename='images/06globe.jpg'),
            alttitle2="solar globe light",
            image3=url_for('static', filename='images/06solarground.jpg'),
            alttitle3="solar ground light",
            link1='https://amzn.to/41eFC3s',
            link2='https://amzn.to/4fty3fz',
            frase2="I am an Amazon associate. I invite you to use these links for your convenience and to continue maintaining my website.",
        )
        
        # Agregar y confirmar en la base de datos
        db.session.add(new_post)
        db.session.commit()
        
        print("Post agregado correctamente!")
