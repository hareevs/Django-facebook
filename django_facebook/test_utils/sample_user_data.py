

user_data = {}

base_data = dict(image='http://u.fashiocdn.com/images/users/0/0/6/O/J/5.jpg',
                 image_thumb='http://u.fashiocdn.com/images/users/0/0/6/O/J/5.jpg')
user_data['no_email'] = {'first_name': 'Thierry', 'last_name': 'Schellenbach', 'verified': True, 'name': 'Thierry Schellenbach', 'gender': 'man', 'image': 'http://graph.facebook.com/me/picture?type=large', 'updated_time':
                         '2010-04-01T14:26:55+0000', 'birthday': '04/07', 'link': 'http://www.facebook.com/profile.php?id=1225707780', 'location': {'id': None, 'name': None}, 'timezone': -5, 'id': '1225707780', 'image_thumb': 'http://graph.facebook.com/me/picture'}
user_data[
    'tschellenbach'] = {'email': 'fake@mellowmorning.com', 'first_name': 'Thierry', 'last_name': 'Schellenbach', 'verified': True, 'name': 'Thierry Schellenbach', 'gender': 'man', 'image': 'http://graph.facebook.com/me/picture?type=large',
                        'updated_time': '2010-04-01T14:26:55+0000', 'birthday': '04/07', 'link': 'http://www.facebook.com/profile.php?id=1225707780', 'location': {'id': None, 'name': None}, 'timezone': -5, 'id': '1225707780', 'image_thumb': 'http://graph.facebook.com/me/picture'}
user_data[
    'new_user'] = {'email': 'fake_new@mellowmorning.com', 'first_name': 'Thierry', 'last_name': 'Schellenbach', 'verified': True, 'name': 'Thierry Schellenbach', 'gender': 'male', 'image': 'http://graph.facebook.com/me/picture?type=large',
                   'updated_time': '2010-04-01T14:26:55+0000', 'birthday': '04/07', 'link': 'http://www.facebook.com/profile.php?id=1225707780', 'location': {'id': None, 'name': None}, 'timezone': -5, 'id': '1225707781', 'image_thumb': 'http://graph.facebook.com/me/picture'}
user_data[
    'no_birthday'] = {'website': 'www.pytell.com', 'first_name': 'Jonathan', 'last_name': 'Pytell', 'verified': True, 'name': 'Jonathan Pytell', 'image': 'http://graph.facebook.com/me/picture?type=large',
                      'updated_time': '2010-01-01T18:13:17+0000', 'link': 'http://www.facebook.com/jpytell', 'location': {'id': None, 'name': None}, 'timezone': -4, 'id': '776872663', 'image_thumb': 'http://graph.facebook.com/me/picture'}
user_data['partial_birthday'] = {'first_name': 'Thierry', 'last_name': 'Schellenbach', 'verified': True, 'name': 'Thierry Schellenbach', 'gender': 'man', 'image': 'http://graph.facebook.com/me/picture?type=large', 'updated_time':
                                 '2010-04-01T14:26:55+0000', 'birthday': '04/07', 'link': 'http://www.facebook.com/profile.php?id=1225707780', 'location': {'id': None, 'name': None}, 'timezone': -5, 'id': '1225707780', 'image_thumb': 'http://graph.facebook.com/me/picture'}
user_data[
    'short_username'] = {'email': 'f@mellowmorning.com', 'first_name': 'Thierry', 'last_name': 'Schellenbach', 'verified': True, 'name': 'Thierry Schellenbach', 'gender': 'man', 'image': 'http://graph.facebook.com/me/picture?type=large',
                         'updated_time': '2010-04-01T14:26:55+0000', 'birthday': '04/07', 'link': 'http://www.facebook.com/profile.php?id=1225707780', 'location': {'id': None, 'name': None}, 'timezone': -5, 'id': '1225707782', 'image_thumb': 'http://graph.facebook.com/me/picture'}
user_data[
    'long_username'] = {'email': 'superduperlongusernamemorethan30characters@mellowmorning.com', 'first_name': 'Thierry123456789123456789123456789123456789123456789123456789123456789123456789123456789', 'last_name': 'Schellenbach123456789123456789123456789123456789123456789123456789', 'verified': True, 'name': 'Thierry Schellenbach',
                        'gender': 'man', 'image': 'http://graph.facebook.com/me/picture?type=large', 'updated_time': '2010-04-01T14:26:55+0000', 'birthday': '04/07', 'link': 'http://www.facebook.com/profile.php?id=1225707780', 'location': {'id': None, 'name': None}, 'timezone': -5, 'id': '1225707782', 'image_thumb': 'http://graph.facebook.com/me/picture'}

user_data['same_username'] = user_data['short_username'].copy()
user_data['same_username'].update(dict(id='1111111', email='t@fake.com'))

user_data['paul'] = {"website": "http://usabilla.com", "last_name": "Veugen", "locale": "en_US", "image": "https://graph.facebook.com/me/picture?access_token=aa&type=large", "quotes": "\"Make no small plans for they have no power to stir the soul.\"  - Machiavelli", "timezone": 1, "education": [{"school": {"id": "114174235260224", "name": "Tilburg University"}, "type": "College", "year": {"id": "136328419721520", "name": "2009"}}, {"school": {"id": "111600322189438", "name": "Tilburg University"}, "type": "Graduate School", "concentration": [{"id": "187998924566551", "name": "Business Communication and Digital Media"}, {"id": "105587479474873", "name": "Entrepreneurship"}], "degree": {"id": "110198449002528", "name": "BA"}}], "id": "555227728", "first_name": "Paul", "verified": True, "sports": [{"id": "114031331940797", "name": "Cycling"}, {"id": "107496599279538", "name": "Snowboarding"}, {"id": "109368782422374", "name": "Running"}], "languages": [{"id": "106059522759137", "name": "English"}, {"id": "107672419256005", "name": "Dutch"}], "location": {
    "id": "111777152182368", "name": "Amsterdam, Netherlands"}, "image_thumb": "https://graph.facebook.com/me/picture?access_token=aa", "email": "paulv@email.com", "username": "pveugen", "bio": "Founder Usabilla. User Experience designer, entrepeneur and digital media addict. On a mission to make user experience research simple and fun with Usabilla.com.", "birthday": "07/11/1984", "link": "http://www.facebook.com/pveugen", "name": "Paul Veugen", "gender": "male", "work": [{"description": "http://usabilla.com", "employer": {"id": "235754672838", "name": "Usabilla"}, "location": {"id": "111777152182368", "name": "Amsterdam, Netherlands"}, "position": {"id": "130899310279007", "name": "Founder, CEO"}, "with": [{"id": "1349358449", "name": "Marc van Agteren"}], "start_date": "2009-01"}, {"position": {"id": "143357809027330", "name": "Communication Designer"}, "start_date": "2000-02", "location": {"id": "112258135452858", "name": "Venray"}, "end_date": "2010-01", "employer": {"id": "133305113393672", "name": "Flyers Internet Communicatie"}}], "updated_time": "2011-11-27T14:34:34+0000"}

user_data['paul2'] = user_data['paul']
user_data[
    'unicode_string'] = {'bio': 'ATELIER : TODOS LOS DIAS DE 14 A 22 HS C CITA PREVIA. MIX DE ESTETICAS - ECLECTICA - PRENDAS UNICAS-HAND MADE- SEASSON LESS RETROMODERNIDAD -CUSTOMIZADO !!!\r\n\r\nMe encanta todo el proceso que lleva lograr un objeto que sea unico....personalizarlo de acuerdo a cada uno...a cada persona....a su forma de ser.......elegir los materiales, los avios, las telas...siendo la premisa DIFERENCIARSE!!!!\r\n Atemporal..Retro modernidad...Eclecticismo!!!',
                         'birthday': '04/09/1973',
                         'education': [{'classes': [{'description': 'direccion de arte',
                                                       'id': '188729917815843',
                                                       'name': 'AAAP'},
                                                      {'id': '200142039998266',
                                                       'name': 'Indumentaria',
                                                       'with': [{'id': '546455670',
                                                                  'name': 'Gustavo Lento'}]},
                                                      {'description': 'dise\xf1o ',
                                                       'id': '102056769875267',
                                                       'name': 'figurin',
                                                       'with': [{'id': '1285841477',
                                                                  'name': 'La Maison Madrid'}]},
                                                      {'id': '194463713907701',
                                                       'name': 'indumentaria -figurin-seriado'},
                                                      {'id': '180792848632395',
                                                       'name': 'indumentaria-figurin -seriado.etc',
                                                       'with': [{'id': '704003068',
                                                                  'name': 'Mariano Toledo'}]}],
                                         'concentration': [{'id': '176664472378719',
                                                             'name': 'indumentaria y dise\xf1o textil'}],
                                         'school': {'id': '115805661780893',
                                                     'name': 'uba arquitectura dise\xf1o y urbanismo'},
                                         'type': 'College'},
                                        {'classes': [{'id': '116042535136769',
                                                       'name': 'whadrove asesory'}],
                                         'concentration': [{'id': '146715355391868',
                                                             'name': 'producer-  stylist -  asesora de imagen -personal-shooper -whadrove asesory'}],
                                         'school': {'id': '107827585907242',
                                                     'name': 'Miami International University of Art & Design'},
                                         'type': 'Graduate School'},
                                        {'classes': [{'id': '199608053396849',
                                                       'name': 'Reporter, Producer and Director'},
                                                      {'id': '209828275699578',
                                                       'name': 'personal shooper'},
                                                      {'id': '208913322452336',
                                                       'name': 'Designer-stylisti'}],
                                            'concentration': [{'id': '184808144897752',
                                                                'name': 'whadrobing'}],
                                            'school': {'id': '105548239478812',
                                                        'name': 'New York Institute of Technology'},
                                            'type': 'College'},
                                        {'school': {'id': '106431826058746',
                                                     'name': 'Colegio Nuestra Se\xf1ora de la Misericordia'},
                                         'type': 'High School'},
                                        {'school': {'id': '106011862771707',
                                                     'name': 'Mary E. Graham'},
                                         'type': 'High School'},
                                        {'school': {'id': '106011862771707',
                                                     'name': 'Mary E. Graham'},
                                         'type': 'High School'}],
                         'email': 'notfersharerringemail@hotmail.com',
                         'first_name': 'Fernanda',
                         'gender': 'female',
                         'hometown': {'id': '109238842431095',
                                       'name': 'La Coru\xf1a, Galicia, Spain'},
                         'id': '1157872766',
                         'image': 'https://graph.facebook.com/me/picture?type3Dlarge&access_token3D100314226679773|2.1ZkFz1Cusu5RlY1xGft_Pg__.86400.1303534800.4-1157872766|ZgsRrRYwp2pqHEHtncqS5-rBiSg',
                         'image_thumb': 'https://graph.facebook.com/me/picture?access_token3D100314226679773|2.1ZkFz1Cusu5RlY1xGft_Pg__.86400.1303534800.4-1157872766|ZgsRrRYwp2pqHEHtncqS5-rBiSg',
                         'languages': [{'id': '111021838921932', 'name': 'Espa\xf1ol'},
                                        {'id': '110867825605119',
                                         'name': 'Ingles'},
                                        {'id': '108083115891989',
                                         'name': 'Portugu\xe9s'},
                                        {'id': '113051562042989', 'name': 'Italiano'}],
                         'last_name': 'Ferrer Vazquez',
                         'link': 'http://www.facebook.com/FernandaFerrerVazquez',
                         'locale': 'es_LA',
                         'location': {'id': '106423786059675', 'name': 'Buenos Aires, Argentina'},
                         'name': 'Fernanda Ferrer Vazquez',
                         'timezone': -3,
                         'updated_time': '2011-04-22T04:28:27+0000',
                         'username': 'FernandaFerrerVazquez',
                         'verified': True,
                         'website': 'http://fernandaferrervazquez.blogspot.com/\r\nhttp://twitter.com/fferrervazquez\r\nhttp://comunidad.redfashion.es/profile/fernandaferrervazquez\r\nhttp://www.facebook.com/group.php?gid3D40257259997&ref3Dts\r\nhttp://fernandaferrervazquez.spaces.live.com/blog/cns!EDCBAC31EE9D9A0C!326.trak\r\nhttp://www.linkedin.com/myprofile?trk3Dhb_pro\r\nhttp://www.youtube.com/account#profile\r\nhttp://www.flickr.com/\r\n Mi galer\xeda\r\nhttp://www.flickr.com/photos/wwwfernandaferrervazquez-showroomrecoletacom/ \r\n\r\nhttp://www.facebook.com/pages/Buenos-Aires-Argentina/Fernanda-F-Showroom-Recoleta/200218353804?ref3Dts\r\nhttp://fernandaferrervazquez.wordpress.com/wp-admin/',
                         'work': [{'description': 'ATELIER : un mix de esteticas que la hacen eclectica, multicultural, excentrica, customizada, artesanal, unica , exclusiva, lujosa, eco-reciclada,con bordados a mano y texturas..especial atencion a los peque\xf1os detalles!!!! \nSeason less \nHand made ',
                                    'employer': {'id': '113960871952651',
                                                  'name': 'fernanda ferrer vazquez'},
                                    'location': {'id': '106423786059675',
                                                  'name': 'Buenos Aires, Argentina'},
                                    'position': {'id': '145270362165639',
                                                  'name': 'Dise\xf1adora'},
                                    'projects': [{'description': 'produccion-estilismo-fotografia-make up-pelo-asesoramiento de imagen-whadrobing-perso\xf1an shooper-rent an outfit!!',
                                                   'id': '200218353804',
                                                   'name': 'Fernanda F -Showroom Recoleta'}],
                                    'start_date': '2008-12'},
                                   {'employer': {'id': '198034683561689',
                                                  'name': 'el atelier de la isla'}}]}

for k, v in user_data.items():
    v.update(base_data)
