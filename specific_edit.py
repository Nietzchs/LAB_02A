from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/anime/<id>",methods=['PATCH'])
def specific_edit(id):
    id=int(id) #del address
    animes= [{"id": 0,"title":"One Piece","score": 10,"type": "Serie","season": "1","genre": ["Action","Adventure"]},
            {"id": 1,"title":"Death Note","score": 7.9,"type": "Serie","season": "1","genre": ["Strategy","Psychological"]},
            {"id": 2,"title":"Shingeki No Kyojin","score": 8.5,"type": "Serie","season": "5","genre": ["Accion","Pelea"]},
            {"id": 3,"title":"Dragon Ball Z","score": 7.8,"type": "Serie","season": "GT","genre": ["Action","Fight"]},
            {"id": 4,"title":"Naruto","score": 7.5,"type": "Serie","season": "2","genre": ["Action","Fight", "Romance"]},
            {"id": 5,"title":"Full Metal Alchemist","score": 9.2,"type": "Serie","season": "2","genre": ["Accion","Fight", "Brotherhood"]},
            {"id": 6,"title":"One Punch Man","score": 7.9,"type": "Serie","season": "3","genre": ["Action","Fight", "Comedy"]},
            {"id": 7,"title":"Tsuki Ga Kirei","score": 9,"type": "Serie","season": "1","genre": ["Romance","Life"]},
            {"id": 8,"title":"Sword Art Online","score": 8.1,"type": "Serie","season": "3","genre": ["Action","Fight", "Tech"]},
            {"id": 9,"title":"Bleach","score": 7,"type": "Serie","season": "1","genre": ["Action","Fight","Shonnen"]},
            {"id": 10,"title":"Mob Psycho","score": 8,"type": "Serie","season": "1","genre": ["Action","Magic","Fight"]}
    ]; 
    input=request.json
    if id> 10:
        return jsonify({"response": "ID de anime inexistente"})
    else:

        if int(input['id'])==True:
            idd=input['id'] #De postman
            if int(idd)!=animes[id]["id"]:
                return jsonify({"response": "No se puede editar el anime, debido a que otro posee el mismo ID"})
            else:
                animes[id]["id"]=idd;
                return jsonify({"response": "Data editada: "+str(animes[id]["id"])})  
        else:
            if input['title'] == True:
                title=input['title']
                animes[id]["title"]=title
                return jsonify({"response": "Data editada: "+str(animes[id]["title"])})
            else:
                if input['score'] == True:
                    score=input['score']
                    animes[id]["score"]=score
                    return jsonify({"response": "Data editada: "+str(animes[id]["score"])})
                else:
                    if input['type'] == True:
                        type=input['type']
                        animes[id]["type"]=type
                        return jsonify({"response": "Data editada: "+str(animes[id]["type"])})
                    else:
                        if input['season'] == True:
                            season=input['season']
                            animes[id]["season"]=season
                            return jsonify({"response": "Data editada: "+str(animes[id]["season"])})
                        else:
                            if input['genre']==True:
                                genre=input['genre']
                                animes[id]["genre"]=genre;
                                return jsonify({"response": "Data editada: "+str(animes[id]["genre"])})
                            else:
                                return jsonify({"response": "No hay data que editar"})
    
if __name__=='__main__':
    app.run()









