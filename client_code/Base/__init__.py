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
from ..Saved import Saved

class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.Signin_text()
    self.go_to_home()

    # Any code you write here will run before the form opens.

  def Signin_text(self):
    user = anvil.users.get_user()
    if user:
      email = user["email"]
      self.link_2.text = email
    else:
      self.link_2.text = "Sign In"
    self.saved_button_change()


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
    self.Signin_text()

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
    self.content_panel.add_component(Saved())
