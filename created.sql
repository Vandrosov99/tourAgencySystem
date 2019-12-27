CREATE TABLE client
( id_client integer primary key,
 surname varchar(45) not null
);
CREATE TABLE description_client
( id_client integer NOT NULL UNIQUE,
 phone varchar(25) NOT NULL,
 passport_number varchar(45) not null,
 sex varchar(15) not null,
 address varchar(35) not null
);
 ALTER TABLE description_client
    ADD FOREIGN KEY(id_client)
    REFERENCES client(id_client);

CREATE TABLE Employer
( id_emp integer PRIMARY KEY not null,
 surname varchar(45) not null
);
CREATE TABLE description_emp
( id_emp integer not null UNIQUE,
 phone varchar(25) NOT NULL,
 passport_number varchar(45) not null,
 sex varchar(15) not null,
 address varchar(35) not null,
 FOREIGN KEY (id_emp) REFERENCES Employer(id_emp)
 );
CREATE TABLE post 
( id_post integer PRIMARY KEY,
 category varchar(25) NOT NULL
);
CREATE TABLE status_post
( id_post integer not null,
 id_emp integer not null UNIQUE,
 FOREIGN KEY(id_post) REFERENCES post(id_post),
 FOREIGN KEY(id_emp) REFERENCES Employer(id_emp)
);
CREATE TABLE tour
( id_type integer PRIMARY KEY not null,
 way varchar(35) not null,
 days varchar(10) not null,
 price money not null
);
CREATE TABLE description_type
( id_type integer NOT NULL UNIQUE,
 people varchar(25) not null,
 hotel_name varchar(25) not null,
 FOREIGN KEY(id_type) REFERENCES tour(id_type)
);
CREATE TABLE orders
(
	id_order integer not null,
	id_type integer not null,
	id_client integer not null,
	FOREIGN KEY (id_type) REFERENCES tour(id_type),
	FOREIGN KEY (id_client) REFERENCES client(id_client)
);
 ALTER TABLE orders
    ADD PRIMARY KEY(id_order);
CREATE TABLE contract (
	id_contract integer PRIMARY KEY NOT NULL,
	dat date not null,
	id_order integer NOT NULL,
	id_emp integer not null,
	FOREIGN KEY (id_emp) REFERENCES Employer(id_emp),
	FOREIGN KEY (id_order) REFERENCES orders(id_order)
	
);

CREATE TABLE status_payment(
	id_pay integer PRIMARY KEY NOT NULL,
	id_contract integer not null,
	dat date not null,
	stage varchar(5) not null,
	FOREIGN KEY (id_contract) REFERENCES contract(id_contract)
);

CREATE TABLE history (
	id_h integer PRIMARY KEY not null,
	id_pay integer not null,
	FOREIGN KEY (id_pay) REFERENCES status_payment(id_pay)
);

ALTER TABLE history
   ADD UNIQUE(id_pay);





