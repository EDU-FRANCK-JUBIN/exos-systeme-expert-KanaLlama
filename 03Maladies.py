# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:52:09 2019

@author: Margot
"""


from pyDatalog import pyDatalog
pyDatalog.clear()
pyDatalog.create_terms('X, P,G001,G002,G003,G004,G005,G006,G007,G008,G009,G010,G011,G012,G013,G014,G015,G016,G017,G018,G019,G020, \
                       G021,G022, G023,Paupière rouge,Paupière enflée,Douleur oculaire et démangeaisons,\
                       La saleté oculaire est collante et dépend des cils,Ressentir une gêne et des douleurs oculaires,\
                       Douleur quand on presse,Bosse sur les paupières dans quelques semaines,Indolore lorsqu il est pressé,\
                       Il y a un peu de poussière dans loeil,Yeux rouges,Les yeux sont un peu irritants et douloureux,\
                       Maux de gorge et fièvre,Yeux qui piquent,Yeux enflés et douloureux,Yeux larmoyants,Les yeux brillent,\
                       Les yeux brillent,Douleur oculaire,Vision diminuée,Sensation de douleur légère à sévère,Yeux sales,\
                       Douleur intense,Yeux enflés difficiles à ouvrir,')


load("""
""")


P01(X) <= G001(X) & G002(X) & G003(X) & G004(X)
P02(X) <= G001(X) & G002(X) & G005(X) & G006(X)
P03(X) <= G007(X) & G008(X)
P04(X) <= G009(X) & G010(X) & G011(X) & G012(X)
P05(X) <= G013(X) & G014(X) & G015(X) & G016(X) 
P06(X) <= G010(X) & G015(X) & G016(X) & G017(X) & G018(X) & G019(X) 
P07(X) <= G010(X) & G019(X) & G020(X) & G021(X) 
P08(X) <= G001(X) & G010(X) & G022(X) & G023(X) 

pyDatalog.assert_fact('G001', 'Paupière rouge')
pyDatalog.assert_fact('G002', 'Paupière enflée')
pyDatalog.assert_fact('G003', 'Douleur oculaire et démangeaisons')
pyDatalog.assert_fact('G004', 'La saleté oculaire est collante et dépend des cils')
pyDatalog.assert_fact('G005', 'Ressentir une gêne et des douleurs oculaires')
pyDatalog.assert_fact('G006', 'Douleur quand on presse')
pyDatalog.assert_fact('G007', 'Bosse sur les paupières dans quelques semaines')
pyDatalog.assert_fact('G008', 'Indolore lorsqu il est pressé')
pyDatalog.assert_fact('G009', 'Il y a un peu de poussière dans l oeil')
pyDatalog.assert_fact('G010', 'Yeux rouges')
pyDatalog.assert_fact('G011', 'Les yeux sont un peu irritants et douloureux')
pyDatalog.assert_fact('G012', 'Maux de gorge et fièvre')
pyDatalog.assert_fact('G013', 'Yeux qui piquent')
pyDatalog.assert_fact('G014', 'Yeux enflés et douloureux')
pyDatalog.assert_fact('G015', 'Yeux larmoyants')
pyDatalog.assert_fact('G016', 'Les yeux brillent')
pyDatalog.assert_fact('G017', 'Les yeux brillent')
pyDatalog.assert_fact('G018', 'Douleur oculaire')
pyDatalog.assert_fact('G019', 'Vision diminuée')
pyDatalog.assert_fact('G020', 'Sensation de douleur légère à sévère')
pyDatalog.assert_fact('G021', 'Yeux sales')
pyDatalog.assert_fact('G022', 'Douleur intense')
pyDatalog.assert_fact('G023', 'Yeux enflés difficiles à ouvrir')


pyDatalog.assert_fact('P01', 'Blépharite', 'Elle est causée par des allergies à la poussière, à la fumée, \
                      à des produits chimiques et à des bactéries staphylococciques, \
                      alpha streptocoques ou bêta-hémolytiques , - Compression de sels physiologiques \
                      Fourniture dantibiotiques, - \
                      favorise la propreté de la zone autour des yeux et les mains si vous voulez toucher les yeux.')

pyDatalog.assert_fact('P02', 'Orgelet de prévention ', 'Causée par une inflammation superative des glandes des paupières , \
                      Compressez à leau tiède -Donnez une pommade antibiotique -\
                      Donnez des antibiotiques systémiques -Donnez une protection anti-douleur,\
                      - Conservez la propreté de la zone environnante les yeux et les mains si vous voulez toucher les yeux.  \
                      Évitez les facteurs qui provoquent des allergies.')

pyDatalog.assert_fact('P03', 'Chalazion', 'Causée par une inflammation chronique \
                      de la granulomatose des glandes de Meibomian bloquées , \
                      étant donné une incision , - maintenir nettoyer la zone autour des yeux et \
                      des mains quand ils veulent toucher les yeux.')

pyDatalog.assert_fact('P04', 'Conjonctiviste viral', 'Inflammation de la conjonctive causée par le virus, \
                      -Avec ladministration dantibiotiques systomatiques et ,\
                      -Le maintien de létat corporel (propreté) - \
                      Le contact avec les personnes atteintes dune maladie des yeux')

pyDatalog.assert_fact('P05', 'Conjonctiviste en allergie', 'Causée par la conjonctive en raison de réactions allergiques \
                      à des non-infections, \
                      -En fournissant anti-allergique topique et systématique.,\
                      - gardez la zone autour des yeux et des mains propre lorsque vous souhaitez toucher les yeux.\
                      -Évitez les facteurs allergiques.')

pyDatalog.assert_fact('P06', 'Kératite', 'Causé en raison dune inflammation de la cornée, \
                      En fournissant des déchirures artificielles, \
                      des antibiotiques et des cycloplégiques., \
                      -En interdisant lutilisation de lentilles de contact ou en assurant la procédure dinstallation et \
                      le retrait des lentilles de contact selon les règles en vigueur. \
                      Utiliser une protection oculaire tout en continuant fonctionne principalement en ce qui \
                      concerne avec les rayons UV.')

pyDatalog.assert_fact('P07', 'Ulcère cornéen', 'Il sagit dune infection résultant dune \
                      infection bactérienne pathogène à Gram négatif de la cornée , \
                      étant donné des antibiotiques cycloplégiques et topiques et sous-conjonctivaux, - \
                      Utilisez des protections oculaires. -Évitez les lentilles de contact.')

pyDatalog.assert_fact('P08', 'Endophtalmie', 'Causée pour cause dinfection après un traumatisme ou une intervention chirurgicale, \
                      ou endogène en raison dune sepsie , \
                      Dans lhospitalisation  antibiotiques systémiques (perfusion / injection)  gouttes Antibiotica anti-douleur,\
                      Maintenir la propreté la zone autour des yeux et des mains quand ils veulent toucher les yeux')

query = 'p03(X)'
answers = pyDatalog.ask(query).answers 
print(answers)