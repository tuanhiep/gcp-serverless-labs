import genanki

# Define Anki Model
anki_model = genanki.Model(
    1607392322,
    "Google App Engine Structure Guide",
    fields=[{"name": "Question"}, {"name": "Answer"}],
    templates=[{
        "name": "Card 1",
        "qfmt": "<b>{{Question}}</b>",
        "afmt": "{{FrontSide}}<hr id='answer'>{{Answer}}",
    }],
)

# List of Detailed Anki Cards about Structure
anki_cards_data = [
    (
        "What is the required folder structure for deploying a Python Flask app on Google App Engine?",
        "<b>📌 A Google App Engine (GAE) application must have a structured folder layout for deployment.</b>"
        "<br><br><b>✅ Python Flask App Folder Structure:</b>"
        "<br><code>"
        "my-flask-app/\n"
        "│── main.py                # Flask app entry point\n"
        "│── app.yaml               # GAE deployment configuration\n"
        "│── requirements.txt       # Dependencies (Flask, Gunicorn, etc.)\n"
        "│── static/                # CSS, JS, images\n"
        "│── templates/             # HTML files (if using Jinja)\n"
        "</code>"
        "<br><br><b>✅ Key Files Explained:</b>"
        "<br>✔ <b>main.py</b> → Contains the Flask application logic."
        "<br>✔ <b>app.yaml</b> → Defines the runtime, scaling settings, and environment variables."
        "<br>✔ <b>requirements.txt</b> → Lists all necessary dependencies."
    ),
    (
        "What is the required folder structure for deploying a Java Spring Boot app on Google App Engine?",
        "<b>📌 A Spring Boot application on GAE requires specific configurations.</b>"
        "<br><br><b>✅ Java Spring Boot App Folder Structure:</b>"
        "<br><code>"
        "springboot-app/\n"
        "│── src/main/java/com/example/SpringBootApp.java  # Main entry point\n"
        "│── src/main/resources/application.properties    # Configuration settings\n"
        "│── app.yaml                                    # GAE deployment settings\n"
        "│── pom.xml OR build.gradle                     # Dependencies\n"
        "</code>"
        "<br><br><b>✅ Key Files Explained:</b>"
        "<br>✔ <b>SpringBootApp.java</b> → The main Java class containing <code>@SpringBootApplication</code>."
        "<br>✔ <b>app.yaml</b> → Defines runtime (<code>java17</code>), instance class, and scaling settings."
    ),
    (
        "How do you structure an application with multiple services in Google App Engine?",
        "<b>📌 In GAE, you can define multiple services to separate different parts of an application.</b>"
        "<br><br><b>✅ Example Multi-Service Folder Structure:</b>"
        "<br><code>"
        "my-microservices-app/\n"
        "│── service-frontend/\n"
        "│   ├── app.yaml             # Defines this service as the frontend\n"
        "│   ├── main.py              # Frontend application logic\n"
        "│── service-api/\n"
        "│   ├── app.yaml             # Defines this service as the API\n"
        "│   ├── api.py               # API service logic\n"
        "</code>"
        "<br><br><b>✅ How Multi-Service Deployment Works:</b>"
        "<br>✔ Each service has its own <b>app.yaml</b> and codebase."
        "<br>✔ The <b>frontend</b> service interacts with the <b>backend API</b>."
        "<br>✔ Services can scale independently based on traffic needs."
    ),
    (
        "What are the required files for deploying an application on Google App Engine?",
        "<b>📌 To deploy an app on Google App Engine, you must include these key files:</b>"
        "<br><br><b>✅ Required Files:</b>"
        "<br>✔ <b>app.yaml</b> → Defines the runtime, scaling behavior, and environment variables."
        "<br>✔ <b>main.py</b> (Python) / <b>SpringBootApp.java</b> (Java) → The main application logic."
        "<br>✔ <b>requirements.txt</b> (Python) / <b>pom.xml</b> (Java) → Lists required dependencies."
        "<br><br><b>✅ Optional but Recommended:</b>"
        "<br>✔ <b>cron.yaml</b> → If using scheduled tasks (Cron Jobs)."
        "<br>✔ <b>dispatch.yaml</b> → For URL routing across multiple services."
    ),
    (
        "How do you separate staging and production environments in Google App Engine?",
        "<b>📌 Best Practice: Use Multiple Services or Separate GCP Projects.</b>"
        "<br><br><b>✅ Method 1: Use Multiple Services in `app.yaml`</b>"
        "<br><code>"
        "# Staging Environment\n"
        "service: staging\n"
        "runtime: python39\n"
        "entrypoint: gunicorn -b :$PORT main:app\n"
        "automatic_scaling:\n"
        "  min_instances: 0\n"
        "  max_instances: 2\n"
        "</code>"
        "<br><code>"
        "# Production Environment\n"
        "service: default\n"
        "runtime: python39\n"
        "entrypoint: gunicorn -b :$PORT main:app\n"
        "automatic_scaling:\n"
        "  min_instances: 1\n"
        "  max_instances: 5\n"
        "</code>"
        "<br><br><b>✅ Method 2: Use Separate GCP Projects</b>"
        "<br>✔ Create a <b>staging project</b> and a <b>production project</b> in Google Cloud."
        "<br>✔ Deploy staging code to the staging project first."
        "<br>✔ Once verified, deploy the stable version to the production project."
    )
]

# Create Anki Deck
anki_deck = genanki.Deck(2059400113, "Google App Engine Structure Guide")

# Add cards to deck
for question, answer in anki_cards_data:
    note = genanki.Note(model=anki_model, fields=[question, answer])
    anki_deck.add_note(note)

# Save the Anki deck
genanki.Package(anki_deck).write_to_file("google_app_engine_structure.apkg")

print("✅ Anki deck successfully generated: google_app_engine_structure.apkg")