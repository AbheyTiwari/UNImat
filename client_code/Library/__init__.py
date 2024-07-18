from ._anvil_designer import LibraryTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users


class Library(LibraryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_course()
    

    # Any code you write here will run before the form opens.
  def load_course(self):
    courses = anvil.server.call("get_course_detail").search()
    for course in courses:
      print(course["Name"])