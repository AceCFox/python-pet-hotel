-- db name: pet_hotel 

CREATE TABLE "owner" ("ID" SERIAL PRIMARY KEY, 
"name" VARCHAR(100));

CREATE TABLE "pet" ("ID" SERIAL PRIMARY KEY, 
"name" VARCHAR(100), 
"owner_id" INT REFERENCES "owner",
"breed" VARCHAR(100),
"color" VARCHAR(100), 
"checked-in" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
"checked-out" TIMESTAMP );

INSERT INTO "owner" ("name") VALUES ('Ace');