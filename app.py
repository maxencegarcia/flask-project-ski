#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, flash

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'une cle(token) : grain de sel(any random string)'


typeSki = [
    {'id' : 1 ,'libelleType':'Mini-ski'},
    {'id' : 2 ,'libelleType':'Ski de fond'},
    {'id' : 3 ,'libelleType':'Ski de piste'},
    {'id' : 4 ,'libelleType':'Ski de randonnée'},
    {'id' : 5 ,'libelleType':'Freestyle'},
    {'id' : 6 ,'libelleType':'Freeride'},
]
skis = [
   {'id' : 1 ,'modeleSki':'Wedze 500', 'dateAchat':'2019-05-20', 'etat':'Très Bon', 'prixAchat':'240', 'prixLocation':'50', 'taille':'172', 'typeSki_id':5, 'imageSki': 'wedze_500.jpg'},
   {'id' : 2 ,'modeleSki':'Wedze 500 Slash 100', 'dateAchat':'2020-09-13', 'etat':'Neuf', 'prixAchat':'360', 'prixLocation':'75', 'taille':'184', 'typeSki_id':6, 'imageSki': 'wedze_500_slash_100.jpg'},
   {'id' : 3 ,'modeleSki':'Inovix XC S 500', 'dateAchat':'2019-11-19', 'etat':'Assez Bon', 'prixAchat':'155', 'prixLocation':'30', 'taille':'205', 'typeSki_id':2, 'imageSki': 'inovix_xc_s_500.jpg'},
   {'id' : 4 ,'modeleSki':'Rossignol Experience 80', 'dateAchat':'2018-09-12', 'etat':'Très Bon', 'prixAchat':'380', 'prixLocation':'38', 'taille':'174', 'typeSki_id':3, 'imageSki': 'rossignol_experience_80.jpg'},
   {'id' : 5 ,'modeleSki':'Wedze Mountain touring MT85', 'dateAchat':'2018-07-11', 'etat':'Très Bon', 'prixAchat':'575', 'prixLocation':'56', 'taille':'176', 'typeSki_id':4, 'imageSki': 'wedze_mountain_touring_mt85.jpg'},
   {'id' : 6 ,'modeleSki':'Atomic Redster X5', 'dateAchat':'2019-05-20', 'etat':'Assez Bon', 'prixAchat':'370', 'prixLocation':'32', 'taille':'177', 'typeSki_id':3, 'imageSki': 'atomic_redster_x5.png'},
   {'id' : 7 ,'modeleSki':'Rossignol Experience 84', 'dateAchat':'2019-11-01', 'etat':'Bon', 'prixAchat':'540', 'prixLocation':'35', 'taille':'184', 'typeSki_id':3, 'imageSki': 'rossignol_experience_84.png'},
   {'id' : 8 ,'modeleSki':'Salomon Max 8S', 'dateAchat':'2017-02-11', 'etat':'Très Bon', 'prixAchat':'500', 'prixLocation':'50', 'taille':'165', 'typeSki_id':3, 'imageSki': 'salomon_max_8s.png'},
   {'id' : 9 ,'modeleSki':'Atomic Vantage 77 TI', 'dateAchat':'2019-05-20', 'etat':'Bon', 'prixAchat':'420', 'prixLocation':'41', 'taille':'156', 'typeSki_id':3, 'imageSki': 'atomic_vantage_77_ti.jpg'},
   {'id' : 10 ,'modeleSki':'Dynastar Vertical Deer', 'dateAchat':'2017-11-25', 'etat':'Mauvais', 'prixAchat':'697', 'prixLocation':'22', 'taille':'180', 'typeSki_id':4, 'imageSki': 'dynastar_vertical_deer.jpg'},
   {'id' : 11 ,'modeleSki':'Elan Ripstick 96', 'dateAchat':'2020-04-16', 'etat':'Très Bon', 'prixAchat':'490', 'prixLocation':'42', 'taille':'181', 'typeSki_id':6, 'imageSki': 'elan_ripstick_96.jpg'},
   {'id' : 12 ,'modeleSki':'Salomon Distance M10 GW L90', 'dateAchat':'2019-08-30', 'etat':'Neuf', 'prixAchat':'299', 'prixLocation':'34', 'taille':'125', 'typeSki_id':1, 'imageSki': 'salomon_distance_m10_gw_l90.jpg'},
   {'id' : 13 ,'modeleSki':'Rossignol Freeze Xpress GW', 'dateAchat':'2020-01-04', 'etat':'Très Bon', 'prixAchat':'269', 'prixLocation':'21', 'taille':'118', 'typeSki_id':1, 'imageSki': 'rossignol_freeze_xpress_gw.jpg'},
]

@app.route('/')
def show_accueil():
    return render_template('layout.html')


@app.route('/type-ski/show')
def show_type_ski():
    #print(types_skis)
    return render_template('type_ski/show_type_ski.html', types_skis=typeSki)

@app.route('/type-ski/add', methods=['GET'])
def add_type_ski():
    return render_template('type_ski/add_type_ski.html')

@app.route('/type-ski/add', methods=['POST'])
def valid_add_type_ski():
    libelleType = request.form.get('libelleType', '')
    print(u'type ajouté , libelleType :', libelleType)
    message = u'type ajouté , libelleType :'+libelleType
    flash(message, 'alert-success')
    return redirect('/type-ski/show')


@app.route('/type-ski/delete', methods=['GET'])
def delete_type_ski():
    id = request.args.get('id', '')
    print ("un type d'ski supprimé, id :",id)
    message=u'un type d\'ski supprimé, id : ' + id
    flash(message, 'alert-warning')
    return redirect('/type-ski/show')

@app.route('/type-ski/edit', methods=['GET'])
def edit_type_ski():
    id = request.args.get('id', '')
    id=int(id)
    type_ski = typeSki[id-1]
    return render_template('type_ski/edit_type_ski.html', type_ski=type_ski)

@app.route('/type-ski/edit', methods=['POST'])
def valid_edit_type_ski():
    libelleType = request.form.get('libelleType', '')
    id = request.form.get('id', '')
    print(u'type ski modifié, id: ',id, " libelleType :", libelleType)
    message=u'type ski modifié, id: ' + id + " libelleType : " + libelleType
    flash(message, 'alert-success')
    return redirect('/type-ski/show')
@app.route('/ski/show')
def show_ski():
    # print(skis)
    return render_template('ski/show_ski.html', skis=skis)

@app.route('/ski/add', methods=['GET'])
def add_ski():
    return render_template('ski/add_ski.html', types_skis=typeSki)

@app.route('/ski/add', methods=['POST'])
def valid_add_ski():
    modeleSki = request.form.get('modeleSki', '')
    typeSki_id = request.form.get('typeSki_id', '')
    prixAchat = request.form.get('prixAchat', '')
    prixLocation = request.form.get('prixLocation', '')
    etat = request.form.get('etat', '')
    dateAchat = request.form.get('dateAchat', '')
    taille = request.form.get('taille', '')
    description = request.form.get('description', '')
    image = request.form.get('image', '')
    message = u'ski ajouté , modeleSki: '+ modeleSki + '---- typeSki : ' + typeSki_id + ' ---- prixAchat: ' + prixAchat + '---prixLocation: ' + prixLocation + '---etat: ' + etat + ' - dateAchat: '+  dateAchat + ' - description:' + description + '------taille: '+ taille+  ' - image:' + image
    print(message)
    flash(message, 'alert-success')
    return redirect('/ski/show')

@app.route('/ski/delete', methods=['GET'])
def delete_ski():
    id = request.args.get('id', '')
    message=u'un ski supprimé, id : ' + id
    flash(message, 'alert-warning')
    return redirect('/ski/show')

@app.route('/ski/edit', methods=['GET'])
def edit_ski():
    id = request.args.get('id', '')
    id=int(id)
    ski = skis[id-1]
    return render_template('ski/edit_ski.html', ski=ski, types_skis=typeSki)

@app.route('/ski/edit', methods=['POST'])
def valid_edit_ski():
    id = request.form.get('id', '')
    nom = request.form.get('nom', '')
    type_ski_id = request.form.get('type_ski_id', '')
    prix = request.form.get('prix', '')
    stock = request.form.get('stock', '')
    description = request.form.get('description', '')
    image = request.form.get('image', '')
    message = u'ski modifié , nom:'+nom + '---- type_ski_id :' + type_ski_id + ' ---- prix:' + prix + ' - stock:'+  stock + ' - description:' + description + ' - image:' + image + u' ------ pour l ski d identifiant :' + id
    print(message)
    flash(message, 'alert-success')
    return redirect('/ski/show')

@app.route('/ski/filtre', methods=['GET'])
def show_filtre_ski():
    return render_template('ski/filtre_ski.html', skis=skis, types_skis=typeSki)


@app.route('/ski/filtre', methods=['POST'])
def valid_filtre_ski():
    types_select = request.form.getlist('typeSki')
    prix_min = request.form.get('prix_min', '')
    prix_max = request.form.get('prix_max', '')
    recherche = request.form.get('recherche', '')
    if types_select or prix_min or prix_max or recherche:
        flash(f"Types cochés : {types_select}", 'alert-info')
        flash(f"Prix min : {prix_min} | Prix max : {prix_max} | Recherche : {recherche}", 'alert-success')
    else:
        flash("Erreur : veuillez remplir au moins un champ ou cocher un type de ski.", 'alert-danger')
    return render_template('ski/filtre_ski.html', skis=skis, types_skis=typeSki)


if __name__ == '__main__':
    app.run()