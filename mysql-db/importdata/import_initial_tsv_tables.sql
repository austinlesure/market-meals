LOAD DATA LOCAL INFILE 'importdata\farmer.tsv' 
INTO TABLE MarketMeals.farmer
LINES TERMINATED BY '\n';