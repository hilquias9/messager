from secrets import token_hex
class Messager:
    def __init__(self,*headers:str):
        self.headers={"length":token_hex(8).encode(),"end_length":token_hex(8).encode()}
        for header in headers:
            self.headers[header]=token_hex(8).encode()
            self.headers[f"end_{header}"]=token_hex(8).encode()

    def unpackger(self,msg:bytes):
        pass

    def m_packger(self,msg:bytes,header): #message
        msg_length=str(len(msg)+32+(len(msg)+32)).encode()
        message=self.headers[header]+self.headers["length"]+msg_length+self.headers["end_length"]+msg+self.headers[f"end_{header}"]
        return message

    def f_packger(self,msg:bytes): #file
        pass

    def see_headers(self):
        return self.headers

