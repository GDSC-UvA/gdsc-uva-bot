import jinja2

ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader("templates/"))

VERIFICATION_MESSAGE_TEMPLATE = ENVIRONMENT.get_template("messages/verification_welcome.md")

def verification_message(username: str) -> str:
    return VERIFICATION_MESSAGE_TEMPLATE.render(username=username)