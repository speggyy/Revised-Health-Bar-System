
from Systems import Character
from Systems import Health
from Systems import Weapon

healthBar = Health(5, 6)
dagger = Weapon("Dagger", 1)
character = Character("Chris Rock", healthBar, dagger)

healthBar.printHealth()
character.printCharacter()