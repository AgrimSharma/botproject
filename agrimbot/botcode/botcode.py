import re,os,json


class AgrimBot:
    def __init__(self):
        os.chdir('..')
        os.chdir('botfiles')

    def find_response(self,question,file_name):
        with open(os.path.abspath(file_name+'.txt'), 'r') as fn:
            data = eval(fn.read())
            resp = data.get(question.lower(), 'Please try again?')
            fn.close()
            return resp

    def get_response(self, question):
        s = re.findall(r'ai|finance|comedy|sports|technology', question)
        if s:
            res = self.find_response(question,s[0])
        else:
            res = self.find_response(question, 'custom.txt')

        return res

    def put_response(self,question,answer):
        with open(os.path.abspath('custom.txt'), 'r+') as fn:
            data = eval(fn.read())
            if data:
                fn.truncate()
                data[question] = answer
                fn.write(json.dumps(data))
            else:
                data[question] = answer
                fn.write(json.dumps(data))
            fn.close()
        return True
