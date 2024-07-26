from ._anvil_designer import display_courseTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..StudyNow import StudyNow


class display_course(display_courseTemplate):
  def __init__(self, name, butoon_text, image, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name_1.text=name
    self.image_content.source=image
    self.study_now.text=butoon_text

    # Any code you write here will run before the form opens.
  
  def give_course(self):
    courses = anvil.server.call("get_course_detail").search()
    for course in courses:
      c= display_course(image=course["Image"])
      self.conent_panel.add_component(c)