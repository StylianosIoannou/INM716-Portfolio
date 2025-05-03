from flask import Flask, render_template, request, redirect, flash
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

#contact form
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        try:
            send_email(name, email, message)
            flash("✅ Message sent successfully!", "success")
        except Exception as e:
            print("Email sending failed:", e)
            flash("❌ Failed to send message. Please try again.", "error")

        return redirect("/contact")

    return render_template("Contact.html")

def send_email(name, email, message):
    subject = f"New Contact Form Message from {name}"
    body = f"From: {name} <{email}>\n\n{message}"
    msg = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

artworks = {
    "aral-sea": {
        "title": "The Aral Sea",
        "image": "images/Aralsea.jpg",
        "current_image": "images/Aralsea.jpg",
        "description": "Once a vast inland sea, now reduced to salt and memory. This piece reimagines the Aral Sea before ecological collapse — a thriving aquatic realm teeming with life and serenity, honoring what was and mourning what’s lost."
    },
    "zayanderud": {
        "title": "Zayanderud Echo",
        "image": "images/zayanderud.jpg",
        "current_image": "images/zayanderud.jpg",
        "description": "Flowing through the heart of Isfahan, the Zayanderud River sustained generations. Here, we restore its ancient pulse through AI, imagining the river alive again — cradling bridges, gardens, and the soul of a city."
    },
    "icelandic-forests": {
        "title": "Beech Forests of Iceland",
        "image": "images/icelandicforests.jpg",
        "current_image": "images/icelandicforests.jpg",
        "description": "Before the axes fell and the winds howled through bare landscapes, Iceland was cloaked in ancient beech forests. This vision breathes life back into that forgotten green, whispering what might have been."
    },
    "native-americans": {
        "title": "Native American Landscapes",
        "image": "images/nativeamericans.jpg",
        "current_image": "images/nativeamericans.jpg",
        "description": "This artwork pays tribute to Indigenous harmony with land — where mountains, animals, and people spoke in shared rhythms. It is not a reconstruction but a reverent reflection on balance, spirit, and sovereignty."
    },
    "vikings-past": {
        "title": "Norse Vikings Lost to Time",
        "image": "images/vikingspast.jpg",
        "current_image": "images/vikingspast.jpg",
        "description": "Among the fjords and crashing seas, Viking voices echo. This piece imagines not conquest, but quiet — the sacred landscapes, rituals, and seaborne myths that carried Norse memory across time."

    },
    "jerusalem": {
        "title": "Jerusalem by the Dead Sea",
        "image": "images/jerusalem.jpg",
        "current_image": "images/jerusalem.jpg",
        "description": "Perched on sacred stone, Jerusalem is reimagined in its mythic stillness. The city stands timeless, looking over the Dead Sea — a place of prophecy, pilgrimage, and enduring presence."
    },
    "parthenon": {
        "title": "The Parthenon Restored",
        "image": "images/Parthenon.jpg",
        "description": "We return the Parthenon to its full form — all 17 marbles intact, every column resolute. It stands here not as a ruin but as a restored idea: of beauty, philosophy, and empire, in perfect proportion."
    },
    "olympia": {
        "title": "Statue of Zeus in Olympia",
        "image": "images/Olympia.jpg",
        "description": "Once one of the Seven Wonders, the Statue of Zeus has been lost to fire and time. In this work, we raise it again — thunder-eyed, ivory-skinned, and seated in cosmic stillness within Olympia’s temple."
    },
    "egyptian_hie": {
        "title": "Egyptian Hieroglyphs Modernized",
        "image": "images/Egyptian_Hie.jpg",
        "description": "Ancient symbols, reawakened in the digital age. This artwork blends traditional Egyptian iconography with contemporary motion and color, drawing new lines between history, mystery, and design."
    },
    "linear_a": {
        "title": "Linear A Reimagined",
        "image": "images/Linear A.jpg",
        "description": "A script that speaks no known language. With this piece, AI offers a vision of what the Minoan world might have felt like — curved stone, glowing symbols, and a sea-bound culture etched in silence."
    },
    "pahlavi_era": {
        "title": "Modern Persia Rising",
        "image": "images/pahlavi era.jpg",
        "description": "Tehran in twilight — glowing neon, prayer calls, and revolutions both cultural and industrial. This piece revisits a modernizing Persia caught between memory and ambition."
    },
    "pairidaeza": {
        "title": "Pairidaeza – The Last Paradise",
        "image": "images/pairidaeza.jpg",
        "description": "Inspired by ancient Persian paradise gardens, this is a dream of heaven-on-earth — still waters, perfect symmetry, and starlight through trees. Pairidaeza means “walled garden,” but this one opens inward."
    },
    "shahnameh": {
        "title": "Divs and Djinn of the Desert",
        "image": "images/shahnameh2.jpg",
        "description": "From the pages of the Shahnameh come fire-born creatures, enchanted cities, and battles not of men but of myth. This work paints the Persian epic as a living dreamscape — volatile, divine, and boundless."
    },
    "achaeminid_empire": {
        "title": "Echoes of Achaemenid Majesty",
        "image": "images/achaemenid empire.jpg",
        "description": "Great halls carved in stone, columns like prayers. Here, the Achaemenid Empire is remembered not for war, but for architecture, tolerance, and vision. The echoes still resound."
    }
}



# Homepage
@app.route('/')
def home():
    return render_template('Homepage.html')

# About Page
@app.route('/about')
def about():
    return render_template('About.html')

# Sales Page
@app.route('/sales')
def sales():
    return render_template('Sales.html')

# Portfolio Pages
@app.route('/portfolio')
def portfolio():
    return render_template('Portfolio.html')

@app.route('/portfolio2')
def portfolio2():
    return render_template('portfolio2.html')

@app.route('/portfolio3')
def portfolio3():
    return render_template('portfolio3.html')
#artowrk pages
@app.route('/artwork/<art_id>')
def artwork_page(art_id):
    art = artworks.get(art_id)
    if not art:
        return "Artwork not found", 404
    return render_template('artwork.html', art=art)


if __name__ == '__main__':
    app.run(debug=True)
