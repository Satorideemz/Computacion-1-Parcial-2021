from logging import raiseExceptions
class Mail:
    def __init__(self,mail,tipo,persona_id=None):
        self._Mail__mail_id=None
        self._Mail__mail=mail
        self._Mail__tipo=tipo
        self._Mail__persona_id=persona_id
        #esto valida que el mail haya sido escrito con arroba
        if self._Mail__mail.find("@") == -1:
            raise Exception("mail invalido")
        
    #sobre-escribo el metodo str para que se ajuste a lo que solicita el test
    def __str__(self=None):
        mail_id="None"
        persona_id="None"
        if self._Mail__mail_id!=None:
            mail_id=self._Mail__mail_id
        if self._Mail__persona_id!=None:
            persona_id=self._Mail__persona_id        
        m=mail_id+" - "+self._Mail__tipo+"/"+self._Mail__mail+" - "+persona_id
        return m
    