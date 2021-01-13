# Random_ord_api
Skilar einu íslensku orði af handahófi undir endapunktinum "/random_ord". Gögnin eru geymd í textaskrám vegna þess að verkefnið var gert í flýti, ideally 
væri SQLite gagnagrunnur notaður. Gögnin eru skröpuð með generate_word_files() undir helpers.py og skipt niður í skrár þar sem hver skrá inniheldur að hámarki
15.000 orð. Endapunkturinn "/random_ord" velur eina af þeim textaskrám af handahófi og svo eitt orð úr þeirri textaskrá af handahófi og skilar.
