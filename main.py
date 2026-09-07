from secrets import token_hex
class Messager:
    def __init__(self,*headers:str):
        self.headers={"length":token_hex(8).encode(),"end_length":token_hex(8).encode()}
        for header in headers:
            self.headers[header]=token_hex(8).encode()
            self.headers[f"end_{header}"]=token_hex(8).encode()
        self.stack=b""

    def unpackger(self,msg:bytes,header):
        message=[]
        while True:
            start=msg.find(self.headers["length"])
            end=msg.find(self.headers["end_length"])
            msg_length=int(msg[start+16:end])
            message.append(msg[end+16:msg.find(self.headers[f"end_{header}"])])
            msg=msg[msg_length:]
            if len(msg)==0:
                break
        return message

    def packger(self,msg:bytes,header): 
        counter=0
        for number in str(len(msg)):
            counter+=1
        msg_length=str(64+len(msg)+counter).encode()
        message=self.headers[header]+self.headers["length"]+msg_length+self.headers["end_length"]+msg+self.headers[f"end_{header}"]
        return message

    def see_headers(self):
        return self.headers

