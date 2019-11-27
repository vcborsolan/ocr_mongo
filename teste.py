from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient('localhost',27017)
db = client.ocr_pdf
ocr = db.ocr

list = ['Certificamos que', 'Victor Cesar Barbosa Orsolan', '', 'Completou o curso Python Básico, cumprindo a carga', 'horária de 8 horas com o instrutor Guilherme', 'Junqueira. Certificado emitido em 06 de novembro de', '20 RO', '', ' ', '', 'Uberlândia, 06 de novembro de 2019', '', 'SOLYD', '', 'RES RUÉ TO solyd.com.br', '', 'Autenticidade: solyd.com.br/verificar/KPiTEdZsnj']

for x in range(0 , list.count('')):
    list.remove('')

for x in range(0 , list.count(' ')):
    list.remove(' ')

test = {}
for str in list:
    test[f'linha {list.index(str)}'] = str
    # print(list.index(str)+1)
# print(test)

# print(ocr.insert_one(test))
# teste = {}
# for obj in ocr.find( ):
#     teste[obj['_id']] = obj

# print(ocr.find_one( {"_id": ObjectId('5dde81234763e3aa88ad34dd') } ))
# pdf = ocr.find_one()
# for i,x in pdf.items() :
#     print(f"{i} | {x}")

# print(ocr.find_one())
# print(ocr.find_one_and_delete( {'_id': ObjectId('5ddebc31802fd044597801f6')} ) != None)
print(ocr.update_one( {'_id': ObjectId('5ddec1cc145efb56ca920b76')} , {"$set": {"linha 2": "Foda-se"}}))