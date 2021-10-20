(import [hyenas[*]])
(import [pandas [read_csv]])

;; Equivalent SQL:
;; 
;; SELECT COUNT("long_name"), AVG("weight_kg") 
;; FROM players 
;; GROUP BY "height_cm"

(print(
    select  :cols [ (count_agg "long_name") (mean_agg "weight_kg")] 
            :from_df (read_csv "/home/lordbertson/Projects/badger/data/players_21.csv") 
            :group_by (group :by ["height_cm"])
))
