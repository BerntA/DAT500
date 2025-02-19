#!/usr/bin/python3

import sys

MUNICIPALITIES_TO_MODERN = {"Sarpsborg":"Sarpsborg","Fredrikstad":"Fredrikstad","Moss":"Moss","Hvaler":"Hvaler","Berg":"Berg","Aremark":"Aremark","Rømskog":"Rømskog","Trøgstad":"Trøgstad","Spydeberg":"Spydeberg","Askim":"Askim","Eidsberg":"Eidsberg","Skiptvet":"Skiptvet","Rakkestad":"Rakkestad","Råde":"Råde","Rygge":"Rygge","Hobøl":"Hobøl","Moss":"Moss","Vestby":"Vestby","Ås":"Ås","Frogn":"Frogn","Nesodden":"Nesodden","Bærum":"Bærum","Asker":"Asker","Sørum":"Sørum","Fet":"Fet","Enebakk":"Enebakk","Lørenskog":"Lørenskog","Skedsmo":"Skedsmo","Nittedal":"Nittedal","Gjerdrum":"Gjerdrum","Ullensaker":"Ullensaker","Eidsvoll":"Eidsvoll","Nannestad":"Nannestad","Hurdal":"Hurdal","Hamar":"Hamar","Kongsvinger":"Kongsvinger","Ringsaker":"Ringsaker","Vang":"Vang","Løten":"Løten","Stange":"Stange","Nord-Odal":"Nord-Odal","Sør-Odal":"Sør-Odal","Eidskog":"Eidskog","Grue":"Grue","Hof":"Holmestrand","Åsnes":"Åsnes","Elverum":"Elverum","Trysil":"Trysil","Åmot":"Åmot","Stor-Elvdal":"Stor-Elvdal","Tolga":"Tolga","Tynset":"Tynset","Lillehammer":"Lillehammer","Gjøvik":"Gjøvik","Dovre":"Dovre","Lesja":"Lesja","Skjåk":"Skjåk","Lom":"Lom","Vågå":"Vågå","Sel":"Sel","Nord-Fron":"Nord-Fron","Sør-Fron":"Sør-Fron","Ringebu":"Ringebu","Øyer":"Øyer","Østre Toten":"Østre Toten","Vestre Toten":"Vestre Toten","Jevnaker":"Jevnaker","Lunner":"Lunner","Gran":"Gran","Søndre Land":"Søndre Land","Nordre Land":"Nordre Land","Sør-Aurdal":"Sør-Aurdal","Etnedal":"Etnedal","Nord-Aurdal":"Nord-Aurdal","Vestre Slidre":"Vestre Slidre","Øystre Slidre":"Øystre Slidre","Vang":"Vang","Drammen":"Drammen","Kongsberg":"Kongsberg","Hole":"Hole","Flå":"Flå","Gol":"Gol","Hemsedal":"Hemsedal","Ål":"Ål","Hol":"Hol","Sigdal":"Sigdal","Krødsherad":"Krødsherad","Modum":"Modum","Øvre Eiker":"Øvre Eiker","Nedre Eiker":"Nedre Eiker","Lier":"Lier","Røyken":"Røyken","Hurum":"Hurum","Flesberg":"Flesberg","Rollag":"Rollag","Svelvik":"Svelvik","Holmestrand":"Holmestrand","Horten":"Horten","Tønsberg":"Tønsberg","Sandefjord":"Sandefjord","Larvik":"Larvik","Andebu":"Sandefjord","Stokke":"Sandefjord","Nøtterøy":"Færder","Tjøme":"Færder","Lardal":"Larvik","Kragerø":"Kragerø","Porsgrunn":"Porsgrunn","Skien":"Skien","Bamble":"Bamble","Drangedal":"Drangedal","Sauherad":"Sauherad","Tinn":"Tinn","Hjartdal":"Hjartdal","Seljord":"Seljord","Kviteseid":"Kviteseid","Nissedal":"Nissedal","Fyresdal":"Fyresdal","Vinje":"Vinje","Risør":"Risør","Tvedestrand":"Tvedestrand","Arendal":"Arendal","Grimstad":"Grimstad","Lillesand":"Lillesand","Gjerstad":"Gjerstad","Vegårshei":"Vegårshei","Froland":"Froland","Eide":"Eide","Birkenes":"Birkenes","Åmli":"Åmli","Iveland":"Iveland","Bygland":"Bygland","Valle":"Valle","Bykle":"Bykle","Kristiansand":"Kristiansand","Mandal":"Mandal","Farsund":"Farsund","Flekkefjord":"Flekkefjord","Vennesla":"Vennesla","Søgne":"Søgne","Åseral":"Åseral","Lyngdal":"Lyngdal","Hægebostad":"Hægebostad","Eigersund":"Eigersund","Sandnes":"Sandnes","Stavanger":"Stavanger","Haugesund":"Haugesund","Sokndal":"Sokndal","Sokndal":"Sokndal","Lund":"Lund","Bjerkreim":"Bjerkreim","Eigersund":"Eigersund","Klepp":"Klepp","Time":"Time","Gjesdal":"Gjesdal","Forsand":"Forsand","Strand":"Strand","Årdal":"Årdal","Hjelmeland":"Hjelmeland","Suldal":"Suldal","Sauda":"Sauda","Finnøy":"Finnøy","Rennesøy":"Rennesøy","Bokn":"Bokn","Tysvær":"Tysvær","Etne":"Etne","Sveio":"Sveio","Stord":"Stord","Fitjar":"Fitjar","Tysnes":"Tysnes","Kvinnherad":"Kvinnherad","Jondal":"Jondal","Eidfjord":"Eidfjord","Voss":"Voss","Fusa":"Fusa","Samnanger":"Samnanger","Austevoll":"Austevoll","Sund":"Sund","Fjell":"Fjell","Askøy":"Askøy","Modalen":"Modalen","Lindås":"Lindås","Austrheim":"Austrheim","Masfjorden":"Masfjorden","Bergen":"Bergen","Gulen":"Gulen","Solund":"Solund","Hyllestad":"Hyllestad","Vik":"Vik","Balestrand":"Balestrand","Leikanger":"Leikanger","Sogndal":"Sogndal","Aurland":"Aurland","Lærdal":"Lærdal","Årdal":"Årdal","Luster":"Luster","Askvoll":"Askvoll","Jølster":"Jølster","Førde":"Førde","Naustdal":"Naustdal","Bremanger":"Bremanger","Selje":"Selje","Eid":"Eid","Hornindal":"Hornindal","Gloppen":"Gloppen","Stryn":"Stryn","Ålesund":"Ålesund","Molde":"Molde","Kristiansund":"Kristiansund","Vanylven":"Vanylven","Ulstein":"Ulstein","Volda":"Volda","Ørsta":"Ørsta","Norddal":"Norddal","Stranda":"Stranda","Stordal":"Stordal","Ørskog":"Ørskog","Sykkylven":"Sykkylven","Skodje":"Skodje","Giske":"Giske","Haram":"Haram","Vestnes":"Vestnes","Eid":"Eid","Nesset":"Nesset","Aukra":"Aukra","Sandøy":"Sandøy","Fræna":"Fræna","Eide":"Eide","Gjemnes":"Gjemnes","Tingvoll":"Tingvoll","Sunndal":"Sunndal","Surnadal":"Surnadal","Rindal":"Rindal","Aure":"Aure","Halsa":"Halsa","Trondheim":"Trondheim","Hemne":"Hemne","Hitra":"Hitra","Ørland":"Ørland","Agdenes":"Agdenes","Rissa":"Indre Fosen","Bjugn":"Bjugn","Roan":"Roan","Osen":"Osen","Oppdal":"Oppdal","Rennebu":"Rennebu","Meldal":"Meldal","Orkdal":"Orkdal","Røros":"Røros","Flå":"Flå","Melhus":"Melhus","Klæbu":"Klæbu","Malvik":"Malvik","Selbu":"Selbu","Tydal":"Tydal","Levanger":"Levanger","Steinkjer":"Steinkjer","Namsos":"Namsos","Meråker":"Meråker","Stjørdal":"Stjørdal","Frosta":"Frosta","Leksvik":"Indre Fosen","Levanger":"Levanger","Verdal":"Verdal","Verran":"Verran","Namdalseid":"Namdalseid","Inderøy":"Inderøy","Lierne":"Lierne","Grong":"Grong","Høylandet":"Høylandet","Overhalla":"Overhalla","Fosnes":"Fosnes","Flatanger":"Flatanger","Vikna":"Vikna","Nærøy":"Nærøy","Leka":"Leka","Bodø":"Bodø","Narvik":"Narvik","Bindal":"Bindal","Vik":"Vik","Brønnøy":"Brønnøy","Vega":"Vega","Alstahaug":"Alstahaug","Vefsn":"Vefsn","Hattfjelldal":"Hattfjelldal","Nesna":"Nesna","Hemnes":"Hemnes","Lurøy":"Lurøy","Træna":"Træna","Rødøy":"Rødøy","Meløy":"Meløy","Gildeskål":"Gildeskål","Beiarn":"Beiarn","Saltdal":"Saltdal","Fauske":"Fauske","Sørfold":"Sørfold","Steigen":"Steigen","Hamarøy":"Hamarøy","Lødingen":"Lødingen","Tjeldsund":"Tjeldsund","Evenes":"Evenes","Værøy":"Værøy","Flakstad":"Flakstad","Vågan":"Vågan","Hadsel":"Hadsel","Øksnes":"Øksnes","Sortland":"Sortland","Harstad":"Harstad","Tromsø":"Tromsø","Kvæfjord":"Kvæfjord","Ibestad":"Ibestad","Lavangen":"Lavangen","Salangen":"Salangen","Bardu":"Bardu","Målselv":"Målselv","Sørreisa":"Sørreisa","Dyrøy":"Dyrøy","Tranøy":"Tranøy","Torsken":"Torsken","Berg":"Berg","Lenvik":"Lenvik","Balsfjord":"Balsfjord","Karlsøy":"Karlsøy","Lyngen":"Lyngen","Skjervøy":"Skjervøy","Nordreisa":"Nordreisa","Kvænangen":"Kvænangen","Hammerfest":"Hammerfest","Vardø":"Vardø","Vadsø":"Vadsø","Alta":"Alta","Loppa":"Loppa","Hasvik":"Hasvik","Hammerfest":"Hammerfest","Kvalsund":"Kvalsund","Måsøy":"Måsøy","Lebesby":"Lebesby","Vardø":"Vardø","Sør-Varanger":"Sør-Varanger","Fredrikshald":"Halden","Torsnes":"Fredrikstad","Borge":"Fredrikstad","Varteig":"Sarpsborg","Skjeberg":"Sarpsborg","Idd":"Halden","Øymark":"Marker","Rødenes":"Marker","Tune":"Sarpsborg","Glemmen":"Fredrikstad","Kråkerøy":"Fredrikstad","Onsøy":"Fredrikstad","Våler":"Våler (Østfold)","Son":"Vestby","Hvitsten":"Vestby","Drøbak":"Frogn","Hølen":"Vestby","Kråkstad":"Ski","Aker":"Oslo","Høland":"Aurskog-Høland","Setskog":"Aurskog-Høland","Aurskog":"Aurskog-Høland","Lillestrøm":"Skedsmo","Nes":"Nes (Akershus)","Feiring":"Eidsvoll","Kristiania":"Oslo","Furnes":"Ringsaker","Romedal":"Stange","Vinger":"Kongsvinger","Brandval":"Kongsvinger","Sollia":"Stor-Elvdal","Ytre Rendal":"Rendalen","Øvre Rendal":"Rendalen","Lille Elvedalen":"Alvdal","Kvikne":"Tynset","Heidal":"Sel","Østre Gausdal":"Gausdal","Vestre Gausdal":"Gausdal","Fåberg":"Lillehammer","Biri":"Gjøvik","Snertingdal":"Gjøvik","Vardal":"Gjøvik","Eina":"Vestre Toten","Kolbu":"Østre Toten","Brandbu":"Gran","Hønefoss":"Ringerike","Holmsbu":"Asker","Norderhov":"Ringerike","Ådal":"Ringerike","Ytre Sandsvær":"Kongsberg","Øvre Sandsvær":"Kongsberg","Nore":"Nore Og Uvdal","Uvdal":"Nore Og Uvdal","Åsgårdstrand":"Horten","Strømm":"Svelvik","Skoger":"Drammen","Sande":"Sande (Møre Og Romsdal)","Botne":"Holmestrand","Våle":"Re","Borre":"Horten","Ramnes":"Re","Sem":"Tønsberg","Sandar":"Sandefjord","Tjølling":"Larvik","Brunlanes":"Larvik","Hedrum":"Larvik","Fredriksvern":"Larvik","Langesund":"Bamble","Stathelle":"Bamble","Brevik":"Porsgrunn","Slemdal":"Oslo","Gjerpen":"Skien","Eidanger":"Porsgrunn","Skåtøy":"Kragerø","Sannidal":"Kragerø","Solum":"Porsgrunn","Holla":"Skien","Lunde":"Nome","Bø":"Bø (Telemark)","Heddal":"Bø (Telemark)","Gransherad":"Notodden","Hovin":"Notodden","Mo":"Tokke","Lårdal":"Tokke","Rauland":"Vinje","Søndeled":"Risør","Holt":"Tvedestrand","Dypvåg":"Tvedestrand","Flosta":"Arendal","Austre Moland":"Arendal","Øyestad":"Arendal","Tromøy":"Arendal","Hisøy":"Arendal","Fjære":"Grimstad","Landvik":"Grimstad","Vestre Moland":"Lillesand","Høvåg":"Lillesand","Gjøvdal":"Åmli","Tovdal":"Åmli","Mykland":"Birkenes","Herefoss":"Birkenes","Vegusdal":"Birkenes","Hornnes":"Evje Og Hornnes","Evje":"Evje Og Hornnes","Randesund":"Kristiansand","Oddernes":"Kristiansand","Tveit":"Kristiansand","Hægeland":"Vennesla","Øvrebø":"Vennesla","Halse Og Harkmark":"Mandal","Holum":"Mandal","Øyslebø":"Marnardal","Laudal":"Lindesnes","Finsland":"Songdalen","Bjelland":"Marnardal","Grindheim":"Audnedal","Nord-Audnedal":"Audnedal","Sør-Audnedal":"Audnedal","Spangereid":"Lindesnes","Austad":"Lyngdal","Kvås":"Lyngdal","Fjotland":"Kvinesdal","Liknes":"Kvinesdal","Feda":"Kvinesdal","Herad":"Farsund","Spind":"Farsund","Vanse":"Farsund","Hidra":"Flekkefjord","Gyland":"Flekkefjord","Bakke":"Flekkefjord","Tonstad":"Sirdal","Øvre Sirdal":"Sirdal","Skudeneshavn":"Karmøy","Kopervik":"Karmøy","Heskestad":"Eigersund","Helleland":"Eigersund","Ogna":"Hå","Varhaug":"Hå","Nærbø":"Hå","Høyland":"Sandnes","Håland":"Stavanger","Hetland":"Sandnes","Høle":"Sandnes","Fister":"Hjelmeland","Sand":"Suldal","Jelsa":"Suldal","Nedstrand":"Tysvær","Sjernarøy":"Finnøy","Mosterøy":"Rennesøy","Avaldsnes":"Karmøy","Åkra":"Karmøy","Skudenes":"Karmøy","Torvastad":"Karmøy","Skåre":"Haugesund","Skjold":"Vindafjord","Vats":"Vindafjord","Vikedal":"Vindafjord","Skånevik":"Etne","Fjelberg":"Kvinnherad","Vikebygd":"Sveio","Valestrand":"Sveio","Finnås":"Bømlo","Varaldsøy":"Kvinnherad","Strandebarm":"Jondal","Røldal":"Odda","Ullensvang":"Odda","Ulvik":"Ulvik","Granvin":"Voss","Vossestrand":"Voss","Evanger":"Voss","Kvam":"Kvam Herad","Hålandsdal":"Fusa","Strandvik":"Fusa","Os":"Os (Hordaland)","Fana":"Bergen","Haus":"Osterøy","Bruvik":"Osterøy","Hosanger":"Osterøy","Hamre":"Lindås","Åsane":"Bergen","Alversund":"Lindås","Herdla":"Askøy","Hjelme":"Øygarden","Manger":"Radøy","Årstad":"Bergen","Florø":"Flora","Brekke":"Gulen","Lavik":"Gulen","Kyrkjebø":"Høyanger","Borgund":"Ålesund","Hafslo":"Luster","Jostedal":"Luster","Ytre Holmedal":"Fjaler","Indre Holmedal":"Gaular","Vevring":"Naustdal","Kinn":"Bremanger","Sør-Vågsøy":"Vågsøy","Nord-Vågsøy":"Vågsøy","Davik":"Vågsøy","Breim":"Jølster","Innvik":"Stryn","Rovde":"Sande (Møre Og Romsdal)","Sande":"Sande (Møre Og Romsdal)","Herøy":"Sande (Møre Og Romsdal)","Vartdal":"Ørsta","Hjørundfjord":"Ørsta","Sunnylven":"Stranda","Vatne":"Haram","Borgund":"Ålesund","Roald":"Giske","Sylte":"Vestnes","Voll":"Rauma","Grytten":"Rauma","Hen":"Rauma","Veøy":"Rauma","Eresfjord Og Vistdal":"Molde","Bolsøy":"Molde","Bud":"Fræna","Kornstad":"Averøy","Kvernes":"Averøy","Bremsnes":"Averøy","Grip":"Kristiansund","Frei":"Kristiansund","Øre":"Gjemnes","Straumsnes":"Tingvoll","Øksendal":"Sunndal","Ålvundeid":"Sunndal","Stangvik":"Surnadal","Åsskard":"Surnadal","Valsøyfjord":"Halsa","Tustna":"Aure","Edøy":"Smøla","Fillan":"Hitra","Sør-Frøya":"Frøya","Nord-Frøya":"Frøya","Lensvik":"Agdenes","Stadsbygd":"Agdenes","Stjørna":"Indre Fosen","Jøssund":"Bjugn","Aa":"Rennebu","Å":"Rennebu","Stoksund":"Åfjord","Ålen":"Holtålen","Haltdalen":"Holtålen","Singsås":"Holtålen","Budal":"Midtre Gauldal","Støren":"Midtre Gauldal","Soknedal":"Midtre Gauldal","Horg":"Melhus","Hølonda":"Melhus","Leinstrand":"Trondheim","Byneset":"Trondheim","Buvik":"Skaun","Børseskogn":"Skaun","Børsa":"Skaun","Geitastrand":"Orkdal","Strinda":"Trondheim","Tiller":"Trondheim","Hegra":"Stjørdal","Lånke":"Stjørdal","Skatval":"Stjørdal","Åsen":"Levanger","Skogn":"Levanger","Ytterøy":"Levanger","Mosvik":"Inderøy","Beitstad":"Steinkjer","Sandvollan":"Inderøy","Røra":"Inderøy","Sparbu":"Steinkjer","Ogndal":"Steinkjer","Egge":"Steinkjer","Stod":"Steinkjer","Kvam":"Steinkjer","Snåsa":"Snåsa - Snåasen Tjielte","Vemundvik":"Namsos","Klinga":"Namsos","Kolvereid":"Nærøy","Foldereid":"Nærøy","Gravvik":"Nærøy","Mosjøen":"Vefsn","Velfjord":"Brønnøy","Tjøtta":"Alstahaug","Stamnes":"Vaksdal","Dønnes":"Dønna","Mo":"Rana","Skjerstad":"Bodø","Bodin":"Bodø","Kjerringøy":"Bodø","Nordfold":"Steigen","Leiranger":"Steigen","Tysfjord":"Narvik","Ankenes":"Narvik","Buksnes":"Vestvågøy","Borge":"Vestvågøy","Gimsøy":"Vågan","Dverberg":"Andøy","Trondenes":"Harstad","Bjarkøy":"Harstad","Hillesøy":"Tromsø","Malangen":"Balsfjord","Tromsøysund":"Tromsø","Helgøy":"Karlsøy","Sørfjord":"Tromsø","Kautokeino":"Kautokeino - Guovdageainnu Suohkan","Talvik":"Alta","Kjelvik":"Nordkapp","Kistrand":"Porsanger - Porsánjggu Gielda - Porsangin Komuuni","Karasjok":"Karasjok - Kárásjoga Gielda","Tana":"Tana - Deanu Gielda","Polmak":"Tana - Deanu Gielda","Nesseby":"Nesseby - Unjárgga Gielda","Nord-Varanger":"Vadsø"}

BIRTH_PLACE_REPLACE = {"Id":"Idd","Frhald":"Fredrikshald","Frstad":"Fredrikstad","Lillestm":"Lillestrøm","Armark":"Aremark","Christiania":"Kristiania","Mos":"Moss","Vos":"Voss","Ness":"Nes","Torvestad":"Torvastad","Skudesnes":"Skudenes","Skudesnshavn":"Skudenes","Åker":"Aker","Akrehavn":"Åkra","Akrehamn":"Åkra","Åkre":"Åkra","Åkrehavn":"Åkra","Ållesund":"Ålesund","Ållesud":"Ålesund","Ålaesund":"Ålesund","Ålesud":"Ålesund","Akerhus":"Aker","Akers":"Aker","Akersbyen":"Aker","Akersh":"Aker","Akershus":"Aker","Trondhjem":"Trondheim","Tronhjem":"Trondheim","Eidsvold":"Eidsvoll","Glemminge":"Fredrikstad","Stre Toten":"Østre Toten","Tnsberg":"Tønsberg","Troms":"Tromsø","Vre Eker":"Øvre Eiker","Vrdalen":"Verdal","Hland":"Håland","Eidskogen":"Eidskog","Brum":"Bærum","Sndre Odalen":"Sør-Odal","Nordre Odalen":"Nord-Odal","Sndre Land":"Søndre Land","Ibbestad":"Ibestad","Nedre Eker":"Nedre Eiker","Sandeherred":"Sandar","Asken":"Asker","Hevne":"Hemne","Orkedalen":"Orkdal","Tromsysund":"Tromsøysund","Kvinnherred":"Kvinnherad","Vre Rendalen":"Øvre Rendal","Hgsd":"Haugesund","Vefsen":"Vefsn","Fane":"Fana","Rros":"Røros","Bamle":"Bamble","Krager":"Kragerø","Volden":"Volda","Opdal":"Oppdal","Enebak":"Enebakk","Saude":"Sauda","Porsgrund":"Porsgrunn","Nordre Aurdal":"Nord-Aurdal","Jlster":"Jølster","Trgstad":"Trøgstad","Hitterdal":"Heddal","Hiland":"Hetland","Nordre Fron":"Frogn","Urskog":"Aurskog","Ntter":"Nøtterøy","Saltdalen":"Saltdal","Tingvold":"Tingvoll","Egersund Herred":"Eigersund","Egersund":"Eigersund","Tysvr":"Tysvær","Vads":"Vats","Hnefoss":"Hønefoss","Fredriksvrn":"Fredriksvern","Rldal":"Røldal","Nsseby":"Nesseby","Christiansand":"Kristiansand","Stjrdalen":"Stjørdal","Lillestrm":"Lillestrøm","Fredriksstad":"Fredrikstad","Gimsy":"Gimsøy","Nerstrand":"Nedstrand","Gjvik":"Gjøvik","Strinden":"Strinda","Fjeld":"Fjell","Rken":"Røyken","Iestad":"Ibestad","Rissen":"Rissa","Tolgen":"Tolga","Nordfrya":"Nord-Frøya","Bod":"Bodø","Ldingen":"Lødingen","Tnset":"Tynset","Surendalen":"Surnadal","Beitstaden":"Beitstad","Brnny":"Brønnøy","Frde":"Førde","Hamary":"Hamarøy","Sndre Aurdal":"Sør-Aurdal","Leksviken":"Leksvik","Rlandet":"Ørland","Risr":"Risør","Ksnes":"Øksnes","Sgne":"Søgne","Bindalen":"Bindal","Rindalen":"Rindal","Srum":"Sørum","Kristianssand":"Kristiansand","Sandns":"Sandnes","Fjre":"Fjære","Hollen":"Holla","Mely":"Meløy","Meldalen":"Meldal","Lyster":"Luster","Alten":"Alta","Srfold":"Sørfold","Drbak":"Drøbak","Lrdal":"Lærdal","Koppervik":"Kopervik","Målselven":"Målselv","Skåt":"Skåtøy","Ådalen":"Ådal","Daviken":"Davik","Storelvedalen":"Stor-Elvdal","Sndeled":"Søndeled","Krdsherred":"Krødsherad","Her":"Herad","Tjm":"Tjøme","Våge":"Tysnes","Tjlling":"Tjølling","Tjtta":"Tjøtta","Ier":"Lier","Rsten":"Værøy","Hitteren":"Hitra","Vikten":"Vikna","Indviken":"Innvik","Hery":"Herøy","Hammer":"Hamre","Dybvåg":"Dypvåg","Rdy":"Rødøy","Frnen":"Nord-Fron","Kvfjord":"Kvæfjord","Sndre Undal":"Sør-Audnedal","Sndre Fron":"Sør-Fron","Tanen":"Tana","Askvold":"Askvoll","Lesje":"Lesja","Skjervy":"Skjervøy","Vannelven":"Vanylven","Vard":"Vardø","Hurdalen":"Hurdal","Norddalen":"Norddal","Stre Gausdal":"Østre Gausdal","Austevold":"Austevoll","Skkelven":"Sykkylven","Stadsbygden":"Stadsbygd","Ytre Sandsvr":"Ytre Sandsvær","Stre Slidre":"Øystre Slidre","Snåsen":"Snåsa","Hjrundfjord":"Hjørundfjord","Sannikedal":"Sannidal","Soknedalen":"Soknedal","Skjrn":"Stjørna","Stren":"Støren","Vossestranden":"Vossestrand","Kråkery":"Kråkerøy","Etnedalen":"Etnedal","Stenkjr":"Steinkjer","Sydvaranger":"Sør-Varanger","Srreisa":"Sørreisa","Karlsy":"Karlsøy","Hgebostad":"Hægebostad","Trom":"Tromsø","Hvåg":"Høvåg","Sundalen":"Sunndal","Ytre Rendalen":"Ytre Rendal","Sunnelven":"Sunnylven","Srfrya":"Sør-Frøya","Hlandet":"Håland","S Odalen":"Sør-Odal","Rskog":"Ørskog","Snertingdalen":"Snertingdal","Tusteren":"Tustna","Kvnangen":"Kvænangen","Stranden":"Strand","Nittedalen":"Nittedal","Mås":"Måsøy","Halse":"Halse Og Harkmark","Bjarky":"Bjarkøy","Vegardsheien":"Vegårshei","Trany":"Tranøy","Stre Moland":"Austre Moland","Vre Sandsvr":"Øvre Sandsvær","Hillesy":"Hillesøy","Namdalseidet":"Namdalseid","Eresfjord Og Vistdalen":"Eresfjord Og Vistdal","Jssund":"Jøssund","Hornindalen":"Hornindal","Hedalen":"Heddal","Åsene":"Åsane","Helgy":"Helgøy","Gransherred":"Gransherad","V Toten":"Vestre Toten","Ytteren":"Ytterøy","Mosviken":"Mosvik","Ogne":"Søgne","Lensviken":"Lensvik","Randsund":"Randesund","Tydalen":"Tydal","Moster":"Mosterøy","Rennes":"Rennesøy","Mosjen":"Mosjøen","Dnnes":"Dønnes","Strmmen":"Strømm","Hle":"Høle","Vry":"Værøy","Rdenes":"Rødenes","Klingen":"Klinga","Srfjord":"Sørfjord","Brseskognen":"Børseskogn","Sndre Vågs":"Sør-Vågsøy","Nordre Vågs":"Nord-Vågsøy","Nordvaranger":"Nord-Varanger","Halså Og Hartmark":"Halse Og Harkmark","Hegre":"Frogn","Bols":"Bolsøy","Overhallen":"Overhalla","Meraker":"Meråker","Ekersund":"Eigersund"}

RELIGION_REPLACE = {"Intet Samfund":"Atheist","Uttraadt Intet Samfund":"Atheist","Uttraadt Intet Samf":"Atheist","Intet Samf":"Atheist","Udtraadt Intet Samfund":"Atheist","Udtraadt Intet Samf":"Atheist","Uttrdt Intet Samfund":"Atheist","Udtraat Intet Samfund":"Atheist","Uttraadt Intet S":"Atheist","Uttrdt Intet Samf":"Atheist","Intet Samfun":"Atheist","Uttraadt":"Atheist","Uttraat Intet Samf":"Atheist","Udtraadt":"Atheist","Udtraat":"Atheist","Utraadt Intet Samfund":"Atheist","Uttr Intet Samf":"Atheist","Utraat Intet Samfund":"Atheist","Intet":"Atheist","Uttraat Intet Samfund":"Atheist","Uttrdt":"Atheist","Uttrt Intet Samfund":"Atheist","Udtrdt Intet Samfund":"Atheist","Intet S":"Atheist","Uttraadt Int Samf":"Atheist","Udtr Intet Samf":"Atheist","Udtraadt Intet S":"Atheist","Uttraadt Intet Sf":"Atheist","Uttraadt I S":"Atheist","Utraat":"Atheist","Uttraadt Int S":"Atheist","Uttraat":"Atheist","Luttersk":"Lutheranism","Lutt Frikirke":"Lutheranism","Luttersk Frikirke":"Lutheranism","Lut Frikirke":"Lutheranism","Luteraner":"Lutheranism","Babtist":"Baptist","Baptistsamf":"Baptist","Baptistsamfundet":"Baptist","Baptistsamfund":"Baptist","Baptister":"Baptist","Katholik":"Catholism","nan":"Norwegian Church"}

def findBestCandidate(a):
    words = a.split()
    
    b = [MUNICIPALITIES_TO_MODERN[w] for w in words if w in MUNICIPALITIES_TO_MODERN]
    if len(b) != 0:
        return b[0]
        
    b = [BIRTH_PLACE_REPLACE[w] for w in words if w in BIRTH_PLACE_REPLACE]
    if len(b) != 0:
        return MUNICIPALITIES_TO_MODERN[b[0]]
        
    return None
    
def findUpdatedBirthPlace(a):
    a = a.strip().lower().replace('aa','å').title()
    if a in MUNICIPALITIES_TO_MODERN:
        return MUNICIPALITIES_TO_MODERN[a]
    elif a in BIRTH_PLACE_REPLACE:
        return MUNICIPALITIES_TO_MODERN[BIRTH_PLACE_REPLACE[a]]

    # Still nothing? Check word for word if we find any potential combo.
    candidate = findBestCandidate(a)
    if (candidate is None) and a.endswith('en'): # Do a quick check, if for ex Rendalen->Rendal
        candidate = findBestCandidate(a[:-2])
    
    return (candidate if candidate else a)

def cleanupFieldOfWork(r):
    if 'fisker' in r:
        return 'Fisher'
    
    if 'hustru' in r:
        return 'Housewife'
    
    if 'gaard' in r or 'gard' in r or 'gjter' in r or 'grdbruk' in r:
        return 'Farmer'
    
    if 'tjenestep' in r or 'hushj' in r:
        return 'Maid'
    
    return r.title()

def cleanupReligion(r):
    if r in RELIGION_REPLACE:
        return RELIGION_REPLACE[r]
    
    if 'Luthersk' in r or 'Lutersk' in r or 'Luth' in r or 'Lutheraner' in r:
        return 'Lutheranism'
    
    if 'Methodist' in r or 'Metodist' in r:
        return 'Methodism'
    
    if 'Adventist' in r:
        return 'Adventism'
    
    if 'Katholsk' in r or 'Katolik' in r or 'Katolsk' in r:
        return 'Catholism'
    
    if 'Frimenig' in r or 'Frikirke' in r:
        return 'Evangelical Lutheran Free Church'
    
    if 'Kristi' in r:
        return 'Kristi Menighet'
    
    if 'Mormon' in r:
        return 'Mormon'
    
    if 'Mosaisk' in r:
        return 'Jew'
    
    if 'Dissenter' in r or 'Desenter' in r or 'Disenter' in r:
        return 'Dissenter'
    
    if 'Samfundet' in r or 'samfundet' in r:
        return 'Quakers'
    
    return r.title()

# INDEXES
# 0 - Census Year
# 1 - County
# 2 - Municipality
# 3 - Gender
# 4 - Field of Work
# 5 - Martial Status
# 6 - Religion/Faith
# 7 - Birth Year
# 8 - Birth Place (Municipality)

#sys.stdin.reconfigure(encoding='utf-8') # Ensure correct encoding.

for line in sys.stdin:
    line = line.strip()
    try:
        line = [str(s) for s in line.split(',')]
    except:
        continue

    if len(line) != 9:
        continue

    # Update municipality name to todays municipality name.
    line[2] = line[2].title()
    if line[2] in MUNICIPALITIES_TO_MODERN:
        line[2] = MUNICIPALITIES_TO_MODERN[line[2]]
    
    # Preprocess birthplaces and find the 'todays' municipality from the preprocessed birth place.
    line[-1] = findUpdatedBirthPlace(line[-1])

    # Preprocess field of work.
    # Fix typos and casings.
    line[4] = cleanupFieldOfWork(line[4].lower())

    # Preprocess religion.
    # Fix faulty abbrevations and typos.
    line[6] = cleanupReligion(line[6])

    print(",".join(line[2:]))
