class Guns:
    def __init__(self, type_gun, rounds_in_mag, condition=10):
        self.type_gun = type_gun
        self.rounds_in_mag = rounds_in_mag
        self.condition = condition

    def shoot(self):
        if self.rounds_in_mag < 1:
            return f'No ammo! RELOAD!'
        if self.condition >= 4:
            self.rounds_in_mag -= 1
            self.condition -= 1
            if self.condition <= 5:
                return f'A shot with a {self.type_gun}! Rounds: {self.rounds_in_mag}. Condition: {self.condition}\n' \
                       f'Weapon needs repairs!'
            return f'A shot with a {self.type_gun}! Rounds: {self.rounds_in_mag}. Condition: {self.condition}'
        else:
            return f'Weapon jammed!'

    def reload(self):
        if self.type_gun == 'smg' or self.type_gun == 'assault rifle':
            if 0 < self.rounds_in_mag < 30:
                self.rounds_in_mag = 31
            elif self.rounds_in_mag == 0:
                self.rounds_in_mag = 30
            else:
                return 'Mag is full!! No need to reload!'
            return f'Reloading... Mag: {self.rounds_in_mag} rounds!'
        elif self.type_gun == 'pistol':
            if 0 < self.rounds_in_mag < 8:
                self.rounds_in_mag = 9
            elif self.rounds_in_mag == 0:
                self.rounds_in_mag = 8
            else:
                return 'Mag is full! No need to reload!'
            return f'Reloading... Mag: {self.rounds_in_mag} rounds!'
        elif self.type_gun == 'shotgun':
            if self.rounds_in_mag == 5:
                return 'Mag is full! No need to reload!'
            else:
                self.rounds_in_mag += 1
            return f'Reloading... Mag: {self.rounds_in_mag} rounds!'
        elif self.type_gun == 'rpg':
            if self.rounds_in_mag == 0:
                self.rounds_in_mag = 1
            else:
                return 'Mag is full! No need to reload!'
            return f'Reloading... Mag: {self.rounds_in_mag} rounds!'


pm = Guns('pistol', 8)
mp5 = Guns('smg', 30)
ak_47 = Guns('assault rifle', 30)
mp_133 = Guns('shotgun', 5)
rpg_7 = Guns('rocket launcher', 1)

print(ak_47.shoot())
print(ak_47.shoot())
print(ak_47.shoot())
print(ak_47.shoot())
print(ak_47.shoot())
print(ak_47.reload())
print(ak_47.shoot())
print(ak_47.shoot())
print(ak_47.shoot())
print(ak_47.shoot())
