from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..Home import Home

class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.go_to_home()

    # Any code you write here will run before the form opens.



  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    user = anvil.users.get_user()
    if user:
      logout = confirm("Do you want to log out?")
      if logout:
        anvil.users.logout()
        self.go_to_home()
    else:
      anvil.users.login_with_form()

  def saved_button_change(self):
    self.link_3.visible = anvil.users.get_user() is not None
  
  def go_to_home(self):
    self.content_panel.clear()
    self.content_panel.add_component(Home())

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.go_to_home()


  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
