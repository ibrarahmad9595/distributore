from model.Distributore import Distributore

distributore = Distributore("Bibita");
distributore.aggiungiBevanda("A","Acqua",0.20);
distributore.aggiungiBevanda("B","Coca",0.30);
distributore.aggiungiBevanda("C","Birra",1.00);

distributore.getPrice("A");

#throw exception
# distributore.getNome("D");

distributore.caricaTessera(12,5.5)
distributore.caricaTessera(21,10.0)
distributore.caricaTessera(99,0.75)

#throw exception
# distributore.leggiCredito(22)

distributore.aggiornaColonna("Acqua",40)
distributore.aggiornaColonna("Coca",1)
distributore.aggiornaColonna("Birra",50)

distributore.erogaBibita("A",12)