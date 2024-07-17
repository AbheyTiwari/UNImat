from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..Home import Home
from ..Saved import Saved

class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.Signin_text()
    self.content_panel.add_component(Home())

    # Any code you write here will run before the form opens.

  def Signin_text(self):
    user = anvil.users.get_user()
    if user:
      email = user["email"]
      self.Signin_text = email
    else:
      self.Signin = "Sign In"

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.login_with_form()
    

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Home())


  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Saved())
