from re import I, S
from persona import Persona
from mail import Mail

class Repository:
    def __init__(self):   
        self.personas = []
        self.persona_id_auto_increment = 0
        self.mails = []
        self.mail_id_auto_increment = 0

    def add_persona (self,p):
        #a medida que se crean los objetos, defino una variable contador,y se la voy asignando a los objetos creados
        #luego, almaceno los objetos en un array
        self.persona_id_auto_increment+=1
        p.persona_id=self.persona_id_auto_increment
        self.personas.append(p)
        return p
        
    def add_mail (self,m):
        #lo mismo que lo anterior pero para mails
        self.mail_id_auto_increment+=1
        m._Mail__mail_id=self.mail_id_auto_increment 
        self.mails.append(m)
        return m
    
    def to_string(self,persona_id=None,mail_id=None):
        output=""
        if persona_id!=None:
            output=output+str(self.personas[persona_id-1].persona_id)+"/"+self.personas[persona_id-1]._Persona__apellido+", "+self.personas[persona_id-1]._Persona__nombre
            for i in range(self.mail_id_auto_increment):
                if self.mails[i]._Mail__persona_id==persona_id:
                    output=output+"\n    "+str(self.mails[i]._Mail__mail_id)+" - "+self.mails[i]._Mail__tipo+"/"+self.mails[i]._Mail__mail+" - "+str(self.mails[i]._Mail__persona_id)
        if mail_id!=None:
            output=output+str(self.mails[mail_id-1]._Mail__mail_id)+" - "+self.mails[mail_id-1]._Mail__tipo+"/"+self.mails[mail_id-1]._Mail__mail+" - "+str(self.mails[mail_id-1]._Mail__persona_id)
            for i in range(self.persona_id_auto_increment):
                if self.personas[i].persona_id==self.mails[mail_id-1]._Mail__persona_id:
                    output=output+"\n    "+str(self.personas[i].persona_id)+"/"+self.personas[i]._Persona__apellido+", "+self.personas[i]._Persona__nombre
                    
        return output





