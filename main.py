from models.model import Model
from views.view import View
from controllers.controller import Controllers

if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controllers(model, view)

    controller.start_application()