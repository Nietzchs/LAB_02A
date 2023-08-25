from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/anime",methods=['POST'])
def upload_anime():
    
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
    idd=input['id']
    title=input['title']
    score=input['score']
    type=input['type']
    season=input['season']
    genre=input['genre']
    
    if idd<= 10:
        return jsonify({"response": "No se puede sobreescribir en un anime de la lista"})
    elif idd==11:
        animes.append({})
        animes[idd]["id"]=idd;
        animes[idd]["title"]=title;
        animes[idd]["score"]=score;
        animes[idd]["type"]=type;
        animes[idd]["season"]=season;
        animes[idd]["genre"]=genre;

        list=[];
        for e in animes:
            x=e.get("title")
            list.append(x)

        return jsonify({"response": str(list)})
    else:
        return jsonify({"response": "El id no va de acuerdo al numero de elementos de la  lista de animes"})
if __name__=='__main__':
    app.run()
