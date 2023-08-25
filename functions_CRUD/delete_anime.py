from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/anime/<id>",methods=['DELETE'])
def delete_anime(id):
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
    if id> len(animes)-1:
        print("No se puede")
        return jsonify({"response": "No existe un id que eliminar"})
    else:
        animes[id]={};
        list=[];
        for e in animes:
            x=e.get("title")
            list.append(x)
        return list

if __name__=='__main__':
    app.run()