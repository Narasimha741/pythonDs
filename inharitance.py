class emp:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show(self):
        print(self.name)
        print(self.salary)

class manager(emp):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept
    def show(self):
        super().show()
        print(self.dept)
    
d=manager("ravi",100000,"IT") 
d.show()




class camera:
    def __init__(self,camera_mp):
        self.camera_mp=camera_mp
    def take_photos(self):
        print(camera_mp)
    
class musicplayer(camera):
    def __init__(self,brand,camera_mp):
        super().__init__(camera_mp)
        self.brand=brand
    def play_music(self):
        super().take_photos()
        print(self.brand)
    
class smartphone(musicplayer):
    def __init__(self,model,brand,camera_mp):
        super().__init__(brand,camera_mp)
        self.model=model
    def show_details(self):
        super().play_music()
        print(self.model)
 
 
 d=smartphone("vivo v21e","vivo","40mp") 
 d.show_details()